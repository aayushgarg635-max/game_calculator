
print("===== WELCOME TO THE MINI ATM =====")

inputpin = int(input("Enter your PIN: "))
pin = 2348

if inputpin == pin:
    print("Correct PIN, Access Granted!")

    Balance = 7000

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your Current Balance:", Balance)

        elif choice == 2:
            print("Deposit Selected")
            amount1 = int(input("Enter the amount: "))

            if amount1 > 0:
                Balance += amount1
                print("Money Deposited Successfully!")
                print("Updated Balance:", Balance)
            else:
                print("Invalid Amount!")

        elif choice == 3:
            print("Withdrawal Selected")
            amount2 = int(input("Enter the amount: "))

            if amount2 > 0 and amount2 <= Balance:
                Balance -= amount2
                print("Withdrawal Successful!")
                print("Remaining Balance:", Balance)
            else:
                print("Invalid Amount or Insufficient Balance!")

        elif choice == 4:
            print("Thank You for using Mini ATM!")
            break

        else:
            print("Invalid Choice! Try Again.")

else:
    print("Wrong PIN! Access Denied.")
