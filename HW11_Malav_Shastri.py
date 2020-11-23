from typing import List, Dict, Tuple, DefaultDict, Any
from Student_Repository_Malav_Shastri import file_reader
from prettytable import PrettyTable
from _collections import defaultdict
import os
import sys
import sqlite3

DB_FILe: str = "/Users/malavshastri/Stevens/Sem 3/SSW810/Student-Repository.db"

"""Passing custom grades as global variable in form of dictionary"""
general_grades: Dict = {"A": 4.0, "A-": 3.75, "B+": 3.25, "B": 3.0, "B-": 2.75,
                        "C+": 2.25, "C": 2.0, "C-": 0.0, "D+": 0.0, "D": 0.0,
                        "D-": 0.0, "F": 0.0}


class Major:
    """This class is ude to give information regarding major.txt file"""
    def __init__(self, major: str):
        self._major: str = major
        self._eleccourse: set = set()
        self._reqcourse: set = set()

    def all_courses(self, course: str, type: str):
        """This function is use to seperate elective and required courses"""
        if type == "R":
            self._reqcourse.add(course)
        elif type == "E":
            self._eleccourse.add(course)
        else:
            print("Invalid Type")
            sys.exit("Type is not valid ")

    def result_return_major(self):
        """This function is use to return the data used in preety table of major summary"""
        return [self._major, sorted(self._reqcourse), sorted(self._eleccourse)]


class Student:
    """Contains information about every student"""
    def __init__(self, cwid: str, name: str, major: str):
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._course: Dict[str, str] = dict()
        self._courseelective: List[str] = list()
        self._courserequired: List[str] = list()

    def comp_courses(self, course: str, grade: str):
        """Use to get completed courses in form of list as keys for this assignment"""
        self._course[course]: Dict[str, int] = general_grades[grade]

    def add_courses(self, course: Any):
        """This function is use know which required and eletive courses is left for a particular student to complete"""
        self._courserequired = list(set(course[1])-set(self._course.keys()))
        if set(course[2]).intersection(set(self._course.keys())):
            self._courseelective = []
        else:
            self._courseelective = list(course[2])

    def result_return_student(self):
        """Use to return the final value of the class student
         and this value is used and printed in pretty table of student summary"""
        try:
            gpa: float = (round(sum(self._course.values()) / len(self._course.values()), 2))
        except ZeroDivisionError:
            gpa: float = 0.0
        return [self._cwid, self._name,
                sorted(self._course.keys()), sorted(self._courserequired),
                sorted(self._courseelective), gpa]


class Instructor:
    """Contains every information about instructor"""
    def __init__(self, cwid: str, name: str, dept: str):
        self._cwid: str = cwid
        self._name: str = name
        self._dept: str = dept
        self._courses: DefaultDict[str, int] = defaultdict(int)

    def add_num_of_students(self, course: str):
        """This function is use to keep the count of number of students taken courses of a particular instructor"""
        self._courses[course] += 1

    def result_return_instructor(self):
        """Use to return the final value of the class instructor
         and this value is used and printed in pretty table of instructor summary"""
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]


class Repository:
    """Contain every information"""
    def __init__(self, path: str):
        self._path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self.mainmajor: Dict[str, Major] = dict()
        self.student_grade_variable = set()
        self.check_student_data()
        self.check_instructor_data()
        self.check_grades_data()
        self.check_majors_data()
        self.cal_required_elective_courses_forstudent()
        self.student_grades_table_db(DB_FILe)
        self.printpretty_1()
        self.printpretty_2()
        self.printpretty_3()
        self.printpretty_4()

    def check_student_data(self):
        """This function read the students.txt file and fill values in self._students"""
        path1: str = os.path.join(self._path, "students.txt")
        try:
            open_file1 = file_reader(path1, fields=3, sep="\t", header=True)
            for cwid, name, major in open_file1:
                self._students[cwid] = Student(cwid, name, major)
        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def check_instructor_data(self):
        """This function read the instructors.txt file and fill values in self._instructors"""
        path2: str = os.path.join(self._path, "instructors.txt")
        try:
            open_file2 = file_reader(path2, fields=3, sep="\t", header=True)
            for cwid, name, dept in open_file2:
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def check_grades_data(self):
        """This function read the grades.txt file and fill values in both self._students and self._instructors"""
        path3: str = os.path.join(self._path, "grades.txt")
        try:
            open_file3 = file_reader(path3, fields=4, sep="\t", header=True)
            for cwid_stud, course, grade, cwid_inst in open_file3:
                if cwid_stud in self._students:
                    if grade != "F":
                        self._students[cwid_stud].comp_courses(course, grade)
                else:
                    print("Invalid Student")
                    sys.exit("New Student CWID found in grades.txt")
                if cwid_inst in self._instructors:
                    self._instructors[cwid_inst].add_num_of_students(course)
                else:
                    print("Invalid Instructor")
                    sys.exit("New Student CWID found in grades.txt")
        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def check_majors_data(self):
        """This function reads the majors.txt file and is use to fill the value of self.mainmajor"""
        path4: str = os.path.join(self._path, "majors.txt")
        try:
            open_file4 = file_reader(path4, fields=3, sep="\t", header=True)
            for major, type, course in open_file4:
                self.mainmajor[major] = Major(major)
            open_file4 = file_reader(path4, fields=3, sep="\t", header=True)
            for major, type, course in open_file4:
                self.mainmajor[major].all_courses(course, type)

        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def cal_required_elective_courses_forstudent(self):
        """This function is use to calculate required and elective courses left for a particular student"""
        path1: str = os.path.join(self._path, "students.txt")
        try:
            open_file1 = file_reader(path1, fields=3, sep="\t", header=True)
            for cwid, name, major in open_file1:
                self._students[cwid].add_courses(self.mainmajor[major].result_return_major())

        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def student_grades_table_db(self, db_path):
        db: sqlite3.Connection = sqlite3.connect(db_path)

        query: str = """SElECT s.Name,s.CWID,g.Course,g.Grade,i.Name
                    from Students s join Grades g join Instructors i
                    on s.CWID=g.StudentCWID and g.InstructorCWID=i.CWID
                    ORDER BY s.Name ASC"""

        for row in db.execute(query):
            self.student_grade_variable.add(row)

        db.close()

        return (sorted(self.student_grade_variable))

    def printpretty_1(self):
        """This function is use to print the prettytable of students summary"""
        print("Student Summary")
        p1: PrettyTable = PrettyTable(field_names=["CWID", "Name",
                                                   "Completed Courses",
                                                   "Remaining Required",
                                                   "Remaining Elective",
                                                   "GPA"])
        testfile_dict1: Dict = dict()
        for a in self._students.values():
            testfile_dict1[a.result_return_student()[0]] = tuple(a.result_return_student()[1:])
            p1.add_row(a.result_return_student())
        print(p1)
        return testfile_dict1

    def printpretty_2(self):
        """This function is use to print the prettytable of instructor summary"""
        print("Instructor Summary")
        p2: PrettyTable = PrettyTable(field_names=["CWID", "Name", "Dept",
                                                   "Course", "Students"])
        testfile_2: Dict = dict()
        for i in self._instructors.values():
            for j in i.result_return_instructor():
                testfile_2[j[0]] = tuple(j[1:])
                p2.add_row(j)

        print(p2)
        return testfile_2

    def printpretty_3(self):
        """This function is use to print the prettytable of major summary"""
        print("Major Summary")
        p3: PrettyTable = PrettyTable(field_names=["Major", "Required Courses",
                                                   "Electives"])
        testfile_3: Dict = dict()
        for i in self.mainmajor.values():
            p3.add_row(i.result_return_major())
            testfile_3[i.result_return_major()[0]] = tuple(i.result_return_major()[1:])

        print(p3)
        return testfile_3

    def printpretty_4(self):
        """This function is use to print the pretty
           table of Student-Grades summary"""
        print("Student Grade Summary")
        p4: PrettyTable = PrettyTable(field_names=["Name", "CWID", "Course",
                                                   "Grade", "Instructor"])
        for Name, CWID, Course, Grade, Instructor in sorted(self.student_grade_variable):
            p4.add_row([Name, CWID, Course, Grade, Instructor])
        print(p4)


def main():
    Repository(r"/Users/malavshastri/Desktop/assignment11")


if __name__ == '__main__':
    main()
