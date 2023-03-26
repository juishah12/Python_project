from student_project_day3_assignment.student_package.student_type import Student
print(Student.school_Name)
print(Student.school_Address)

Student.school_Name = "Saint kabir"
Student.school_Address = "Drive in"

print(Student.school_Name)
print(Student.school_Address)

student1 = Student()
student2 = Student()
student3 = Student()

student1.student_Rollno=1001
student1.student_Name="Jack"
student1.student_Mailid = "jack@gmail.com"
student1.student_Percentage = 45.2

student2.student_Rollno=1002
student2.student_Name="peter"
student2.student_Mailid="peter@gmail.com"
student2.student_Percentage  =85.2

student3.student_Rollno=1003
student3.student_Name="mark"
student3.student_Mailid = "mark@gmail.com"
student3.student_Percentage = 56.5

print(student1.student_Mailid)
print(student2.student_Mailid)
print(student3.student_Mailid)

stu1=student1
stu2=student2
print(stu1)
print(stu2)