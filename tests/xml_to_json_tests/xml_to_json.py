import filecmp
import os
import xml.etree.ElementTree as ET

from main_program.fileProcessing import xml_to_json_convert


class TestClass(object):

    def test_check_path(self):
        assert os.path.exists('../../main_program/resources/test_data.xml') == True

    def test_check_xml_shema(self):
        tree = ET.parse('../../main_program/resources/test_data.xml')
        root = tree.getroot()
        for item in root.findall('PERSON'):
            assert item.findall('*')[0].tag == 'FIRST_NAME'
            assert item.findall('*')[1].tag == 'LAST_NAME'
            assert item.findall('*')[2].tag == 'YEAR_OF_BIRTH'
            assert item.findall('*')[3].tag == 'MONTH_OF_BIRTH'
            assert item.findall('*')[4].tag == 'DAY_OF_BIRTH'
            assert item.findall('*')[5].tag == 'COMPANY'
            assert item.findall('*')[6].tag == 'PROJECT'
            assert item.findall('*')[7].tag == 'ROLE'
            assert item.findall('*')[8].tag == 'ROOM'
            assert item.findall('*')[9].tag == 'HOBBY'

    def test_check_json_file(self):
        xml_to_json_convert('../../main_program/resources/test_data.xml',
                            '../../main_program/resources/updated_test_data.xml',
                            '../../main_program/resources/prcessed_data.json')
        assert filecmp.cmp('../../main_program/resources/expected.json', '../../main_program/resources/data.json')
