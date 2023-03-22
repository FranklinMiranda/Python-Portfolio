# Python Practice
# Authorship: Franklin Miranda
# Date: 3/20/2022
# This file practices Python Concepts

message = "Hello World"
example = "World Hello"

#Global Variable Declaration
def myFunc(): 
    global g
    g = "Global Variable"

myFunc()

# Data Types
# Text Type: str
# Numeric Type: int, float
# Sequence Type: list, tuple, range
# Mapping Type: dict
# Set Types: set
# Boolean Type: bool
# None Type: NoneType

#Type function returns type of data
print(type(message))

#Accessing String by Index
print(message[2:5])
print(message[:7])
print(message[3:])
print(message[:-2])
print(message[-3:])


#Modifying Strings
print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("H", "J"))
print(message.split(" "))
print(message + example)

#String Format
age = 24
txt = 'My name is Franklin and I am {} years old!'

print(txt.format(age))

#Escape Characters 
text = "This is a \"escape\" character"
print(text)

#Boolean Functions 
def myFunction(): 
    return True

print(myFunction())

#Lists
thisList = [1,2,3,4,5,6,7,8,9,0]
thatList = [25,26,27,28]

print(len(thisList))
print(type(thisList))

#Accessing List Items by Index
print(thisList[1])
print(thisList[-1])
print(thisList[1:3])
print(thisList[:-1])
print(thisList[-1:])

if 1 in thisList: 
    print(True)

#Changing List Items
thisList[1] = 3
thisList[3:5] = [9,8]


#Adding List Items
thisList.append(24)
thisList.insert(2, 10)
thisList.extend(thatList)


#Removing List Items
thisList.remove(1)
thisList.pop()
del thisList[0]
thatList.clear()

#Looping Through a List 
for n in thisList: 
    print(n)

for i in range(len(thisList)):
    print(thisList[i])

i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1

#Looping using List Comprehension
[print(x) for x in thisList]


#Creating a new list conditionally with List Comprehension
fruits = ['cherry', "apple", 'banana']

newList = [x.upper() for x in fruits if 'a' in x]
print(newList)

#Sorting Lists
thisList.sort()
fruits.sort()
print(thisList)
print(fruits)

thisList.sort(reverse = True)
print(thisList)

#Sort Function can also be passed a custom function to use to sort
def sortingFunc (n):
    return abs(n - 10)

thisList.sort(key = sortingFunc)
print(thisList)

#Reverse Order of List 
thisList.reverse()
print(thisList)

#Copying a List, Lists can be Copied in 2 ways
listCopy1 = thisList.copy()
listCopy2 = list(thisList)

print(listCopy1)
print(listCopy2)

#Joining Lists, Lists can be joined in 3 ways
list3 = listCopy1 + listCopy2

for n in listCopy1:
    list3.append(n)

list3.extend(listCopy1)

print(list3)

#Tuples
tuple1 = (1,2)

print(tuple1)
print(len(tuple1))

#Tuple with one Item 
tuple2 = (1,)
print(tuple2)

#Accessing Tuples is the same as Lists
#Tuples are unchangeable, to change them they must be converted to lists and then changed then converted back to tuples
fruitTuple = ("apples",)
fruitList = list(fruitTuple)
fruitList[0] = 'oranges'
fruitTuple = tuple(fruitList)

print(fruitTuple)

#Deleting Tuples
del fruitTuple


#Unpacking a Tuple * is used to assign the remaining values to a list
fruitsTuple = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruitsTuple

print(green)
print(yellow)
print(red)

#Tuples can be Looped just liked Lists using a for loop, using a for loop with index, or using a while loop
for x in fruitsTuple: 
    print(x)

for i in range(len(fruitsTuple)):
    print(fruitsTuple[i])

i = 0 
while i < len(fruitsTuple):
    print(fruitsTuple[i])
    i = i + 1

#Tuples can be joined using concatenation 
fruitTuple1 = ("apples", "apples", "apples")

fruitTuple12 = fruitsTuple + fruitTuple1
print(fruitTuple12)


#Multiply Tuples to multiply the contents of the tuple 
fruitTuple1 = fruitTuple1 * 2
print(fruitTuple1)

#Counting number of times a value occurs in a tuple 
x = fruitTuple1.count('apples')
print(x)

#Finding Index of a specified value in a tuple
index = fruitTuple1.index('apples')

print(index)


#Sets
thisSet = {1,2,3}
print(thisSet)

#Sets ignore duplicate values
thisSet = {"apples", "apples"}
print(thisSet)

print(len(thisSet))

#Set items are accessed by looping through them with a for loop
thisSet = {"apples", "bananas", "cherries", "oranges"}

for x in thisSet:
    print(x)

#Adding Items to Sets
thisSet.add("pineapples")
print(thisSet)

thisFruitSet = {"mangos", "papayas"}
thisSet.update(thisFruitSet)

print(thisSet)

#Removing Items from a set
thisSet.remove("mangos")
thisSet.discard("papayas")

print(thisSet)

#Clearing or deleting sets
thisSet.clear()

print(thisSet)

del thisSet


#Joining Sets
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,0}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

#Intersection Update updates sets keeping items present only in both sets
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,0}

set1.intersection_update(set2)
print(set1)

set3 = set1.intersection(set2)
print(set3)

#Symmetric Difference Update keeps only items that are not present in both sets
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,0}

set1.symmetric_difference_update(set2)
print(set1)

set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,0}

set3 = set1.symmetric_difference(set2)
print(set3)


#Dictionaries
thisDict = {"fname": "Franklin", "lname": "Miranda"}

print(thisDict)
print(len(thisDict))

#Accessing Dictionaries
print(thisDict['lname'])

#Get method can also be used to retrieve a dictionary key value by key
x = thisDict.get("lname")
print(x)

#Get a list of all dictionary key, updates after changes to the dictionary
y = thisDict.keys()
print(y)

thisDict['age'] = 24

print(y)

#Get a list of all values of a dictionary, updates after changes to the dictionary
z = thisDict.values()
print(z)

thisDict['height'] = 75

print(z)

#Get a list of all key-value pairs in a dictionary as tuples in a list, updates after changes to the dictionary
x = thisDict.items()
print(x)

#Check if key exists in a dictionary
if "lname" in thisDict:
    print(True)

#Changing or Add values in dictionary
thisDict["age"] = 25
print(thisDict["age"])

#Updating the dictionary with a key-value pair
thisDict.update({"birthyear": 1998})
print(thisDict['birthyear'])

#Removing items from a dictionary
thisDict.pop("birthyear")

print(thisDict)

del thisDict['height']

print(thisDict)

thisDict.clear()
print(thisDict)

thisDict = {"fname": "Franklin", "lname": "Miranda"}


#Looping through a Dictionary
for x in thisDict:
    print(x)

for x in thisDict:
    print(thisDict[x])

#Copying a Dictionary 
myDict = thisDict.copy()
print(myDict)

#Nested Dictionary
myFamily = {"person1" : {"fname": "Franklin", "lname": "Miranda"},"person2" : {"fname": "Anna", "lname": "Miranda"} }

#Accessing items in a Nested Dictionary
print(myFamily['person1']['fname'])


#If ELIF ELSE Conditional Statements
a = 10
b = 20
c = 30

if a > b: 
    print("a is greater than b")
elif a > c:
    print("a is greater than c")
elif b > c:
    print("b is greater than c")
else: 
    print("c is greater than a and b")

#Short Hand If Statement 
if b > a: print("b is greater than a")

#Short Hand If Else
print("c is greater than b") if c > b else print("b is greater than c")


#And operator with IF ELIF ELSE statements
if a < b and b < c:
    print("Both conditions are True")

#Or operator with IF ELIF ELSE statements
if a > b or c > a:
    print("At least one of the conditions is True")

#Not operator, used to reverse the result of the conditional statement 
if not a > b:
    print("b is greater than a")

#Nested IF statements
if c > b:
    print("c is greater than b")
    if b > a: 
        print("b is greater than a")
    else:
        print("Neither c is greater than b nor b is greater than a")

#Use a pass statement with a empty If statement to avoid a error 
if b > a:
    pass

#While Loops, can also use Break and Continue Statements to break out of a loop or to skip a loop
i = 0
while i < 6:
    print(i)
    i = i + 1
else: 
    print("i is no longer less than 6")

#For Loops, can also use Break and Continue Statements to break out of a loop or to skip a loop
numbers = [1,2,3,4,5,6,7,8,9]
fruits = ["apples", "bananas"]

for n in numbers:
    print(n)
else:
    print("Loop Finished")

#Nested Loops
for n in numbers:
    for x in fruits:
        print(n, x)

#Pass statement is used to avoid error on empty loop block
for x in [0,1,2]:
    pass

#Functions 
def messagePrinter(message):
    print("Hello " + message)

messagePrinter("World")


#Passing arbitrary arguments to functions 
def familyFunc(*kids):
    print("The youngest child is " + kids[0])

familyFunc('Franklin', 'Anna')

#Default Parameter Values 
def countryPrinter(country = "Norway"):
    print("I am from " + country)

countryPrinter()


#Function return 
def calculator(n):
    return n + 1

print(calculator(4))

#Lambda Functions 
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(1,2,3))

#Using a lambda function inside another function
def cal(n):
    return lambda a : a * n

doubler = cal(2)
print(doubler(10))

#Classes
class MyClass:
    x = 5

#Creating Objects from a Class
obj1 = MyClass()
print(obj1.x)

#Class _init_ function and __str__ function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myFunc(self):
        print("Hello my name is " + self.name)

    def __str__(self):
        return f"{self.name}({self.age})"

person1 = Person("Franklin", 24)


print(person1.name)
print(person1.age)
print(person1)
person1.myFunc()



#Inheritance
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.fname = fname
        self.lname = lname

x = Student("Anna", 'Miranda')
print(x.fname)
print(x.lname)
