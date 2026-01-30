print("\n============================= Calculator ==============================")

loop = True
while (loop == True):
    print("\nEnter operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division [Returns integer value of quotient]")
    print("6. Modulus [Returns remainder of division]")
    print("7. Exponentiation")
    choice = input("\nEnter your choice number: ")
    print("=========================================================================\n")
    if choice == '1':
        print("You chose addition")
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        print("Sum Of The Given Numbers:",num1+num2)
    elif choice == '2':
        print("You chose subtraction")
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        print("Difference Of The Given Numbers:",num1-num2)
    elif choice == '3':
        print("You chose multiplication")
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        print("Product Of The Given Numbers:",num1*num2)
    elif choice == '4':
        print("You chose division")
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        print("Quotient Of The Given Numbers:",num1/num2)
    elif choice == '5':
        print("You chose floor division")
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        print("Floor Quotient Of The Given Numbers:",num1//num2)
    elif choice == '6':
        print("You chose modulus")
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        print("Remainder Of The Given Numbers:",num1%num2)
    elif choice == '7':
        print("You chose exponentiation")
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        print("Exponentiation Of The Given Numbers:",num1**num2)
    else:
        print("Enter a valid number")
    print("\n=========================================================================\n")

    restart = True
    while (restart == True):
        Continue = input("Want To Continue? (Y/N): ")
        if Continue == "Y":
            print("Restarting...")
            restart = False
            loop = True
        elif Continue == "N":
            print("Terminating...")
            print("=========================================================================\n")
            restart = False
            loop = False
        else:
            print("Enter a valid answer")
            restart = True




