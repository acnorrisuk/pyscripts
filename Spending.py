#spending
#type conversion and integers

print(
    """

                        Monthly Spending

This is a program to total your monthly spending so you can keep track
of what you have spent.

"""

)

petrol = float(input("Petrol money: £"))
food = float(input("Food Shopping: £"))
disposable = float(input("Spending money: £"))
mortgage = float(input("Mortgage: £"))
utility = float(input("Utility Bills: £"))


total = petrol + food + disposable + mortgage + utility

print("\nTotal: £",total)

print("\nYearly Spend: £" ,total *12)
input("\n\nPress enter to exit")
