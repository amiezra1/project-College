import os
import json
import pandas as pd
from Student import Student
from Employee import Employee
from auxiliary_functions import getUserInput, onlyNumber, getUserType, printEntry

# Auxiliary functions

def addNewUser(users, ages_sum):
    """Adds a new user."""
    user_type = getUserType("Do you want to add a student or employee?('S' for Stodent 'E' for Employee): ")
    if not user_type:
        return None
    try:
        new_id = onlyNumber(getUserInput("ID: "), "ID")
        if not new_id:
            return None
    except Exception as e:
        print(e)
        return None
    
    if new_id in users:
        print(f"ID {new_id} already exists.")
        return None
    
    try:        
        if user_type == "e":
            my_person = Employee()
            my_person.updateEmployee()
        elif user_type == "s":
            my_person = Student()
            my_person.updateStudent()
    except Exception as e:
        print(e)
        return None
    
    users[new_id] = my_person
    try:
        ages_sum += my_person.getAge()
    except Exception as e:
        print(e)
        
    print(f"User with ID [{new_id}] added successfully.")
    return ages_sum


def printEntryByIndex(users):
    """Gets an id from the user and prints it"""
    try:
        index = onlyNumber(getUserInput("Please enter the index of the entry want to print: "), "Index")
    except:
        return None
    index = int(index)
    if 0 <= index < len(users):
        for i, key in enumerate(users):
            if i == index:
                printEntry(key, users[key])
    else:
        max_index = len(users) - 1
        print(f"There are between 0-{max_index} records, choose something in that range ")


def searchById(users):
    """Searches for a user by ID."""
    id_user = getUserInput("Please enter the ID you want to look for: ")
    if not id_user:
        return None
    if id_user in users:
        printEntry(id_user, users[id_user])
    else:
        print(f"id {id_user} does not exist")


def calculateAverageAge(users, ages_sum):
    """Calculates and prints the average age of all users."""
    total_users = len(users)
    print_ages_average = ages_sum / total_users
    print("Average age:", print_ages_average)


def printAllNames(users):
    """Prints the names of all users."""
    for user in users:
        print("name: " + users[user].getFullname())


def printAllIds(users):
    """Prints all the IDs of users."""
    location_id = 0
    for user in users:
        print(f"ID {location_id}: {user}")
        location_id += 1


def PrintAllEntries(users):
    """Prints details of all users."""
    location_user = 0
    for user in users:
        print(f"User the {location_user} place")
        printEntry(user, users[user])
        location_user += 1


def writeUserDataToCsv(users):
    """The function receives the header from the conf.json file and the data from variable users, then it finds the data in the file that the user submit"""
    # Input file
    path_input_file = "conf.json"
    if not os.path.exists(path_input_file):
        print(f"Error: config file conf.json is missing in path {os.getcwd()}")
        return None
    print("Note that you need to change the column names in the 'conf.json' file according to the type you are exporting")
    user_type = getUserType("Do you want to export a student or employee?('S' for Stodent 'E' for Employee): ")
    
    # Output file
    file_name_output = getUserInput("What is your output file name? ")
    if not file_name_output:
        return None
    if not file_name_output.endswith(".csv"):
        print("he file name must end with an '.csv'")
        return None

    # Open input file
    with open(path_input_file) as inpout_titles:
        load_titles = json.load(inpout_titles)

    # Create output file
    try:
        id_title = load_titles["id"]
        name_title = load_titles["name"]
        age_title = load_titles["age"]
        work_or_study_title = load_titles["workOrStudy"]
        salary_or_gpa_title = load_titles["salaryOrGpa"]
        seniority_or_year_of_study_title = load_titles["seniorityOrYearOfStudy"]
        user_type_column = load_titles["userType"]
    except Exception as e:
        print(f"Missing configuration for {e} in the 'conf.json' file.")
        return None

    data = []    
    for user_id, user_data in users.items():
        if user_type == "s":
            dict_for_csv = {
            id_title: user_id,
            name_title: user_data.getFullname(),
            age_title: user_data.getAge(),
            work_or_study_title: user_data.getFieldOfStudy(),
            salary_or_gpa_title: user_data.getGpa(),
            seniority_or_year_of_study_title: user_data.getYearOfStudy(),
            user_type_column: user_data.userType()
            }
            data.append(dict_for_csv)
        elif user_type == "e":
            dict_for_csv = {
           id_title: user_id,
           name_title: user_data.getFullname(),
           age_title: user_data.getAge(),
           work_or_study_title: user_data.getFieldOfWork(),
           salary_or_gpa_title: user_data.getSalary(),
           seniority_or_year_of_study_title: user_data.getSeniority(),
           user_type_column: user_data.userType()
            }
            data.append(dict_for_csv)
    df = pd.DataFrame(data)

    try:
        df.to_csv(file_name_output, index = False)
        print(f"The data was added to the {file_name_output} file successfully")
    except Exception as e:
        print(e)
        return None