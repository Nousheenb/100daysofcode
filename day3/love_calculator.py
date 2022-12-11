'''
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.
'''



print("Welcome Love calculator.")

name1 = input("What's your name? ").lower()
name2 = input("What's their name? ").lower()
name = name1 + name2

true = 0
love = 0

true += name.count('t')
true += name.count('r')
true += name.count('u')
true += name.count('e')

love += name.count('l')
love += name.count('o')
love += name.count('v')
love += name.count('e')

love_score = str(true) + str(love)



if love_score < 10 or love_score >90 :
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
