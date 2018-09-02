from entities.rulerallies import KingdomAllies


class RulerInMemoryGateway:

    def __init__(self, kingdom_allies):
        self.kingdom_allies = kingdom_allies or []

    def get_all_rulers(self):
        return self.kingdom_allies

    def get_kingdom_allies(self, kingdom):
        if not kingdom:
            return []
        kingdom = list(filter(lambda x: x.kingdom == kingdom, self.kingdom_allies))
        if not kingdom:
            return []
        return [alley.name for alley in kingdom[0].allies]

    def get_ruler(self):
        kingdom = list(filter(lambda x: len(x.allies) >= 3, self.kingdom_allies))
        if not kingdom:
            return None
        if len(kingdom) > 1:
            raise ValueError("More that 1 rulers")
        return kingdom[0].kingdom

    def get_kingdom(self, kingdom):
        for k in self.kingdom_allies:
            if k.kingdom.name == kingdom.name:
                return k
        return None

    def add_ruler(self, kingdom):
        kingdom_alley = KingdomAllies([], kingdom)
        self.kingdom_allies.append(kingdom_alley)
        return self.kingdom_allies[-1]

    def add_alley(self, kingdom, alley):
        kingdom_alley = self.get_kingdom(kingdom)
        if not kingdom_alley:
            kingdom_alley = self.add_ruler(kingdom)
        matched_alley = list(filter(lambda x: x.name == alley.name, kingdom_alley.allies))
        if matched_alley:
            return kingdom_alley
        kingdom_alley.allies.append(alley)
        return kingdom_alley
