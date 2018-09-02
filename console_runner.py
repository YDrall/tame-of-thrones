import random

import constants
import messages
from entities.kingdom import Kingdom
from gateways.kingdom_gateway import KingdomInMemoryGateway
from gateways.message_gateway import MessagesGateway
from gateways.query_intent_gateway import QueryIntentGateway
from gateways.ruler_gateway import RulerInMemoryGateway
from views.query_view import QueryView


def run():
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
        print(query_view.post(message))
