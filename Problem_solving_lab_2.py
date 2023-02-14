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

string = input("Please type a string. ")

# Create a second variable to hold new string

capitalized_string = ""

# Identify the letters that need to be capitalized: in this case they are H, W, M, N, and I

# Create a for loop to print each letter and identify that there are spaces before each letter that needs to be capitalized

for index in range(0,len(string)):
    if index == 0:
        capitalized_string += string[index].upper()
    elif string[index - 1] == " ":
        capitalized_string += string[index].upper()
    elif string[index] == " ":
        capitalized_string += string[index]
    else:
        capitalized_string += string[index]
print(capitalized_string)

        
    
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

# Use an if statement to add to the count based on the number of characters we have
    if characters[character] == characters[character+1]:
        count = count + 1
    else:
        compressed_characters = compressed_characters + characters[character] + str(count)
        count = 1
compressed_characters = compressed_characters + characters[character+1] + str(count)
print(compressed_characters)