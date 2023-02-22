class student:
    school_Name = None
    school_Address = None

   def __init__(self,rollno,name,mailid,percentage):
       self.student_id = rollno
       self.name= name
       self.mailid = mailid
      # self.percentage = percentage

   def get_student_name(self):
           self.name

   def get_name_with_percentage(self):    return (
   "Hi", self.student_name, "- Your Percentage is", self.student_percentage)

   @staticmethod
   def get_school_detail():
       return student.school_Name +"is located at "+student.school_Address

   #@property
   #def get_student_name(self)
    #   return self.student_name