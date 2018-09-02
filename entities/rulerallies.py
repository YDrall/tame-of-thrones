class KingdomAllies:
    def __init__(self, allies, kingdom):
        self.allies = allies
        self.kingdom = kingdom

    def __str__(self):
        return "{}-->{}".format(self.kingdom.name,
                                [al.name for al in self.allies]) or ''

    def __unicode__(self):
        return "{}-->{}".format(self.kingdom.name,
                                [al.name for al in self.allies]) or ''
