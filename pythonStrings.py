# Python Strings Data Types
# Authorship: Franklin Miranda
# Date: 12/2/2022
# This file lists and explores the different aspects of the Python String Data Type

string = "This is a string"
print(string)

# Multiline Strings can be assigned using 3 quotation marks
a = """This is 
a Multiline
String."""
print(a)

# String Characters can be accessed using indexes because strings are Arrays
print(string[1], string[10])

# Strings can be Looped through using for Loops 
for x in string:
    print(x)

# String Length can be accessed using len()
print(len(string))

# Keyword in can be used to check if characters are present in strings
txt = "The best things in life are free!"
if "free" in txt: 
    print("Yes Free is in the txt!")

# Keyword not in can be used to check if characters are not present in strings
txts = "This sentence does not contain the word dictionary!"
if 'dictionary' in txts: 
    print(True)
else: 
    print(False)