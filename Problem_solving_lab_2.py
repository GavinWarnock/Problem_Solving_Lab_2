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


# Task 3: Palindrome
# Create a variable to hold a string inputted by a user

string_2 = input("What word would you like to check? ")

# Create a variable to hold the reversed value of the inputted string

reversed_string = ""


# Create a for loop to acquire the reversed version of the string that is inputted

for index in range(len(string_2)-1, -1, -1):
    reversed_string += string_2[index]
print(reversed_string)


# Create an if statement to check if the string and the reversed string match

  
if string_2 == reversed_string:
    print(f"Yes, {string_2} is a palindrome")
else:
    print(f"{string_2} is not a palindrome.")


# Task 4: Compress a string of characters

# Create a variable that holds and inputted string of characters

characters = input("Please type some characters. ")

# Create a new variable to hold the compressed string of characters

compressed_characters = ""

# Create a variable to identify the count of each character and set it equal to 1

count = 1

# Create a for loop that inputs the information we know

for character in range(len(characters)-1):

# Use an if statement to add the characters together and print the result
    if characters[character] == characters[character+1]:
        count = count + 1
    else:
        compressed_characters = compressed_characters + characters[character] + str(count)
        count = 1
compressed_characters = compressed_characters + characters[character+1] + str(count)
print(compressed_characters)