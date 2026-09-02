#1.function to print "Hello Python"
def fun1():
    print("Hello Python")
fun1()

#2.function that accepts a name.
def fun2(name):
    print("Hello", name ,"I am Jarvis")
fun2("Dhiraj")

#3.function to add two numbers.
def fun3(A,B):
    return A+B
sum = fun3(45,45)
print("The Sum Of Two Numbers Is :", sum)

#4.functions for addition, subtraction, multiplication and division.
def add(A,B):
    return A+B
def sub(A,B):
    return A-B
def multiply(A,B):
    return A*B
def divide(A,B):
    return A/B
print("Addition Of Two Numbers Is :", add(45,45))
print("subtraction Of Two Numbers Is :", sub(45,45))
print("multiplication Of Two Numbers Is :", multiply(45,45))
print("division Of Two Numbers Is :", divide(45,45))


#5.function to check even/odd.
def check(num):
    if num%2==0:
        print(num,"is Even Number")
    else:
        print(num,"is Odd Number")
check(7325) 


#6.function to check positive/negative/zero.
def fun4(num):
    if num>0:
        print(num,"is Positive Number")
    elif num<0:
        print(num,"is Negative Number")
    else:
        print(num,"is Zero")

fun4(45)

#7.function to calculate factorial.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial Of 5 Is :", factorial(5))

#8. function to find the largest of two numbers.
def find(x,y):
    if x>y:
        return x
    else:
        return y

print("Largest Number Is :", find(18,45))

#9.function to calculate student percentage.
def percentage(marks,total_marks):
    return (marks/total_marks)*100

marks = 435
total_marks = 500

print("Student's Percentage Is :", percentage(marks, total_marks))


#10. function that accepts a list and returns its sum.
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print("Sum Of List Is :", sum_list([10,20,30,40,50]))
