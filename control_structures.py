def classify_number():
    """Classify numbers as positive, negative, or zero."""
    print("Welcome to the Number Classifier!")
    print("Type 'exit' to quit the program.")

    while True:
        user_input = input("Please enter a number (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the classifier. Goodbye!")
            break

        try:
            number = float(user_input)
            if number > 0:
                print(f"{number} is a positive number.")
            elif number < 0:
                print(f"{number} is a negative number.")
            else:
                print("The number is zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    classify_number()