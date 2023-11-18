import os

import xlsxwriter
import yaml

from services.template import Template

TEMPLATES_DIRECTORY = 'config/templates'
FILE_NAME = 'decentralized_workplace.yml'

FILE_PATH = TEMPLATES_DIRECTORY + '/' + FILE_NAME

BUILD_DIRECTORY = 'build'

TRANSLATION_KEYS = ['fr', 'en']

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def create_sheet(workbook, sheet, translation_key):
    return workbook.add_worksheet(sheet.translation.go_for(translation_key))


def letters(index):
    c = index % ALPHABET.__len__()
    c2 = index // ALPHABET.__len__()
    if c2 > 0:
        return ALPHABET[c2 - 1] + ALPHABET[c]
    else:
        return ALPHABET[c]


def workbook_name(template, translation_key):
    return 'build/' + template.key + '.' + translation_key + '.xlsx'


def generate_header(sheet, columns, translation_key):
    for index, column in enumerate(columns):
        sheet.write(letters(index) + '1', column.translation.go_for(translation_key))


def generate_validation(sheet, columns, choices, translation_key):
    for choice in choices:
        for column_index, item in enumerate(columns):
            if item.key == choice.key:
                break
        else:
            column_index = -1

        sheet.data_validation(
            letters(column_index) + '2', {"validate": "list", "source": choice.list(translation_key)}
        )


if __name__ == '__main__':
    with open(FILE_PATH, 'r') as file:
        if not os.path.exists(BUILD_DIRECTORY):
            os.makedirs(BUILD_DIRECTORY)

        content = yaml.safe_load(file)
        template = Template(content['template'])
        sheets = template.sheets
        columns = template.columns
        choices = template.choices

        for translation in TRANSLATION_KEYS:
            workbook = xlsxwriter.Workbook(workbook_name(template, translation))
            home_sheet = create_sheet(workbook, sheets.instructions, translation)
            inventories_sheet = create_sheet(workbook, sheets.inventories, translation)
            params_sheet = create_sheet(workbook, sheets.params, translation)

            generate_header(home_sheet, columns, translation)
            generate_validation(inventories_sheet, columns, choices, translation)

            workbook.close()
