""" Script implements file manipulating operations """
import csv
import os
from datetime import datetime, timedelta
from prettytable import PrettyTable


def date_arithmetic():
    """ Code segment for date arithmetic problems """
    date1 = 'Feb 27, 2000'
    date2 = 'Feb 27, 2017'
    date3 = 'Jan 1, 2017'
    date4 = 'Oct 31, 2017'

    dt1 = datetime.strptime(date1, '%b %d, %Y')
    dt2 = datetime.strptime(date2, '%b %d, %Y')
    dt3 = datetime.strptime(date3, '%b %d, %Y')
    dt4 = datetime.strptime(date4, '%b %d, %Y')

    delta = dt4 - dt3

    d1 = f'3 days after {dt1:%m/%d/%y} is {(dt1 + timedelta(days=3)):%m/%d/%y}'
    d2 = f'3 days after {dt2:%m/%d/%y} is {(dt2 + timedelta(days=3)):%m/%d/%y}'
    d3 = f'{delta.days} passed between {dt3:%m/%d/%y} and {dt4:%m/%d/%y}'

    return d1, d2, d3


def file_reader(path, fields, sep, header=False):
    """ Generator to return fields from the file """
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist')
    else:
        with fp:
            count = 0
            reader = csv.reader(fp, delimiter=sep)

            for line in reader:
                count += 1
                if len(line) != fields:
                    raise ValueError(f'{path} has {len(line)} fields on line {count} but expected {fields}')

                if header is False:
                    yield tuple(line)
                else:
                    header = False


class FileAnalyzer():
    """ Class for analyzing the file """
    def __init__(self, directory):
        self.directory = directory
        self.files_summary = dict()
        self.analyze_files()

    def analyze_files(self):
        """ Analyze the files """
        path = self.directory
        try:
            dr = os.listdir(path)
        except FileNotFoundError:
            raise FileNotFoundError('No such directory')
        else:
            for file in dr:
                if file.endswith('.py'):
                    try:
                        fp = open(os.path.join(path, file), 'r',
                                  encoding='utf8')
                    except FileNotFoundError:
                        raise FileNotFoundError('File does not exist')
                    else:
                        with fp:
                            char_count, class_count = 0, 0
                            func_count, line_count = 0, 0

                            for line in fp:
                                char_count += len(line)
                                line_count += 1

                                if line.startswith('class '):
                                    class_count += 1

                                if line.strip().startswith('def '):
                                    func_count += 1

                            self.files_summary[file] = {
                                'class': class_count,
                                'function': func_count,
                                'line': line_count,
                                'char': char_count
                            }

        return self.files_summary

    def pretty_print(self):
        """ Return the table """
        x = PrettyTable()
        x.field_names = ['File Name', 'Classes',
                         'Functions', 'Lines', 'Characters']

        for i, j in self.files_summary.items():
            x.add_row([i, j['classes'], j['functions'],
                      j['lines'], j['characters']])

        return x
