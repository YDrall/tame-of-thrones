import constants


class QueryIntentGateway(object):

    def __init__(self):
        pass

    def get_intent(self, query):
        query = query.lower()
        if 'who is' in query:
            return constants.INTENT_GET_RULER
        if 'allies of' in query:
            return constants.INTENT_GET_RULER_ALLIES
        if 'send' in query:
            return constants.INTENT_SEND_MESSAGE_TO_ALLIES
        else:
            raise ValueError('Unable to decode input query.')
