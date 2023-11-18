from services.sheet import Sheet


class Sheets:
    def __init__(self, sheets_yaml):
        self.instructions = Sheet(sheets_yaml['instructions'])
        self.inventories = Sheet(sheets_yaml['inventories'])
        self.params = Sheet(sheets_yaml['params'])