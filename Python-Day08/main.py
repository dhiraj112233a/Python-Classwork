file = open("data.txt", "w")
file.write("Hello Python\n")
file.close()

# ====================================================================

file = open("student.txt", "w")
file.write("Name: Dhiraj\n")
file.write("Age: 21\n")
file.write("City: Pune\n")
file.close()

# ====================================================================

file = open("data.txt", "r")
data = file.read()
print(data)
file.close()

#=====================================================================

file = open("Message.txt", "w")
file.write("Hey Guys\n")
file.write("Hello Guys\n")
file.write("Hi Guys\n")
file.write("What's up? Guys\n")
file.write("Ki Haal Hai? Guys\n")
file.close()

#=====================================================================

file = open("Message.txt", "r")
data = file.readlines()
for line in data:
    print(line)

#=====================================================================

with open("data.txt", "r") as file:
    count = len(file.readlines())

print("Number of lines:", count)

#=====================================================================

with open("data.txt", "r") as file:
    text = file.read()

words = text.split()

print("Number of words:", len(words))

#=====================================================================

with open("data.txt", "r") as file:
    text = file.read()

characters = len(text)

print("Number of characters:", characters)

#=====================================================================

word = input("Enter word to search: ")

with open("data.txt", "r") as file:
    text = file.read()

if word in text:
    print("Word exists in the file.")
else:
    print("Word does not exist in the file.")

#=====================================================================

with open("data.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line, end="")

#=====================================================================

file = open("students.txt", "w")
file.write("Rohit\n")
file.write("Virat\n")
file.write("Shubman\n")
file.write("Suryakumar\n")
file.write("Rishabh\n")
file.close()

#=====================================================================

file = open("students.txt", "a")
file.write("Hardik\n")
file.write("Jasprit\n")
file.close()

#====================================================================

file = open("numbers.txt", "w")
file.write("1\n")
file.write("2\n")
file.write("3\n")
file.write("4\n")
file.write("5\n")
file.write("6\n")
file.write("7\n")
file.write("8\n")
file.write("9\n")
file.write("10\n")
file.close()

#=====================================================================

file = open("numbers.txt", "a")
file.write("11\n")
file.write("12\n")
file.write("13\n")
file.write("14\n")
file.write("15\n")
file.write("16\n")
file.write("17\n")
file.write("18\n")
file.write("19\n")
file.write("20\n")
file.write("21\n")

file.close()

#=====================================================================

file = open("cities.txt", "w")
file.write("New York\n")
file.write("London\n")
file.write("Tokyo\n")
file.write("Paris\n")
file.write("Sydney\n")
file.close()
file = open("cities.txt", "a")
file.write("Perth\n")
file.write("Melbourne\n")
file.write("Lord Howe\n")
file.close()

#=====================================================================

file = open("StudentsData.txt", "w")
file.write(input("Enter Your Name: ") + "\n")
file.write(input("Enter Your Marks: ") + "\n")
file.close()

#=====================================================================

file = open("employee.txt", "w")
file.write(input("Enter Employee Name: ") + "\n")
file.write(input("Enter Employee Name: ") + "\n")
file.write(input("Enter Employee Name: ") + "\n")
file.write(input("Enter Employee Name: ") + "\n")
file.write(input("Enter Employee Name: ") + "\n")
file.close()

#=====================================================================

file = open("Numbersinput.txt", "w")
file.write(input("Enter Number 1: ") + "\n")
file.write(input("Enter Number 2: ") + "\n")
file.write(input("Enter Number 3: ") + "\n")
file.write(input("Enter Number 4: ") + "\n")
file.write(input("Enter Number 5: ") + "\n")
file.close()


#=====================================================================

                        #OOPs Questions

#=====================================================================

class Student:
    name = "Dhiraj"
    age = 21
    course = "BBA CA"


student1 = Student()

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)


#=====================================================================

class Student1:
    player_name = "Rohit"
    jersey_number = 45
    team = "Mumbai Indians"
    
