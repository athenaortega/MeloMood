#Day 03 - Exercises on Python strings and lists


## These exercises are designed to be finished in class.
## Once you are happy with your code, push it to Github
## and your submission will be auto-graded. If your
## submission does get the full grade, you have the option
## of resubmitting it (unlimited attempts till the end of
## the day).
##
## Note that you need to get outputs exactly as specified
## as the autograder looks for an exact match.
##
## You have as many attempts to do this as you would like,
## and you can ask for help from us, or from your friends.
## You do not need to acknowledge help received for this
## particular activity; however, please make sure that you
## understand the code that you end up writing.


#
#A string called "text" is defined in the code below. Your task is to loop through the string,
#and produce an output where each word is printed separately in a new line, with a '-'
#(without the quotes) printed after each line. The '-' character should be in its own line.
#So, your output is going to look like this:
#
#Pythons
#-
#are
#-
#some
#-
#of
#-
#the
#-
#largest
#-
#snakes
#-
#in
#-
#the
#-
#world
#-

text = "Pythons are some of the largest snakes in the world"

## Write your code here. Remember, there may be more than one correct way of writing your code
myList = text.split(" ")
for item in myList:
    print(item)
    print('-')



#Once you are done with the task above, print each element of the list below, with each element turned
#into upper-case (capitalized).
#Hint: You can use the .upper() string method to achieve this.
#Your output should look like the following:
#
#PYTHONS
#ARE
#NONVENOMOUS

## Write your code here
wordList =["Pythons", "are", "nonvenomous"]
for item in wordList:
    print(item.upper())

