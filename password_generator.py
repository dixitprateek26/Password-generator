import random
import string

def generator(minlen, numbers=True, spec_char=True):                  #minlen variable holds the data what is desired length of the password

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters                                              #characters is the variable that we are using that can hold what type of ascii character we can use while generating the password

    if numbers:
        characters += digits                                          #if numbers are given to be true when calling the function it will add numbers to available characters
    if spec_char:
        characters += special

    pwd = ""                                                          #this will hold our password when we create the password

    meets_critera = False
    has_number = False                                                #To keep a record of data if the password contains a number
    has_special = False                                               #to keep a record of data if the password contains a special charachter

    while not meets_critera or len(pwd) <minlen:
        new_char = random.choice(characters)

        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_critera = True
        if numbers:
            meets_critera = has_number
        if spec_char:
            meets_critera = meets_critera and has_special           # this is just to make sure we have included the special charachters and numbers in the password being generated if the user asks for it in the password
    
    
    return pwd



minlen = int(input("Enter minimum length: "))
has_number = input("Do you want to have numbers(Y/N)?").lower() =='y'             #if the user gives any other input other than y the program will take it as false 
has_special = input("Do you want to have special characters(Y/N)?").lower() =='y'       #if the user gives any other input other than y the program will take it as false 

pwd = generator(minlen, has_number, has_special)

print ("The generated password is:", pwd)