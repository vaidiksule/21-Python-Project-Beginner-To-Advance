import random
import string
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += specials
    
    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in specials:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd
    

min_length = int(input("Enter the minimum length of password: "))
has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
has_special = input("Include special charcter? (y/n): ").lower() == 'y'

pwd = generate_password(min_length, has_numbers, has_special)
print("The Generated password is: ", pwd)