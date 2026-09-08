# 1. Multiline string
print('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are''')


# 2. Text-to-Speech
import pyttsx3
engine = pyttsx3.init()
engine.say("Salam! Amna Azeem")
engine.runAndWait()

# 3. List directory contents
import os
directory = "."
contents = os.listdir(directory)
for item in contents:
    print(item)

# 4. Generates a random joke
import pyjokes
joke = pyjokes.get_joke()
print(joke)

# 5. Checking the data type
a = "67"
print(type(a))

# 6. Sum of 2 variables
a=int (input("Enter num 1 =" ))
b=int (input("Enter num 2 =" ))
print("Sum of a nd b is =", a+b )

# 7. Remainder 
a = 35
b = 5
print("Remainder =", a%b)

# 8. Checking input data type 
a=input("Enter num"  )
print(type(a))

# 9. comparison operation
a= 34
b= 98
c=a<=b
print(c)

# 10. comparison operation 
a=int(input("Enter num 1"))
b=int(input("Enter num 2"))
print("Is a greater than b" , a>b)

# 11. Average of variables 
a=int(input("Enter num 1"))
b=int(input("Enter num 2"))
print("Average of a nd b" , (a+b)/2)

# 12. Square 
a=int(input("Enter num 1"))
b=int(input("Enter num 2"))
print("Square of the sum = " , (a+b)**2)

# Day 2 - Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# -Simple Calculator(1st mini project)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\nChoose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")
operation = input("Enter operation: ")

if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operation!")

