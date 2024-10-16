# Задание 2

import xml.etree.ElementTree as ET

database = 'currency.xml'

def parse_xml(data):
    tree = ET.parse(data)
    root = tree.getroot()
    ans_dict = {}
    valutes = root.findall('Valute')

    for val in valutes:
        char_code = val.find('CharCode').text
        nominal = int(val.find('Nominal').text)  # Преобразуем номинал в целое число
        ans_dict[char_code] = nominal
    return ans_dict


if __name__ == '__main__':
    result = parse_xml(database)
    print(result)
