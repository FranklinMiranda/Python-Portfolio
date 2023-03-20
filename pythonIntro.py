# Python Introduction
# Authorship: Franklin Miranda
# Date: 12/2/2022
# This file introduces basic python concepts

msg = "Hello World"

print(msg)

if 5 > 2:
    print("Five is greater than two")

x = 10
y = 20

if x > y:
    print("X is greater than Y")
else:
    print("Y is greater than X")


#This is a python comment

# Variables do  not have a declaration keyword in python
z = 30

# Casting can be used to declare a specific datatype with variable declarations 
a = str(3)
b = int(5)
c = float(10)

print(a,b,c)

# Type() function can be used to get the type of the variable 
print(type(a))

A = str(40)
print(A)

# Variable Naming Rules 
var = 1
_var = 12
var1 = 123
Var_1 = 1234

print(var, _var, var1, Var_1)

# Camel Case, Pascal Case, and Snake case can be used to make names more readable
camelCase = "Camel Case"
PascalCase = "Pascal Case"
snake_case = "Snake Case"

print(camelCase, PascalCase, snake_case)

# One Line multivariable declaration 
e, f, g = 1, 2, 3
print(e,f,g)

# One value assigned to multiple variables
x = y = z = "Red"
print(x,y,z)

# Unpacking a collection of values from a list
fruits = ["apples", "bananas", "cherries"]
x, y, z = fruits
print(fruits)
print(x,y,z)

print(x + z)

# Global Variables, unlike variables declared inside a function, can be accessed globally


def myFunc():
    global x
    x = 'globalvariable'

myFunc()

print(x)
# Variables declared inside function can only be accessed locally

