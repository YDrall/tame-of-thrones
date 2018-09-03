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

    def get_ruler(self, system=''):
        if system == 'ballot':
            ruler = self.get_max_allies_rulers()
            if not ruler:
                return None
            return ruler[-1].kingdom
        kingdom = list(filter(lambda x: len(x.allies) >= 3, self.kingdom_allies))
        if not kingdom:
            return None
        if len(kingdom) > 1:
            raise ValueError("More that 1 rulers")
        return kingdom[0].kingdom

    def get_max_allies_rulers(self):
        all_rulers = self.get_all_rulers()
        if not all_rulers:
            return []
        all_rulers.sort(key=lambda x: len(x.allies))

        max_allies = len(all_rulers[-1].allies)
        winner_allies = list(filter(
            lambda x: len(x.allies) >= max_allies, self.kingdom_allies))
        return winner_allies

    def get_kingdom(self, kingdom):
        for k in self.kingdom_allies:
            if k.kingdom.name == kingdom.name:
                return k
        return None

    def get_alley_kingdom(self, alley):
        for k in self.kingdom_allies:
            for k_alley in k.allies:
                if alley.name == k_alley.name:
                    return k.kingdom
        return None

    def add_ruler(self, kingdom):
        kingdom_alley = KingdomAllies([], kingdom)
        self.kingdom_allies.append(kingdom_alley)
        return self.kingdom_allies[-1]

    def add_alley(self, kingdom, alley):
        # print('Adding alley, kingdom: ', kingdom, 'alley: ', alley)
        is_alley_ruler = list(filter(
            lambda x: x.kingdom.name == alley.name, self.get_all_rulers()))
        if is_alley_ruler:
            # If the receiving kingdom is competing to be the ruler,
            # they will not give their allegiance
            # print('receiving kingdom is competing to be the ruler')
            return self.get_kingdom(kingdom)
        kingdom_alley = self.get_kingdom(kingdom)
        if not kingdom_alley:
            kingdom_alley = self.add_ruler(kingdom)
        if self.get_alley_kingdom(alley):
            # if alley already belongs to another kingdom then no need to add it
            return kingdom_alley
        # print('adding alley ', alley, 'to kingdom', kingdom)
        kingdom_alley.allies.append(alley)
        return kingdom_alley
