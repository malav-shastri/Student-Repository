"""Test file use to test all the cases used in the HW08_Test_Malav_Shastri.py file"""
from typing import Dict, List
import unittest
from datetime import datetime

from HW08_Malav_Shastri import date_arithmetic, file_reader, FileAnalyzer


class TestAll(unittest.TestCase):
    """Helps to test all the functions"""
    def test_data_arithmetic(self):
        """Function is used to test data_arithmetic"""
        self.assertEqual(date_arithmetic(), ('3 days after 02/27/00 is 03/01/00',
                                             '3 days after 02/27/17 is 03/02/17',
                                             '303 passed between 01/01/17 and 10/31/17'))
        self.assertNotEqual(date_arithmetic(), ('3 days after 02/27/00 is 03/01/00',
                                                '3 days after 02/27/17 is 03/02/17',
                                                '303 passed between 01/01/17 and 10/31/18'))
        self.assertNotEqual(date_arithmetic(), ('3 days after 02/27/00 is 03/01/00',
                                                '3 days after 02/27/17 is 03/02/17',
                                                '303 passed between 01/01/17 and 10/31/19'))

    def test_file_reader(self):
        """Function is used to test file_reader"""
        path = "text1.txt"
        file1 = list()
        expected: List = ["('123', 'Jin He', 'Computer Science')",
                          "('234', 'Nanda Koka', 'Software Engineering')",
                          "('345', 'Benji Cai', 'Software Engineering')"]

        for items in file_reader(path, 3, sep='|', header=True):
            file1.append(f"{items}")
        self.assertEqual(file1, expected)

        for items in file_reader(path, 3, sep='|', header=False):
            file1.append(f"{items}")
        self.assertNotEqual(file1, expected)

    def test__analyze_file(self):
        """Function is used to test analyze_files function"""
        f1: FileAnalyzer = FileAnalyzer(r"/Users/malavshastri/Stevens/Sem 3/SSW810/assignment5")

        expected: Dict = {
            'HW05_Test_Malav_Shastri.py': {
                'class': 4,
                'function': 4,
                'line': 50,
                'char': 2221
            },
            'HW05_Malav_Shastri.py': {
                'class': 1,
                'function': 5,
                'line': 68,
                'char': 2536
            }
        }
        expected1: Dict = {
            'HW05_Test_Malav_Shastri.py': {
                'class': 0,
                'function': 5,
                'line': 61,
                'char': 1975
            },
            'HW05_Malav_Shastri.py': {
                'class': 1,
                'function': 5,
                'line': 57,
                'char': 2742
            }
        }
        self.assertEqual(f1.analyze_files(), expected)
        self.assertNotEqual(f1.analyze_files(), expected1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
