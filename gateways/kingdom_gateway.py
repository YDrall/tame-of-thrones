from decoders.secret_decoder import decode_secret


class KingdomInMemoryGateway:

    def __init__(self, kingdoms):
        self.kingdoms = kingdoms

    def get_all_kingdoms(self):
        return self.kingdoms

    def get_kingdom_by_emblem(self, emblem):
        matched_kingdom = list(filter(lambda x: x.emblem == emblem, self.kingdoms))
        if not matched_kingdom:
            raise ValueError("Kingdom doesn't exists with emblem '{}'".format(emblem))
        if len(matched_kingdom) > 1:
            raise ValueError("More than one kingdoms for {}".format(emblem))

        return matched_kingdom[0]

    def get_kingdom_by_name(self, name):
        matched_kingdom = list(filter(lambda x: x.name.lower() == name.lower(), self.kingdoms))
        if not matched_kingdom:
            raise ValueError("Kingdom doesn't exists with name {}".format(name))
        if len(matched_kingdom) > 1:
            raise ValueError("More than one kingdoms for {}".format(name))

        return matched_kingdom[0]

