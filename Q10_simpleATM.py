#Create an ATM simulation with initial balance = ₹10,000. 
#The user should be able to perform the following operations:
#1. Check Balance
#2. Deposit Money 
#3. Withdraw Money
#4. Exit
#rules:
#1. The user can only withdraw money if the balance is sufficient.
#minimum balance should be maintained at ₹500 after withdrawal.
#Display transaction messages and updated balance after each transaction 
balance = 10000
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your balance is ₹", balance) 
    elif choice == 2:
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print("₹", deposit_amount, "deposited successfully.")
            print("Updated balance: ₹", balance)
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount > 0:
            if balance - withdraw_amount >= 500:
                balance -= withdraw_amount
                print("₹", withdraw_amount, "withdrawn successfully.")
                print("Updated balance: ₹", balance)
            else:
                print("Insufficient balance. Minimum balance of ₹500 must be maintained after withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")  

