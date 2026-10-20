from app import app, db
from app.main.models import Course, Major, Student, Enrolled
from config  import Config

import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
import os
#os.remove("student.db")

app.app_context().push()

db.create_all()

# Add couple Majors
major1 = Major(name = 'CS', department = 'Computer Science')
db.session.add(major1)
major2 = Major(name = 'DS', department = 'Computer Science')
db.session.add(major2)
major3 = Major(name = 'ME', department = 'Mechanical Engineering')
db.session.add(major3)
major4 = Major(name = 'RBE', department = 'Robotics Engineering')
db.session.add(major4)
major5 = Major(name = 'MATH', department = 'Mathematics')
db.session.add(major5)
major6 = Major(name = "PSY", department = "Psychology")
db.session.add(major6)
major7 = Major(name = 'ECO', department = 'Economics')
db.session.add(major7)
major8 = Major(name = 'ENG', department = 'English')
db.session.add(major8)
major9 = Major(name = 'HIS', department = 'History')
db.session.add(major9)
major10 = Major(name = 'MUS', department = 'Music')
db.session.add(major10)
db.session.commit()

# print Majors
for major in db.session.scalars(sqla.select(Major)):
    print(major)

#---------------------------------------------------
# Add courses

major1 = db.session.scalars(sqla.select(Major).where(Major.name == 'CS')).first()
major2 = db.session.scalars(sqla.select(Major).where(Major.name == 'RBE')).first()
major3 = db.session.scalars(sqla.select(Major).where(Major.name == 'DS')).first()
major4 = db.session.scalars(sqla.select(Major).where(Major.name == 'ME')).first()
major5 = db.session.scalars(sqla.select(Major).where(Major.name == 'MATH')).first()
major6 = db.session.scalars(sqla.select(Major).where(Major.name == 'PSY')).first()
major7 = db.session.scalars(sqla.select(Major).where(Major.name == 'ECO')).first()
major8 = db.session.scalars(sqla.select(Major).where(Major.name == 'ENG')).first()
major9 = db.session.scalars(sqla.select(Major).where(Major.name == 'HIS')).first()
major10 = db.session.scalars(sqla.select(Major).where(Major.name == 'MUS')).first()


c1 = Course(coursenum='3733',majorid = major1.id, title='Software Engineering') # course is associated with major1
db.session.add(c1)
c2 = Course(coursenum='3431',majorid = major1.id, title='Database Systems')     # course is associated with major1
db.session.add(c2)
c3 = Course(coursenum='1001',majorid = major2.id, title='Introduction to Robotics')     # course is associated with major2
db.session.add(c3)
c4 = Course(coursenum='4345',majorid = major3.id, title='Multi-Agent Systems')
db.session.add(c4)
c5 = Course(coursenum='3820',majorid = major4.id, title='Computer-Aided Manufacturing')
db.session.add(c5)
c6 = Course(coursenum='2300',majorid = major4.id, title='Introduction to Engineering Design')
db.session.add(c6)
c7 = Course(coursenum='1022',majorid = major5.id, title='Calculus II')
db.session.add(c7)
c8 = Course(coursenum='2216',majorid = major6.id, title='Introduction to Psychology')
db.session.add(c8)
c9 = Course(coursenum='3233',majorid = major5.id, title='Discrete Optimization')
db.session.add(c9)
c10 = Course(coursenum='1001',majorid = major7.id, title='Principles of Microeconomics')
db.session.add(c10)
c11 = Course(coursenum='3028',majorid = major8.id, title='Literary Theory')
db.session.add(c11)
c12 = Course(coursenum='4815',majorid = major2.id, title='Industrial Robostics')
db.session.add(c12)
c13 = Course(coursenum='2601',majorid = major9.id, title='Civil War and the World')
db.session.add(c13)
c14 = Course(coursenum='2101',majorid = major10.id, title='Arranging and Orchestration')
db.session.add(c14)
c15 = Course(coursenum='3110',majorid = major10.id, title='Jazz Theory')
db.session.add(c15)
db.session.commit()

# print Courses
for course in db.session.scalars(sqla.select(Course)):
    print(course)

#---------------------------------------------------
# Add Students

s1 = Student(username='sarslanay', firstname = 'Sakire', lastname = 'Arslan Ay', email='sarslan@wpi.edu', address = '100 Institute Road, Worcester, MA 01609') 
s1.set_password('123')
db.session.add(s1)

s2 = Student(username='jfyates', firstname = 'John', lastname = 'Yates', email='jfyates@wpi.edu', address = "100 Institute Road, Worcester, MA 01609")  #address is optional
s2.set_password('123')
db.session.add(s2)

s3 = Student(username='amfstrong', firstname = 'Adam', lastname = 'Strong', email='amfstrong@wpi.edu', address = '100 Institute Road, Worcester, MA 01609')  #address is optional
s3.set_password('123')
db.session.add(s3)

s4 = Student(username='jjlovern', firstname = 'Janice', lastname = 'Lovern', email='jjlovern@wpi.edu', address = '2391 North Street, Worcester, MA 01609')
s4.set_password('123')
db.session.add(s4)

s5 = Student(username='yomar2', firstname="Yasmin", lastname = 'Omar', email='yomar2@wpi.edu', address = '837 South Street, Worcester, MA 01609')
s5.set_password('123')
db.session.add(s5)

s6 = Student(username='edstrom', firstname="Eric", lastname = 'Strom', email='edstrom@wpi.edu', address = '102 East Street, Worcester, MA 01609')
s6.set_password('123')
db.session.add(s6)

s7 = Student(username='lmarmstrong', firstname = 'Louisa', lastname = 'Armstrong', email='lmarmstrong@wpi.edu', address = '3 Cherry Road, Shrewsbury, MA 01609')
s7.set_password('123')
db.session.add(s7)

s8 = Student(username='bpolear', firstname = 'Brian', lastname = "Olear", email='bpolear@wpi.edu', address = '374 Star Lane, Los Angeles, MA 01609')
s8.set_password('123')
db.session.add(s8)

db.session.commit()

# print students
for student in db.session.scalars(sqla.select(Student)):
    print(student)

#---------------------------------------------
# query Tables
s1 = db.session.scalars(sqla.select(Student).where(Student.username == 'sarslanay')).first()
s2 = db.session.scalars(sqla.select(Student).where(Student.username == 'jfyates')).first()
s3 = db.session.scalars(sqla.select(Student).where(Student.username == 'amfstrong')).first()
s4 = db.session.scalars(sqla.select(Student).where(Student.username == 'jjlovern')).first()
s5 = db.session.scalars(sqla.select(Student).where(Student.username == 'yomar2')).first()
s6 = db.session.scalars(sqla.select(Student).where(Student.username == 'edstrom')).first()
s7 = db.session.scalars(sqla.select(Student).where(Student.username == 'lmarmstrong')).first()
s8 = db.session.scalars(sqla.select(Student).where(Student.username == 'bpolear')).first()


c1 = db.session.scalars(sqla.select(Course).where(Course.majorid == major1.id).where(Course.coursenum == '3733')).first()
c2 = db.session.scalars(sqla.select(Course).where(Course.majorid == major1.id).where(Course.coursenum == '3431')).first()
c3 = db.session.scalars(sqla.select(Course).where(Course.majorid == major2.id).where(Course.coursenum == '1001')).first()
c4 = db.session.scalars(sqla.select(Course).where(Course.majorid == major3.id).where(Course.coursenum == '4345')).first()
c5 = db.session.scalars(sqla.select(Course).where(Course.majorid == major4.id).where(Course.coursenum == '3820')).first()
c6 = db.session.scalars(sqla.select(Course).where(Course.majorid == major4.id).where(Course.coursenum == '2300')).first()
c7 = db.session.scalars(sqla.select(Course).where(Course.majorid == major5.id).where(Course.coursenum == '1022')).first()
c8 = db.session.scalars(sqla.select(Course).where(Course.majorid == major6.id).where(Course.coursenum == '2216')).first()
c9 = db.session.scalars(sqla.select(Course).where(Course.majorid == major5.id).where(Course.coursenum == '3233')).first()
c10 = db.session.scalars(sqla.select(Course).where(Course.majorid == major7.id).where(Course.coursenum == '1001')).first()
c11 = db.session.scalars(sqla.select(Course).where(Course.majorid == major8.id).where(Course.coursenum == '3028')).first()
c12 = db.session.scalars(sqla.select(Course).where(Course.majorid == major2.id).where(Course.coursenum == '4815')).first()
c13 = db.session.scalars(sqla.select(Course).where(Course.majorid == major9.id).where(Course.coursenum == '2601')).first()
c14 = db.session.scalars(sqla.select(Course).where(Course.majorid == major10.id).where(Course.coursenum == '2101')).first()
c15 = db.session.scalars(sqla.select(Course).where(Course.majorid == major10.id).where(Course.coursenum == '3110')).first()


# associate the Students with Majors  (Many-to-Many relationship through 'students_majors_table' association table)
s1.majors_of_student.add(major1)   # student1 double majors in CS and RBE
s1.majors_of_student.add(major2)   
s2.majors_of_student.add(major3)   # student2 only majors in RBE
s3.majors_of_student.add(major1)   # student3 only majors in CS
s4.majors_of_student.add(major6)
s4.majors_of_student.add(major10)
s5.majors_of_student.add(major4)
s6.majors_of_student.add(major5)
s6.majors_of_student.add(major7)
s7.majors_of_student.add(major8)
s8.majors_of_student.add(major5)
db.session.commit()

enroll1 = Enrolled( course_enrolled = c1, student_enrolled = s1)
db.session.add(enroll1)
enroll2 = Enrolled( course_enrolled = c2, student_enrolled = s1)
db.session.add(enroll2)
enroll3 = Enrolled( course_enrolled = c1, student_enrolled = s2)
db.session.add(enroll3)
enroll4 = Enrolled( course_enrolled = c1, student_enrolled = s3)
db.session.add(enroll4)
enroll5 = Enrolled( course_enrolled = c2, student_enrolled = s3)
db.session.add(enroll5)
enroll6 = Enrolled( course_enrolled = c3, student_enrolled = s3)
db.session.add(enroll6)
enroll7 = Enrolled( course_enrolled = c14, student_enrolled = s4)
db.session.add(enroll7)
enroll8 = Enrolled( course_enrolled = c15, student_enrolled = s4)
db.session.add(enroll8)
enroll9 = Enrolled( course_enrolled = c8, student_enrolled = s4)
db.session.add(enroll9)
enroll10 = Enrolled( course_enrolled = c4, student_enrolled = s5)
db.session.add(enroll10)
enroll11 = Enrolled( course_enrolled = c5, student_enrolled = s5)
db.session.add(enroll11)
enroll12 = Enrolled( course_enrolled = c7, student_enrolled = s6)
db.session.add(enroll12)
enroll13 = Enrolled( course_enrolled = c10, student_enrolled = s6)
db.session.add(enroll13)
enroll14 = Enrolled( course_enrolled = c11, student_enrolled = s7)
db.session.add(enroll14)
enroll15 = Enrolled( course_enrolled = c7, student_enrolled = s8)
db.session.add(enroll15)
enroll15 = Enrolled( course_enrolled = c9, student_enrolled = s8)
db.session.add(enroll15)
db.session.commit()

