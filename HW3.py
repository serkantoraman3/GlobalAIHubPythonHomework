# -*- coding: utf-8 -*-
"""
##### HANGMAN GAME #####

#***Game Rules***     1) You have 5 guesses limit.
                      2) If you repeat wronge letter, your guess limit reduced.
                      3) You must use only lower letter. 

##### GOOD LUCK #####

"""

words = ["course", "grade", "name", "seminar", "labour", "giant", "trade", "adviser", "history", "project", "term", "mark", "board", "fail", "subject", "exam", "rough", "tiny", "vast", "ideal"]
import random

RandomWord = random.choice(words)


name = input("What is your name?: ")
print(f"\n Welcome {name}\n\n WELCOME TO THE HANGMAN GAME! \n\n The Game Begins...\n")

list0 = []


for i in range(0, len(RandomWord)):
    list0.append("_")
print(list0, end = "")
   
list1 = []
indexlist = []

i=0

while i<5:
    
    if len(list1) == len(RandomWord):
        print("Congratulations, You Won!!!")
        break
    
    x = input("\nGuess the letter: ")
    
    if x in list0:
        print("This letter used before. Please guess another letter.")
        
    
    elif i==4:
            print("\n Answer:", RandomWord)
            print(" Game Over...\n Let's Play Again!")
            break
    
    elif x in RandomWord:
        print("True Choice, Go On...\n" )
        list1.append(x)
        indexlist.append(RandomWord.index(x))
        list0[RandomWord.index(x)] = x
        print(" Word: ", list0,"\n","Guesses: ", list1) 
        
    elif x not in RandomWord:
        i=i+1
        print("False Choice, Try Again...")