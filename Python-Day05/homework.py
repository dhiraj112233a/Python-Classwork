# =========================
# TUPLE
# =========================


# 1. Create a tuple containing five numbers

numbers = (10, 20, 30, 40, 50)

print(numbers)


# 2. Print the first and last element

numbers = (10, 20, 30, 40, 50)

print("First element =", numbers[0])
print("Last element =", numbers[-1])


# 3. Find the length of a tuple

numbers = (10, 20, 30, 40, 50)

print("Length =", len(numbers))


# 4. Count a particular value

numbers = (10, 20, 10, 30, 10, 40)

count = numbers.count(10)

print("Count =", count)


# 5. Find the index of a value

numbers = (10, 20, 30, 40, 50)

index = numbers.index(30)

print("Index =", index)


# 6. Unpack a tuple into variables

student = ("Dhiraj", 22, "Pune")

name, age, city = student

print("Name =", name)
print("Age =", age)
print("City =", city)


# 7. Create a student information tuple

student = ("Dhiraj", 22, "Pune", "BBA CA")

print(student)



# =========================
# SET
# =========================


# 8. Create a set of five numbers

numbers = {10, 20, 30, 40, 50}

print(numbers)


# 9. Add an element to a set

numbers = {10, 20, 30, 40, 50}

numbers.add(60)

print(numbers)


# 10. Remove an element

numbers = {10, 20, 30, 40, 50}

numbers.remove(30)

print(numbers)


# 11. Remove duplicate values from a list using a set

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print(unique_numbers)


# 12. Find union of two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)

print("Union =", result)


# 13. Find intersection of two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)

print("Intersection =", result)


# 14. Find difference between two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)

print("Difference =", result)



# =========================
# DICTIONARY
# =========================


# 15. Create a student dictionary

student = {
    "name": "Dhiraj",
    "age": 22,
    "city": "Pune"
}

print(student)


# 16. Access values using keys

student = {
    "name": "Dhiraj",
    "age": 22,
    "city": "Pune"
}

print("Name =", student["name"])
print("Age =", student["age"])
print("City =", student["city"])


# 17. Add a new key

student = {
    "name": "Dhiraj",
    "age": 22
}

student["course"] = "BBA CA"

print(student)


# 18. Update an existing value

student = {
    "name": "Dhiraj",
    "age": 22,
    "city": "Pune"
}

student["age"] = 23

print(student)


# 19. Delete a key

student = {
    "name": "Dhiraj",
    "age": 22,
    "city": "Pune"
}

del student["city"]

print(student)


# 20. Use keys(), values() and items()

student = {
    "name": "Dhiraj",
    "age": 22,
    "city": "Pune"
}

print("Keys =", student.keys())
print("Values =", student.values())
print("Items =", student.items())


# 21. Check whether a key exists

student = {
    "name": "Dhiraj",
    "age": 22,
    "city": "Pune"
}

if "name" in student:
    print("Name key exists")

else:
    print("Name key does not exist")


# 22. Create a dictionary containing student marks

marks = {
    "Maths": 85,
    "Python": 92,
    "Java": 78,
    "SQL": 88
}

print(marks)


# 23. Create a list of dictionaries for five students

students = [
    {
        "name": "Dhiraj",
        "age": 22,
        "marks": 85
    },
    {
        "name": "Rahul",
        "age": 21,
        "marks": 90
    },
    {
        "name": "Amit",
        "age": 22,
        "marks": 78
    },
    {
        "name": "Rohit",
        "age": 20,
        "marks": 88
    },
    {
        "name": "Akash",
        "age": 21,
        "marks": 95
    }
]

print(students)