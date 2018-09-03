import random

import constants
import messages
from entities.kingdom import Kingdom
from gateways.kingdom_gateway import KingdomInMemoryGateway
from gateways.message_gateway import MessagesGateway
from gateways.query_intent_gateway import QueryIntentGateway
from gateways.ruler_gateway import RulerInMemoryGateway
from views.query_view import QueryView


def run_ballot_system(query_view, kingdom_gateway, ruler_gateway):
    participant_kingdoms = str(input(
        'Please Enter the kingdoms competing to be the ruler: ')).strip().split(' ')
    kingdom_entities = []
    for participant_kingdom in participant_kingdoms:
        kingdom_entity = kingdom_gateway.get_kingdom_by_name(participant_kingdom)
        kingdom_entities.append(kingdom_entity)
        ruler_gateway.add_ruler(kingdom_entity)
    round_count = 0
    while True:
        round_count += 1
        ruler_gateway.kingdom_allies = []
        for kingdom_entity in kingdom_entities:
            ruler_gateway.add_ruler(kingdom_entity)

        for kingdom_entity in kingdom_entities:
            # print()
            # print('Messages from ', str(kingdom_entity), '......')
            for kingdom in constants.kingdoms:
                random_message = random.choice(constants.random_messages)
                if kingdom.name.lower() == kingdom_entity.name.lower():
                    continue
                # print(str(kingdom) + ", " + random_message)
                query_view.post('send', kingdom_entity, kingdom, random_message)
        print()
        print('Results after round {} ballot count'.format(round_count))
        for kingdom_entity in kingdom_entities:
            ruler = ruler_gateway.get_kingdom(kingdom_entity)
            allies_count = 0
            if ruler:
                allies_count = len(ruler.allies)
            print("Allies for {}: {}".format(kingdom_entity.name, allies_count))
        winners = ruler_gateway.get_max_allies_rulers()
        if len(winners) > 1:
            kingdom_entities = [winner.kingdom for winner in winners]
            continue
        return


def run(ruler_system=''):
    kingdoms = constants.kingdoms
    kingdom_gateway = KingdomInMemoryGateway(kingdoms)
    ruler_gateway = RulerInMemoryGateway(None)
    message_gateway = MessagesGateway(ruler_gateway)
    intent_gateway = QueryIntentGateway()
    query_view = QueryView(
        intent_gateway, kingdom_gateway, ruler_gateway, message_gateway)

    # show helper text
    print(messages.helper_text)
    # start receiving input
    print(messages.prompt_message)
    while True:
        message = input("> ")
        if message == 'exit':
            exit('Good Bye, My Lord!')
        if message == 'debug':
            print([str(k) for k in kingdom_gateway.kingdoms])
            print([str(kl) for kl in ruler_gateway.kingdom_allies])
        if message == 'chicken':
            if ruler_system == 'ballot':
                run_ballot_system(query_view, kingdom_gateway, ruler_gateway)
                continue
            ruler_kingdom = Kingdom('', 'Kingdom Shan')
            for kingdom in constants.kingdoms:
                if kingdom.name.lower() == ruler_kingdom.name.lower():
                    continue
                # random_message = random.choice(constants.random_messages)
                winning_message = random.choice(constants.winning_messages.get(
                    kingdom.emblem.lower(), ['']))
                print(str(kingdom) + ", " + winning_message)
                query_view.post("send", ruler_kingdom, kingdom, winning_message)
            continue
        print(query_view.post(message, system=ruler_system))
