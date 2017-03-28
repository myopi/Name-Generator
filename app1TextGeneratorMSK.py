'''
This application was created as part of Udemy course for Python.
The purpose of application is to create random 3 letter names that are dependent on user input for the types of letters used.
The application was further expanded to:
(1) include validation for input
(2) include ability for user to select how many names should be generated
(3) provide feedback to user about the selections of letters made
'''

import random

## Declaration of functions used in the application
# Two functions to ask user for input for both (letter, number) cases
def askForInputLetter():
    return input("Pick a letter. 'v' for vowels, 'c' for consonants, 'i' for any letter: ")

def askForInputNumber():
    return input("How many names would you like to get? ")

# Two functions to validate user input for both (letter, number) cases. These make sure that user input is valid for application to function as expected.
def validateInputLetter(userInput):
        if userInput.isalpha() == False:
            print("That's not even a letter.")
            return validateInputLetter(askForInputLetter())
        elif len(userInput) > 1:
            print("That's more than one letter!")
            return validateInputLetter(askForInputLetter())
        else:
            letterConfirmation(userInput)
            return userInput

def validateInputNumber(userInput):
    if userInput.isnumeric() == False:
        print("That doesn't look like a number.")
        return validateInputNumber(askForInputNumber())
    elif len(userInput) > 2:
        print("That's a lot! Perhaps a smaller number?")
        return validateInputNumber(askForInputNumber())
    else:
        return int(userInput)

# Function to provide feedback to user about the made selection since selection is based on one letter codes.
def letterConfirmation(letter):
    if letter == 'c':
        print("You picked a consonant!")
    elif letter == 'v':
        print("You picked a vowel!")
    elif letter == "i":
        print("You picked any letter!")
    else:
        print("You picked '%s'" % letter)

# Function to produce a random letters given user selections (vowels, consonants, any letter or user specific letter)
def randomiseLetter(typeofletter):
    if typeofletter == 'v':
        return random.choice(vowels)
    elif typeofletter == 'c':
        return random.choice(consonants)
    elif typeofletter == 'i':
        return random.choice(all_letters)
    else:
        return typeofletter

### Main body of application
# First assignments are used to gather user input for both (letters and number)
Letter1 = validateInputLetter(askForInputLetter())
Letter2 = validateInputLetter(askForInputLetter())
Letter3 = validateInputLetter(askForInputLetter())
NumberOfNames = validateInputNumber(askForInputNumber())

# Declaration of some variables that are used in name generation
LetterCombination = Letter1 + Letter2 + Letter3
vowels = 'aeiouy'
consonants = 'bcdfghjklmnqprstvwxz'
all_letters = vowels + consonants

# Function to generate the names according to user inputs for letter selection and the number of names desired.
count = 0
name = ''
while count < NumberOfNames:
    for i in range(3):
        name += randomiseLetter(LetterCombination[i])
    print(name)
    name = ''
    count += 1
