-- 1) What is the name of the student with CWID='10115'
-- Answer:
--SELECT Name from Students where CWID="10115"

-- 2) What is the total number of students by major?
-- Answer:
--SELECT COUNT(*) AS cnt,Major from Students group by Major

-- 3) What is the most frequent grade for SSW 810 across all students?
-- Answer:
--SELECT Grade,count(Grade) as cnt from Grades where Course="SSW 810" GROUP BY Grade ORDER BY cnt desc LIMIT 1

-- 4) Display the name and cwid of each student along with the total number of courses taken by the student.
-- Answer:
--SELECT s.CWID,s.Name,COUNT(DISTINCT(g.Course)) AS cnt  from Students s join Grades g on s.CWID=g.StudentCWID GROUP BY s.CWID, s.Name

-- 5) Display each student's name,  CWID, course, grade, and the instructor's name  for all students and grades.  The result should be sorted by the student's name.
-- Answer:
SElECT s.Name,s.CWID,g.Course,g.Grade,i.Name from Students s join Grades g join Instructors i on s.CWID=g.StudentCWID and g.InstructorCWID=i.CWID ORDER BY s.Name ASC