from services.translation import Translation


class Column:
    def __init__(self, column_yaml):
        self.key = column_yaml['key']
        self.type = column_yaml['type']
        self.required = column_yaml['required']
        self.translation = Translation(column_yaml['translation'])
