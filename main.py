import os
import user_utils as uu

# Menu
def printMenuAndChoice():
    """Prints the menu options and returns the user's choice."""
    print("1.Save a new entry")
    print("2.Search by ID")
    print("3.Print ages average")
    print("4.Print all names")
    print("5.Print all IDs")
    print("6.Print all entries")
    print("7.Print entry by index")
    print("8.Save all data")
    print("9.Exit")
           
    user_choice = uu.getUserInput("Please entry your choice: ")
    if not user_choice:
        return "-1"
    return user_choice


def main():
    choice = printMenuAndChoice()
    users = {}
    ages_sum = 0

    while choice != "Exit":
        while len(users) == 0:
                if choice == "1":
                    break
                else:
                    os.system("cls")     
                    print("The list is empty. Please fill it in before using this option.")
                    choice = printMenuAndChoice()

        if choice == "1":
            save_user = uu.addNewUser(users, ages_sum)
            if save_user:
                ages_sum = save_user
        elif choice == "2":
            uu.searchById(users)
        elif choice == "3":
            uu.calculateAverageAge(users, ages_sum)
        elif choice == "4":
            uu.printAllNames(users)
        elif choice == "5":
            uu.printAllIds(users)
        elif choice == "6":
            uu.PrintAllEntries(users)
        elif choice == "7":
            uu.printEntryByIndex(users)
        elif choice == "8":
            uu.writeUserDataToCsv(users)
        elif choice == "9":
            break
        elif choice == "-1":
            pass
        else:
            print(f"Error: The index must be a number between 1-9. '{choice}' is not a number between 1-9.")

        uu.getUserInput("Press Enter to continue")
        os.system("cls")
        choice = printMenuAndChoice()

if __name__ == "__main__":
    main()
