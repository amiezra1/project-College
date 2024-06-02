from datetime import datetime
from auxiliary_functions import getUserInput

class Person:
    def __init__(self, fullname = "", date_of_birth = "31/12/9999") -> None:
        self.fullname = fullname
        self.date_of_birth = date_of_birth
        self.age = self._calculateAge()
        self.user_type = "Person"

    def _calculateAge(self):
        """Calculates the age based on the date of birth"""
        day, month, year = map(int, self.date_of_birth.split("/"))
        birth_date = datetime(year, month, day)
        current_date = datetime.now()
        month_check_less_year = current_date.month < birth_date.month
        day_check_less_year = current_date.month == birth_date.month and current_date.day <= birth_date.day
        age = current_date.year - birth_date.year - (1 if month_check_less_year or day_check_less_year else 0)

        return int(age)

    # get function
    def getFullname(self):
        return self.fullname
    
    def getDateOfBirth(self):
        return self.date_of_birth

    def getAge(self):
        return self.age

    def getUserType(self):
        return self.user_type
    
    # Set function
    def setFullname(self):
        new_fullname = getUserInput("Enter your name: ")
        self.fullname = new_fullname
        if not self.fullname:
            raise Exception()
      
    def _setAge(self):
        self.age = self._calculateAge()

    def setDateOfBirth(self):
        new_date_of_birth = getUserInput("Enter your date of birth (DD/MM/YYYY): ")
        datetime.strptime(new_date_of_birth, "%d/%m/%Y")
        self.date_of_birth = new_date_of_birth
        self._setAge()
        
    def printPerson(self):
        return f"The person {self.fullname} is {self.age} years old."
   
    def printMySelf(self):
        self.printPerson()

if __name__ == "__main__":
    my_self = Person("Ami Ezra", "15/05/1998")
    fullname = my_self.getFullname()
    age = my_self.getAge()
    date_of_birth = my_self.getDateOfBirth()
    print("Fullname: ", fullname=="Ami Ezra")
    print("Date of birth: ", date_of_birth == "25/09/1998")
    print("age: ", age)