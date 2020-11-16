from typing import Dict, List, DefaultDict
import unittest
from _collections import defaultdict
from HW10_Malav_Shastri import Repository, Student, Instructor, Major


class TestAll(unittest.TestCase):
    """Helps to test all the functions"""

    def test_data_for_pretty1(self):
        """This function is used to test student's pretty table data"""
        R1: Repository = Repository("/Users/malavshastri/Desktop")
        calculated = R1.printpretty_1()

        expected: Dict = {'10103': ('Baldwin, C',
                                    ['CS 501', 'SSW 564',
                                     'SSW 567', 'SSW 687'],
                                    ['SSW 540', 'SSW 555'], [], 3.44),
                          '10115': ('Wyatt, X',
                                    ['CS 545', 'SSW 564',
                                     'SSW 567', 'SSW 687'],
                                    ['SSW 540', 'SSW 555'], [], 3.81),
                          '10172': ('Forbes, I',
                                    ['SSW 555', 'SSW 567'], [
                                        'SSW 540', 'SSW 564'],
                                    ['CS 501', 'CS 513', 'CS 545'], 3.88),
                          '10175': ('Erickson, D',
                                    ['SSW 564', 'SSW 567', 'SSW 687'],
                                    ['SSW 540', 'SSW 555'],
                                    ['CS 501', 'CS 513', 'CS 545'], 3.58),
                          '10183': ('Chapman, O', ['SSW 689'],
                                    ['SSW 540', 'SSW 555',
                                     'SSW 564', 'SSW 567'],
                                    ['CS 501', 'CS 513', 'CS 545'], 4.0),
                          '11399': ('Cordova, I', ['SSW 540'],
                                    ['SYS 612', 'SYS 671', 'SYS 800'],
                                    [], 3.0),
                          '11461': ('Wright, U', ['SYS 611',
                                                  'SYS 750', 'SYS 800'],
                                    ['SYS 612', 'SYS 671'],
                                    ['SSW 540', 'SSW 565', 'SSW 810'], 3.92),
                          '11658': ('Kelly, P', [], ['SYS 612',
                                                     'SYS 671', 'SYS 800'],
                                    ['SSW 540', 'SSW 565', 'SSW 810'], 0.0),
                          '11714': ('Morton, A', ['SYS 611', 'SYS 645'],
                                    ['SYS 612', 'SYS 671', 'SYS 800'],
                                    ['SSW 540', 'SSW 565', 'SSW 810'], 3.0),
                          '11788': ('Fuller, E', ['SSW 540'],
                                    ['SYS 612', 'SYS 671', 'SYS 800'],
                                    [], 4.0)}

        expected1: Dict = {'10103': ('Baldwin, C',
                                     ['CS 501', 'SSW 564',
                                      'SSW 567', 'SSW 687'],
                                     ['SSW 540', 'SSW 555'], [], 3.44),
                           '10115': ('Wyatt, X',
                                     ['CS 545', 'SSW 564',
                                      'SSW 567', 'SSW 687'],
                                     ['SSW 540', 'SSW 555'], [], 3.81),
                           '10172': ('Forbes, I',
                                     ['SSW 555', 'SSW 567'],
                                     ['SSW 540', 'SSW 564'],
                                     ['CS 501', 'CS 513', 'CS 545'], 3.88),
                           '10175': ('Erickson, D',
                                     ['SSW 564', 'SSW 567', 'SSW 687'],
                                     ['SSW 540', 'SSW 555'],
                                     ['CS 501', 'CS 513', 'CS 545'], 3.58),
                           '10183': ('Chapman, O',
                                     ['SSW 689'],
                                     ['SSW 540', 'SSW 555',
                                      'SSW 564', 'SSW 567'],
                                     ['CS 501', 'CS 513', 'CS 545'], 4.0),
                           '11399': ('Cordova, I',
                                     ['SSW 540'],
                                     ['SYS 612', 'SYS 671', 'SYS 800'],
                                     [], 3.0),
                           '11461': ('Wright, U',
                                     ['SYS 611', 'SYS 750', 'SYS 800'],
                                     ['SYS 612', 'SYS 671'],
                                     ['SSW 540', 'SSW 565', 'SSW 810'], 3.92),
                           '11658': ('Kelly, P',
                                     [],
                                     ['SYS 612', 'SYS 671', 'SYS 800'],
                                     ['SSW 540', 'SSW 565', 'SSW 810'], 0.0),
                           '11714': ('Morton, A',
                                     ['SYS 611', 'SYS 645'],
                                     ['SYS 612', 'SYS 671', 'SYS 800'],
                                     ['SSW 540', 'SSW 565', 'SSW 810'], 3.0),
                           '11788': ('Fuller, E',
                                     ['SSW 540'],
                                     ['SYS 612', 'SYS 671', 'SYS 800'],
                                     [], 0.0)}

        self.assertEqual(calculated, expected)
        self.assertNotEqual(calculated, expected1)

    def test_data_for_pretty2(self):
        """This function is used to test instructor's pretty table data"""
        R2: Repository = Repository("/Users/malavshastri/Desktop")
        calculated = R2.printpretty_2()

        expected: Dict = {'98765': ('Einstein, A', 'SFEN', 'SSW 540', 3),
                          '98764': ('Feynman, R', 'SFEN', 'CS 545', 1),
                          '98763': ('Newton, I', 'SFEN', 'SSW 689', 1),
                          '98760': ('Darwin, C', 'SYEN', 'SYS 645', 1)}
        expected1: Dict = {'98765': ('Einstein, A', 'SFEN', 'SSW 540', 3),
                           '98764': ('Feynman, R', 'SFEN', 'CS 545', 1),
                           '98763': ('Newton, I', 'SFEN', 'SSW 689', 1),
                           '98760': ('Darwin, C', 'SYEN', 'SYS 645', 2)}
        self.assertEqual(calculated, expected)
        self.assertNotEqual(calculated, expected1)

    def test_data_for_pretty3(self):
        """This function is used to test major's pretty table data"""
        R3: Repository = Repository("/Users/malavshastri/Desktop")
        calculated = R3.printpretty_3()

        expected: Dict = {'SFEN': (['SSW 540', 'SSW 555',
                                    'SSW 564', 'SSW 567'],
                                   ['CS 501', 'CS 513', 'CS 545']),
                          'SYEN': (['SYS 612', 'SYS 671', 'SYS 800'],
                                   ['SSW 540', 'SSW 565', 'SSW 810'])}
        expected1: dict = {'SFEN': (['SSW 540', 'SSW 555',
                                     'SSW 564', 'SSW 567'],
                                    ['CS 501', 'CS 513', 'CS 545']),
                           'SYEN': (['SYS 612', 'SYS 671', 'SYS 800'],
                                    ['SSW 540', 'SSW 565', 'SSW 801'])}
        self.assertEqual(calculated, expected)
        self.assertNotEqual(calculated, expected1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
