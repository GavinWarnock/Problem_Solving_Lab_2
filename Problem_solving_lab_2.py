# Task 1: Reverse a String
# Start off with a variable of string

word = "Hello"

# Create second variable to hold reversed string and use the len() function to identify the final index

reversed_word = ""

# Create a for loop that breaks down the word backwards

for index in range(len(word)-1, -1 ,-1):
    print(word[index])
# Result: o , l, l, e, H

# Put it all together

for index in range(len(word)-1, -1, -1):
    reversed_word += word[index]
print(reversed_word)
# Result: olleH

# Task 2: Capitalize a letter

# Create a variable to hold a String

string = "hello world"

# Identify the letters that need to be capitalized: in this case they are H and W
# Research how to alter a lower case letter to an upper case letter in Python
# There are multiple functions you can use to capitalize letters such as the title() function or the capitalize() function

# Using the title() function you can raise the case of the first letter in words of the string

print(string.title())


print(string.capitalize())
  
