from typing import Dict, List, DefaultDict
import unittest
from _collections import defaultdict
from HW12_Malav_Shastri import Repository, Student, Instructor, Major


class TestAll(unittest.TestCase):
    """Helps to test all the functions"""

    def test_data_for_pretty1(self):
        """This function is used to test student's pretty table data"""
        R1: Repository = Repository("/Users/malavshastri/Desktop/assignment12")
        calculated = R1.printpretty_1()

        expected: Dict = {'10103': ('Jobs, S',
                                    ['CS 501', 'SSW 810'],
                                    ['SSW 540', 'SSW 555'], [], 3.38),
                          '10115': ('Bezos, J',
                                    ['SSW 810'],
                                    ['SSW 540', 'SSW 555'],
                                    ['CS 501', 'CS 546'], 4.0),
                          '10183': ('Musk, E',
                                    ['SSW 555', 'SSW 810'], ['SSW 540'],
                                    ['CS 501', 'CS 546'], 4.0),
                          '11714': ('Gates, B',
                                    ['CS 546', 'CS 570', 'SSW 810'],
                                    [], [], 3.5)}
        expected1: Dict = {'10103': ('Jobs, S',
                                     ['CS 501', 'SSW 810'],
                                     ['SSW 540', 'SSW 555'], [], 3.38),
                           '10115': ('Bezos, J', ['SSW 810'],
                                     ['SSW 540', 'SSW 555'],
                                     ['CS 501', 'CS 546'], 4.0),
                           '10183': ('Musk, E',
                                     ['SSW 555', 'SSW 810'],
                                     ['SSW 540'], ['CS 501', 'CS 546'], 4.0),
                           '11714': ('Gates, B',
                                     ['CS 546', 'CS 570', 'SSW 810'],
                                     [], [], 3.7)}

        self.assertEqual(calculated, expected)
        self.assertNotEqual(calculated, expected1)

    def test_data_for_pretty2(self):
        """This function is used to test instructor's pretty table data"""
        R2: Repository = Repository("/Users/malavshastri/Desktop/assignment12")
        calculated = R2.printpretty_2()

        expected: Dict = {'98764': ('Cohen, R', 'SFEN', 'CS 546', 1),
                          '98763': ('Rowland, J', 'SFEN', 'SSW 555', 1),
                          '98762': ('Hawking, S', 'CS', 'CS 570', 1)}

        expected1: Dict = {'98764': ('Cohen, R', 'SFEN', 'CS 546', 1),
                           '98763': ('Rowland, J', 'SFEN', 'SSW 555', 1),
                           '98762': ('Hawking, S', 'CS', 'CS 570', 2)}

        self.assertEqual(calculated, expected)
        self.assertNotEqual(calculated, expected1)

    def test_data_for_pretty3(self):
        """This function is used to test major's pretty table data"""
        R3: Repository = Repository("/Users/malavshastri/Desktop/assignment12")
        calculated = R3.printpretty_3()

        expected: Dict = {'SFEN': (['SSW 540', 'SSW 555', 'SSW 810'],
                                   ['CS 501', 'CS 546']),
                          'CS': (['CS 546', 'CS 570'], ['SSW 565', 'SSW 810'])}

        expected1: Dict = {'SFEN': (['SSW 540', 'SSW 555', 'SSW 810'],
                                    ['CS 501', 'CS 546']),
                           'CS': (['CS 546', 'CS 570'],
                                  ['SSW 565', 'SSW 801'])}

        self.assertEqual(calculated, expected)
        self.assertNotEqual(calculated, expected1)

    def test_data_for_pretty4(self):
        """This function is used to test Student-Grade pretty table data"""
        R3: Repository = Repository("/Users/malavshastri/Desktop/assignment12")
        calculated = R3.student_grades_table_db("Student-Repository.db")
        expected: List = [('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
                          ('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
                          ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
                          ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
                          ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
                          ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
                          ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
                          ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
                          ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')]

        expected1: List = [('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
                           ('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
                           ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
                           ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
                           ('Gates, B', '11714', 'SSW 810',
                            'B-', 'Rowland, J'),
                           ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
                           ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
                           ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
                           ('Musk, E', '10183', 'SSW 801', 'A', 'Rowland, J')]

        self.assertEqual(calculated, expected)
        self.assertNotEqual(calculated, expected1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
