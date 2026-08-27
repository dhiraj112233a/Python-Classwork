# 1. Take a name from the user and print it in uppercase

name = input("Enter your name: ")

print(name.upper())


# 2. Take a name from the user and print it in lowercase

name = input("Enter your name: ")

print(name.lower())


# 3. Take a full name and print it in title case

name = input("Enter your full name: ")

print(name.title())


# 4. Find the length of a string entered by the user

text = input("Enter a string: ")

print("Length =", len(text))


# 5. Print the first character of a string

text = input("Enter a string: ")

print("First character =", text[0])


# 6. Print the last character of a string

text = input("Enter a string: ")

print("Last character =", text[-1])


# 7. Print the first three characters of a string using slicing

text = input("Enter a string: ")

print(text[:3])


# 8. Reverse a string using slicing

text = input("Enter a string: ")

print(text[::-1])


# 9. Count how many times the letter 'a' appears in a string

text = input("Enter a string: ")

count = text.count("a")

print("Number of a =", count)


# 10. Replace the word 'Python' with 'Java' in a sentence

sentence = input("Enter a sentence: ")

sentence = sentence.replace("Python", "Java")

print(sentence)


# 11. Remove extra spaces from the beginning and end of a string

text = input("Enter a string: ")

text = text.strip()

print(text)


# 12. Check whether a given word exists inside a sentence

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence:
    print("Word exists")

else:
    print("Word does not exist")


# 13. Take first name and last name and create a full name

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + last_name

print("Full name =", full_name)


# 14. Use an f-string to display a student's name, age and city

name = input("Enter student name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print(f"My name is {name}, I am {age} years old, and I live in {city}.")


# 15. Check whether a string is empty or not

text = input("Enter a string: ")

if text == "":
    print("String is empty")

else:
    print("String is not empty")


# 16. Check whether a string starts with a specific letter

text = input("Enter a string: ")
letter = input("Enter a letter: ")

if text.startswith(letter):
    print("String starts with", letter)

else:
    print("String does not start with", letter)


# 17. Check whether a string ends with '.com'

email = input("Enter an email address: ")

if email.endswith(".com"):
    print("String ends with .com")

else:
    print("String does not end with .com")


# 18. Count the number of vowels in a string

text = input("Enter a string: ")

count = 0

for i in text:
    if i in "aeiouAEIOU":
        count = count + 1

print("Number of vowels =", count)


# 19. Count the number of words in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words =", len(words))


# 20. Take an email address and display the username part before @

email = input("Enter your email: ")

username = email.split("@")[0]

print("Username =", username)