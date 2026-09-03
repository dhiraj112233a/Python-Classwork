import calculator

print(calculator.add(10, 5))
print(calculator.sub(10, 5))
print(calculator.multi(10, 5))
print(calculator.divide(10, 5))


import message
message.welcome("Dhiraj")


import student
student.student_details("Dhiraj", 20, 101)


import calculator2 as calc2
print(calc2.plus(10, 5))
print(calc2.multiply(10, 5))


import operations

print("Square:", operations.square(3))
print("Cube:", operations.cube(5))
print("Even/Odd:", operations.even_or_odd(25))

import os

items = os.listdir()

print("Files and Folders:")
for item in items:
    print(item)


import os

if not os.path.exists("student_data"):
    os.mkdir("student_data")
    print("Folder created successfully!")
else:
    print("Folder already exists!")


import os

filename = input("Enter file or folder name: ")

if os.path.exists(filename):
    print("It exists.")
else:
    print("It does not exist.")



import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

total = num1 + num2

print("Sum =", total)




import calculator3

print("===== New Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", calculator3.add(num1, num2))

elif choice == 2:
    print("Result =", calculator3.subtract(num1, num2))

elif choice == 3:
    print("Result =", calculator3.multiply(num1, num2))

elif choice == 4:
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result =", calculator3.divide(num1, num2))

else:
    print("Invalid choice")



# ============================================================
# 20. CALCULATOR MODULE
# ============================================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculator():
    print("\n===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice: "))

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(a, b))
    elif choice == 2:
        print("Result =", subtract(a, b))
    elif choice == 3:
        print("Result =", multiply(a, b))
    elif choice == 4:
        print("Result =", divide(a, b))
    else:
        print("Invalid choice")


# ============================================================
# 21. STUDENT RESULT MODULE
# ============================================================

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, subjects):
    return total / subjects


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def student_result():
    print("\n===== Student Result =====")

    marks = []

    for i in range(3):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    grade = calculate_grade(percentage)

    print("Total =", total)
    print("Percentage =", percentage)
    print("Grade =", grade)


# ============================================================
# 22. EMPLOYEE MODULE
# ============================================================

def employee_details(name, employee_id, department):
    print("Employee Name:", name)
    print("Employee ID:", employee_id)
    print("Department:", department)


def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus


def employee_system():
    print("\n===== Employee Details =====")

    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    department = input("Enter department: ")

    basic_salary = float(input("Enter basic salary: "))
    bonus = float(input("Enter bonus: "))

    employee_details(name, employee_id, department)

    total_salary = calculate_salary(basic_salary, bonus)

    print("Total Salary:", total_salary)


# ============================================================
# 23. BANK MODULE
# ============================================================

balance = 0


def deposit(amount):
    global balance

    balance += amount
    print("Amount deposited successfully.")


def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")


def check_balance():
    print("Current Balance:", balance)


def bank_system():
    while True:

        print("\n===== Bank Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount: "))
            deposit(amount)

        elif choice == 2:
            amount = float(input("Enter amount: "))
            withdraw(amount)

        elif choice == 3:
            check_balance()

        elif choice == 4:
            break

        else:
            print("Invalid choice")


# ============================================================
# 24. LOGIN MODULE
# ============================================================

users = {}


def register_user(username, password):

    if username in users:
        print("Username already exists.")
    else:
        users[username] = password
        print("Registration successful.")


def login_user(username, password):

    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Invalid username or password.")


def login_system():

    while True:

        print("\n===== Login System =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            username = input("Enter username: ")
            password = input("Enter password: ")

            register_user(username, password)

        elif choice == 2:

            username = input("Enter username: ")
            password = input("Enter password: ")

            login_user(username, password)

        elif choice == 3:
            break

        else:
            print("Invalid choice")


# ============================================================
# 25. SHOPPING CART MODULE
# ============================================================

products = []


def add_product(name, price):

    product = {
        "name": name,
        "price": price
    }

    products.append(product)

    print("Product added successfully.")


def remove_product(name):

    for product in products:

        if product["name"] == name:
            products.remove(product)
            print("Product removed.")
            return

    print("Product not found.")


def calculate_cart_total():

    total = 0

    for product in products:
        total += product["price"]

    return total


def display_cart():

    if len(products) == 0:

        print("Cart is empty.")

    else:

        print("\n===== Shopping Cart =====")

        for product in products:
            print(product["name"], "-", product["price"])

        print("Total =", calculate_cart_total())


def shopping_cart():

    while True:

        print("\n===== Shopping Cart Menu =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Display Cart")
        print("4. Calculate Total")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            name = input("Enter product name: ")
            price = float(input("Enter product price: "))

            add_product(name, price)

        elif choice == 2:

            name = input("Enter product name: ")

            remove_product(name)

        elif choice == 3:

            display_cart()

        elif choice == 4:

            print("Total =", calculate_cart_total())

        elif choice == 5:
            break

        else:
            print("Invalid choice")


# ============================================================
# 26. UTILITY PACKAGE
# ============================================================

def utility_demo():

    print("\n===== Utility Package =====")

    print("Addition:", add(10, 20))
    print("Subtraction:", subtract(20, 10))

    marks = [80, 70, 90]

    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))

    print("Student Total:", total)
    print("Student Percentage:", percentage)

    salary = calculate_salary(30000, 5000)

    print("Employee Salary:", salary)


# ============================================================
# 27. NUMBER UTILITY MODULE
# ============================================================

def is_even(number):
    return number % 2 == 0


def is_prime(number):

    if number < 2:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


def reverse_number(number):

    return int(str(number)[::-1])


def number_utility():

    print("\n===== Number Utility =====")

    number = int(input("Enter a number: "))

    print("Even:", is_even(number))
    print("Prime:", is_prime(number))
    print("Factorial:", factorial(number))
    print("Reverse:", reverse_number(number))


# ============================================================
# 28. STRING UTILITY MODULE
# ============================================================

def reverse_string(text):
    return text[::-1]


def count_vowels(text):

    count = 0

    for char in text.lower():

        if char in "aeiou":
            count += 1

    return count


def is_palindrome(text):

    text = text.lower()

    return text == text[::-1]


def count_words(text):

    return len(text.split())


def string_utility():

    print("\n===== String Utility =====")

    text = input("Enter a string: ")

    print("Reverse:", reverse_string(text))
    print("Vowels:", count_vowels(text))
    print("Palindrome:", is_palindrome(text))
    print("Words:", count_words(text))


# ============================================================
# 29. DATE UTILITY MODULE
# ============================================================

from datetime import datetime


def current_date():

    return datetime.now().strftime("%d-%m-%Y")


def current_time():

    return datetime.now().strftime("%H:%M:%S")


def calculate_age(birth_year):

    current_year = datetime.now().year

    return current_year - birth_year


def days_between_dates(date1, date2):

    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")

    return abs((d2 - d1).days)


def date_utility():

    print("\n===== Date Utility =====")

    print("Current Date:", current_date())
    print("Current Time:", current_time())

    birth_year = int(input("Enter your birth year: "))

    print("Age:", calculate_age(birth_year))

    date1 = input("Enter first date (DD-MM-YYYY): ")
    date2 = input("Enter second date (DD-MM-YYYY): ")

    print(
        "Days between dates:",
        days_between_dates(date1, date2)
    )


# ============================================================
# 30. STUDENT MANAGEMENT SYSTEM
# ============================================================

students = []


def add_student():

    print("\n===== Add Student =====")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []

    for i in range(3):

        mark = float(input("Enter marks: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully.")


def view_students():

    print("\n===== All Students =====")

    if len(students) == 0:

        print("No students found.")
        return

    for student in students:

        print("\n--------------------")
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Marks:", student["marks"])


def search_student():

    print("\n===== Search Student =====")

    roll_no = input("Enter roll number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("Student Found!")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Marks:", student["marks"])

            return

    print("Student not found.")


def calculate_student_result():

    print("\n===== Calculate Result =====")

    roll_no = input("Enter roll number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            marks = student["marks"]

            total = calculate_total(marks)
            percentage = calculate_percentage(
                total,
                len(marks)
            )

            grade = calculate_grade(percentage)

            print("Name:", student["name"])
            print("Total:", total)
            print("Percentage:", percentage)
            print("Grade:", grade)

            return

    print("Student not found.")


def delete_student():

    print("\n===== Delete Student =====")

    roll_no = input("Enter roll number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            students.remove(student)

            print("Student deleted successfully.")

            return

    print("Student not found.")


def student_management():

    while True:

        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Result")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            calculate_student_result()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n\n======================================")
    print("       PYTHON MODULE PRACTICE")
    print("======================================")

    print("20. Calculator")
    print("21. Student Result")
    print("22. Employee")
    print("23. Bank")
    print("24. Login")
    print("25. Shopping Cart")
    print("26. Utility Package")
    print("27. Number Utility")
    print("28. String Utility")
    print("29. Date Utility")
    print("30. Student Management System")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "20":
        calculator()

    elif choice == "21":
        student_result()

    elif choice == "22":
        employee_system()

    elif choice == "23":
        bank_system()

    elif choice == "24":
        login_system()

    elif choice == "25":
        shopping_cart()

    elif choice == "26":
        utility_demo()

    elif choice == "27":
        number_utility()

    elif choice == "28":
        string_utility()

    elif choice == "29":
        date_utility()

    elif choice == "30":
        student_management()

    elif choice == "0":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")