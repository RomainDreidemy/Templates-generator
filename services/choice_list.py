from services.translation import Translation


def values(values_yaml):
    values = []
    for value_yaml in values_yaml:
        values.append(Translation(value_yaml['translation']))
    return values


class ChoiceList:
    def __init__(self, choice_list_yaml):
        self.key = choice_list_yaml['key']
        self.values = values(choice_list_yaml['values'])

    def list(self, translation):
        return [value.go_for(translation) for value in self.values]
