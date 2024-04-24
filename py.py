while True:
    print("Select an operation to perform:")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")

    operation = input("Enter your choice: ")

    if operation == "5":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and end the program

    elif operation in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "1":
            print("The sum is", num1 + num2)

        elif operation == "2":
            print("The difference is", num1 - num2)

        elif operation == "3":
            print("The product is", num1 * num2)

        elif operation == "4":
            if num2 != 0:
                print("The result is", num1 / num2)
            else:
                print("Error: Division by zero!")

    else:
        print("Invalid Entry")
