# Python Data Types
# Authorship: Franklin Miranda
# Date: 12/3/2022
# This file lists and explores the Python Lists Data Type

# Lists are created using square brackets []
myList = ["Apples", "Bananas", "Cherries"]
print(myList)
print(myList[0])
print(myList[-1])
print(len(myList))

boolList = [True, False, True]
print(boolList)

multiDataList = ["Apples", 1, True]
print(multiDataList)

# List Items can be accessed using Index
print(myList[0])

# Negative Indexing can be used to access a list from the end backwards
print(myList[-1])

# A range of indexes on a list can be accessed using a start and end range for indexes
print(myList[1:])