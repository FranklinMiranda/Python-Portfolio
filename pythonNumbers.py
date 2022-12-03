# Python Numbers
# Authorship: Franklin Miranda
# Date: 12/2/2022
# This file lists and explores the different Python Number Data Types

x = 1 # Integer Data Number Type
y = 1.5 # Float Data Number Type
z = 1j # Complex Data Number Type

print(x,y,z)

# Float Data Number Type can use e to indicate power of 10
y = 1e2
print(y)

# Type Conversion can be used with int(), float(), and complex() to convert to different Number Data Types
a = int(y)
print(a)


# Python does not have a Random Function but has a built-in module that can be imported and used with randrange() method 
import random

print(random.randrange(1,10))