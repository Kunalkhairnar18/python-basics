#if-Else (Decision Making in Python)
# Conditional statements allow a program to take actions based on conditions
# Comparison operators: <, >, <=, >=, ==, !=

# Boolean comparison examples
a = int(input("Enter number: "))
print(a > 14)
print(a >= 14)
print(a <= 14)
print(a != 14)
print(a == 14)

#if_condition
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")

# If-Else condition
age = int(input("Enter the age: "))
if age >= 18:
    print("You can drive")
  
else:
    print("You cannot drive")

# Elif condition
num = int(input("Enter the number: "))
if num < 0:
    print("Given number is negative")
  
elif num > 0:
    print("Given number is positive")
  
else:
    print("Given number is zero")

# Nested if-elif-else
number = int(input("Enter the number: "))
if number < 0:
    print("Number is negative")
  
elif number > 0:
  
    if number <= 10:
        print("Number is between 0-10")
    elif number <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
      
else:
    print("Number is zero")
