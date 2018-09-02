from decoders.secret_decoder import decode_secret


class MessagesGateway:

    def __init__(self, ruler_gateway):
        self.ruler_gateway = ruler_gateway

    def send_message(self, from_kingdom, to_kingdom, message):
        if decode_secret(message.lower(), [to_kingdom.emblem.lower()]):
            return self.ruler_gateway.add_alley(from_kingdom, to_kingdom)
        return False
