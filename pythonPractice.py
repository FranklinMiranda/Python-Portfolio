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

#Coping a List, Lists can be Copied in 2 ways
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

