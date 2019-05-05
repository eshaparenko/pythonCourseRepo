import json
import xml.etree.ElementTree as ET

import xmltodict as xmltodict


def update_xml_and_save(source, destination):
    tree = ET.parse(source)
    root = tree.getroot()

    for item in root.findall('PERSON'):
        if item.find('FIRST_NAME').text == 'YOUR_FIRST_NAME':
            item.find('FIRST_NAME').text = 'Eugene'
            item.find('LAST_NAME').text = 'Shaparenko'
            item.find('YEAR_OF_BIRTH').text = '1986'
            item.find('MONTH_OF_BIRTH').text = 'August'
            item.find('DAY_OF_BIRTH').text = '1'
            item.find('COMPANY').text = 'Lohika'
            item.find('PROJECT').text = 'Here Mobile'
            item.find('ROLE').text = 'AQA'
            item.find('ROOM').text = '711'
            item.find('HOBBY').text = 'Woodworking'

    tree.write(destination)


def xml_to_json_convert(xml_source, xml_updated, json_destination):
    update_xml_and_save(xml_source, xml_updated)

    with open(xml_updated, "r") as work_data:
        doc = xmltodict.parse(work_data.read())
        f = open(json_destination, 'w')
        f.write(json.dumps(doc, indent=4))


if __name__ == '__main__':
    xml_to_json_convert('resources/test_data.xml', 'resources/updated_test_data.xml', 'resources/data.json')
