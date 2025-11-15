# This program demonstrates proper indentation, comments, and variables
# following PEP 8 style guidelines.

def greet_user():
    """Function to greet the user."""
    
    user_name = "Bhavy"      # Variable storing the user's name
    greeting_message = "Hello, " + user_name  # Creating greeting message

    # Printing the greeting message
    print(greeting_message)


def main():
    """Main function of the program."""
    
    greet_user()  # Call the function to greet the user


# This condition ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
