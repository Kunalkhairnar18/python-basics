#  If-Else (Decision Making)
# Conditional statements allow program to take actions based on conditions
# Comparison operators: <, >, <=, >=, ==, !=
                
a=int(input("enter num: "))
print(a>14)
print(a>=14)
print(a<=14)
print(a!=14)
print(a==14)

#if_condition
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")

#if_else
age=int(input("enter the age:"))

if(age>=18):
    print("you can drive")
else:
    print("you cannot drive")

# elif_condition
num=int(input("enter the number: "))
if(num<0):
    print("Given number is negative")

elif(num>0):
    print("Given number is positive")

else:
    print("Given number is zero")

# nested_if_else_elif
number=int(input("enter the number:"))
if(number<0):
    print("number is negative")

elif(number>0):
  
    if(number<=10):
        print("number is between 0-10")
   
    elif(number>10 and number<=20):
        print("number is between 11-20")
   
    else:
        print("number is greater than 20")
        
else:
    print("number is zero")
