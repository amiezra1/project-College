# Auxiliary functions
def getUserInput(input_for_try):
    """Gets user input, handles keyboardinterrupt gracefully."""
    try:
        user_input = input(input_for_try)
        return user_input
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: You return to the menu.If you wish to exit, you can choose option 9.")
        return None


def onlyNumber(num_as_str, item_text):
    """Checks if a string is a number."""
    if not num_as_str.isdigit():
        raise Exception(f"Error: {item_text} must be a number. '{num_as_str}' is not a number.")
    return num_as_str


def getUserType(question):
    """Gets user type input and validate it."""
    user_type = getUserInput(question).lower()
    if user_type == "e" or user_type == "s":
        return user_type
    print("Invalid input. Please enter 'S' for Student or 'E' for Employee.")
    return None


def printEntry(user_id, user_data = None) -> None:
    """Prints the user's details"""
    print("ID:", user_id)
    user_data.printMySelf()


if __name__ == "__main__":
  pass