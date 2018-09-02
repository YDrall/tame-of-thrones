from decoders.secret_decoder import decode_secret


class KingdomInMemoryGateway:

    def __init__(self, kingdoms):
        self.kingdoms = kingdoms

    def get_all_kingdoms(self):
        return self.kingdoms

    def get_kingdom_by_emblem(self, emblem):
        matched_kingdom = list(filter(lambda x: x.emblem == emblem, self.kingdoms))
        if not matched_kingdom:
            raise ValueError("Kingdom doesn't exists")
        if len(matched_kingdom) > 1:
            raise ValueError("More than one kingdoms for {}".format(emblem))

        return matched_kingdom[0]
