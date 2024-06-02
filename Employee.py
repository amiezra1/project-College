from Person import Person
from auxiliary_functions import getUserInput, onlyNumber

class Employee(Person):
  def __init__(self, fullname = "", date_of_birth = "31/12/9999", field_of_work = "", salary = "", seniority = ""):
    super().__init__(fullname, date_of_birth)
    self.salary = salary
    self.field_of_work = field_of_work
    self.seniority = seniority
    self.user_type = "Employee"

  def getFieldOfWork(self):
    return self.field_of_work
  
  def getSalary(self):
    return self.salary

  def getSeniority(self):
    return self.seniority
  
  def getUserType(self):
    return self.user_type
  
  def setSalary(self):
    new_salary = int(onlyNumber(getUserInput("What is the salary? "), "salary"))
    self.salary = new_salary

  def setFieldOfWork(self):
    new_field_of_work = getUserInput("What is the field of work? ")
    self.field_of_work = new_field_of_work

  def setSeniority(self):
    new_seniority = int(onlyNumber(getUserInput("What is the seniority? "), "seniority"))
    self.seniority = new_seniority

  def updateEmployee(self):
    self.setFullname()
    self.setDateOfBirth()
    self.setSalary()
    self.setFieldOfWork()
    self.setSeniority()

  def printEmployee(self):
    print(f"{self.printPerson()} The field of work is {self.getFieldOfWork()}, the salary is {self.getSalary()}, the seniority is {self.getSeniority()}, and is a empliyee")
  
  def printMySelf(self):
    self.printEmployee()


if __name__ == "__main__":
  pass
 