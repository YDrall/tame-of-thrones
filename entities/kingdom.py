class Kingdom:
    def __init__(self, emblem, name):
        self.emblem = emblem
        self.name = name

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
