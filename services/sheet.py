from services.translation import Translation


class Sheet:
    def __init__(self, config):
        self.translation = Translation(config['translation'])