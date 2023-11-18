from services.choice_list import ChoiceList
from services.column import Column
from services.sheets import Sheets


def generate_columns(columns_yaml):
    columns = []
    for column_yaml in columns_yaml:
        columns.append(Column(column_yaml))
    return columns

def generate_choices(choices_yaml):
    choices = []
    for choice_yaml in choices_yaml:
        choices.append(ChoiceList(choice_yaml))
    return choices

class Template:
    def __init__(self, template_yaml):
        self.name = template_yaml['name']
        self.file_name = template_yaml['file_name']
        self.key = template_yaml['key']

        self.sheets = Sheets(template_yaml['sheets'])

        self.columns = generate_columns(template_yaml['columns'])

        self.choices = generate_choices(template_yaml['choices'])


