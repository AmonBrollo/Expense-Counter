import datetime
from unicodedata import category

def main():
    # Get the Month and Year of the expenses
    now = datetime.datetime.now()
    month = now.strftime("%B")
    year = now.year
    print(year, month)

    one_more = "yes"
    while one_more != "no":
        category, expense_value = get_expense()
        # asks if the user wants to add one more expense.
        one_more = input("Would you like to add one more expense? (yes/no) ")

    print(organizer(category, expense_value))

def get_expense():
    # asks for the category of the expense.
    category = input("What is the category of the expense? ")
    # asks for the value of the expense.
    expense_value = float(input("What is the value of the expense? "))
    return category, expense_value

def organizer(cat, val):
    """
    Organizes the expense information in lists of categories.
    """
    expenses = {
        cat: val
    }
    return expenses

def confirmation():
    # confirms the info with the user
    pass

if __name__ == "__main__":
    main()
