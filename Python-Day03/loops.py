# 1. Print numbers from 1 to 10 using a for loop

for i in range(1, 11):
    print(i)


# 2. Print numbers from 1 to 100

for i in range(1, 101):
    print(i)


# 3. Print all even numbers between 1 and 50

for i in range(2, 51, 2):
    print(i)


# 4. Print all odd numbers between 1 and 50

for i in range(1, 51, 2):
    print(i)


# 5. Print numbers from 10 to 1 in reverse order

for i in range(10, 0, -1):
    print(i)


# 6. Print the multiplication table of a number entered by the user

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 7. Find the sum of numbers from 1 to 100

sum = 0

for i in range(1, 101):
    sum = sum + i

print("Sum =", sum)


# 8. Find the sum of all even numbers from 1 to 100

sum = 0

for i in range(2, 101, 2):
    sum = sum + i

print("Sum of even numbers =", sum)


# 9. Find the factorial of a number using a loop

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# 10. Count how many numbers are present between 1 and a user-entered number

num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    count = count + 1

print("Count =", count)


# 11. Print numbers divisible by 5 between 1 and 100

for i in range(1, 101):
    if i % 5 == 0:
        print(i)


# 12. Use a while loop to print numbers from 1 to 20

i = 1

while i <= 20:
    print(i)
    i = i + 1


# 13. Use a while loop to print even numbers from 2 to 20

i = 2

while i <= 20:
    print(i)
    i = i + 2


# 14. Keep printing numbers and stop when the number becomes 5 using break

for i in range(1, 11):
    print(i)

    if i == 5:
        break


# 15. Print numbers from 1 to 10 but skip 5 using continue

for i in range(1, 11):
    if i == 5:
        continue

    print(i)


# 16. Find the sum of the first N natural numbers

n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)


# 17. Calculate the power of a number without using ** operator

base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result = result * base

print("Power =", result)


# 18. Print the first 10 multiples of 3

for i in range(1, 11):
    print(3 * i)


# 19. Count how many numbers between 1 and 100 are divisible by both 2 and 5

count = 0

for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        count = count + 1

print("Count =", count)


