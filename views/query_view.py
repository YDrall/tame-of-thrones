import constants


class QueryView(object):

    def __init__(self, intent_gateway,
                 kingdom_gateway, ruler_gateway,
                 message_gateway):
        self.intent_gateway = intent_gateway
        self.kingdom_gateway = kingdom_gateway
        self.ruler_gateway = ruler_gateway
        self.message_gateway = message_gateway

    def post(self, input_message, from_kingdom=None,
             to_kingdom=None, secret=None, system=''):
        try:
            intent = self.intent_gateway.get_intent(input_message)
        except ValueError as err:
            return str(err)

        if intent == constants.INTENT_GET_RULER:
            return self.ruler_gateway.get_ruler(system)
        if intent == constants.INTENT_GET_RULER_ALLIES:
            ruler = self.ruler_gateway.get_ruler(system)
            return self.ruler_gateway.get_kingdom_allies(ruler)
        if intent == constants.INTENT_SEND_MESSAGE_TO_ALLIES:
            return self.message_gateway.send_message(
                from_kingdom, to_kingdom, secret)
