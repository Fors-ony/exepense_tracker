expenses = [
    {"description":"Lunch", "amount":230 },
    {"description":"Shoes", "amount":300}
]
while True:
    print( """
    Expense Tracker
    1. Add Expense
    2. View Expense
    3. Total Expense
    4. Exit
    """)


    choice = input ("Choose an option from (1-4)")

    if choice == "1":
        description = input("Enter expense description ")
        amount = int(input("Enter expense amount "))

        expense = {
            "description": description,
            "amount" : amount
        }
        expenses.append(expense)
        print (f"Expense added : {description} - ${amount}")

    elif choice =="2":
        if not expenses:
            print ("No expense recorded yet")
        else:
            print ("\n  All Expenses ")
            for item in expenses:
                print(f"{item["description"]} : ${item["amount"]}")

    elif choice == "3":
        total = sum(item["amount"] for item in expenses)
        print(f"Total spent: ${total}")      

    elif choice == "4":
        print("Exit")    

    else:
        print("Invalid choice... Please enter a number between 1 and 4")         


    

    
    





















# expenses= [
#     {"description":"Lunch", "amount": 12.50},
#     {"description":"Groceries", "amount": 45.00},

# ]

# print("""
#   EXPENSE TRACKER
# 1. Add Expense
# 2. View Expense
# 3. View Total
# 4. Exit
# """)
# description = input("Enter expense description: ")
# amount=input("Enter expense amount: ")
# print(f"Expense added: {description} - ${amount}")

# expenses.append({"description": description, "amount": float(amount)})
# print("Current Expenses:")
# for expense in expenses:
#     print(f"{expense['description']}: ${expense['amount']:.2f}")    

# print(f"Total Expenses: ${sum(expense['amount'] for expense in expenses):.2f}")

# print("Thank you for using the Expense Tracker!")

