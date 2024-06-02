from Person import Person
from auxiliary_functions import getUserInput, onlyNumber

class Student(Person):
  def __init__(self, fullname = "", date_of_birth = "31/12/9999", field_of_study = "", year_of_study = "", grade_point_average = ""):
    super().__init__(fullname, date_of_birth)
    self.field_of_study = field_of_study
    self.year_of_study = year_of_study
    self.gpa = grade_point_average
    self.user_type = "Student"

  def getFieldOfStudy(self):
    return self.field_of_study

  def getYearOfStudy(self):
    return self.year_of_study

  def getGpa(self):
    return self.gpa

  def getUserType(self):
    return self.user_type
  
  # Set function
  def setFieldOfStudy(self):
    new_field_of_study = getUserInput("What is the field of study? ")
    self.field_of_study = new_field_of_study

  def setYearOfStudy(self):
    new_year_of_study = int(onlyNumber(getUserInput("What is the year of study? "), "year of study"))
    self.year_of_study = new_year_of_study

  def setGpa(self):
    new_gpa = int(onlyNumber(getUserInput("What is the gpa? "), "gpa"))
    self.gpa = new_gpa

  def updateStudent(self):
    self.setFullname()
    self.setDateOfBirth()
    self.setFieldOfStudy()
    self.setYearOfStudy()
    self.setGpa()

  def printStudent(self):
    print(f"{self.printPerson()} The field of study is {self.getFieldOfStudy()}, the year of study is {self.getYearOfStudy()}, the gpa is {self.getAge()}, and is a stodent")
 
  def printMySelf(self):
    self.printStudent()


if __name__ == "__main__":
  pass