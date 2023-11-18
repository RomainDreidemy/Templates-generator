class Translation:
    def __init__(self, t):
        self.fr = t['fr']
        self.en = t['en']

    def go_for(self, key):
        return getattr(self, key)
