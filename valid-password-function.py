

#This is a function that checks if a password is valid.
# The password must be at least 8 characters long.
# The password must contain at least one uppercase letter and one lowercase
# letter, and one number.
# The sources I used were the Python documentation and ChatGPT to debug my code.
# I asked ChatGPT to debug the logic of my checks of the conditions, similar to how
#   we did in class. I utilized the sources online available to me, similar to the
#   debugging process.
# Within Python documentation, I used the following link:
#   https://docs.python.org/3/library/stdtypes.html#str.isupper



    # The following passwordCheck function will take in an input of a string
    # This string will be the password that will be analyzed to determined if it is valid
def passwordcheck(password):
    #Determine if the password is at least 8 characters long.
    length = len(password)
    if length < 8:
        return False

        #Checks are established and set to False as a default.
    checkupper = False
    checklower = False
    checkdigit = False

        #Now, increment through each character in the password,
        # checking if the character is either uppercased, lowercased, or is a digit
    for char in password:
        if char.isupper():
            checkupper = True
        elif char.islower():
            checklower = True
        elif char.isdigit():
            checkdigit = True

        # ensure that all three conditions are met
        if checkupper and checklower and checkdigit:
            return True

    # otherwise, False must be returned in the event that at least one of these conditions
    # is not satisfied
    return False



