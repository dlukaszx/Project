#This script allows user to play hangman
#You can choose if guessed sentence must be a single word or proverb
#You have 6 lives to guess the password, good luck
#Passwords contain only small letters

import sys
sys.path.append('env/Lib/site-packages')
from english_words import english_words_lower_alpha_set as words
import random
import csv

#import words
with open('data/proverbs.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

#list of guessed characters
guessed = []

#function to check if letter was previously picked and
# if it is in the password

def guess(lives):
    c = input()
    if len(c)==1 and c.isalpha():
        c = c.lower()
    else:
        print("wrong input, live lost")
        return lives - 1
    if c in guessed:
        print("You have already guessed that letter, chance lost")
        return lives - 1
    elif c in sentence:
        print(c.upper() + " in guessed sentence")
        guessed.append(c)
        return lives
    else:
        print("not this time")
        return lives - 1

def printResult(guessedWords):
    lettersLeft = 0
    for c in guessedWords:
        if c in guessed:
            print(c, end="")
        elif c == " ":
            print("   ",end="")
        else:
            print(" _ ", end ="")
            lettersLeft += 1
    return lettersLeft
    print("Letters left " + (str)(lettersLeft))

def draw(lives):
    if lives == 0:
        print("   ----")
        print("   |  |")
        print("   o  |")
        print("  /|\ |")
        print("  / \ |")
        print("  ____|")
    if lives == 1:
        print("   ----")
        print("   |  |")
        print("   o  |")
        print("  /|  |")
        print("      |")
        print("  ____|")
    if lives == 2:
        print("   ----")
        print("   |  |")
        print("      |")
        print("      |")
        print("      |")
        print("  ____|")
    if lives == 3:
        print("     --")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("  ____|")
    if lives == 4:
        print("       ")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("  ____|")
    if lives == 5:
        print("       ")
        print("       ")
        print("       ")
        print("       ")
        print("       ")
        print("  ____ ")

print("Choose mode: word or proverb")
while(True):
    choice = input()

    if choice =="word":
        sentence = random.choice(tuple(words))
        break
    
    elif choice == "proverb":
        prov = random.choice(data)
        sentence = prov[0].lower()
        break
    else:
        print("error, write word or proverb")

sentenceC = sentence
lettersLeft=len(sentenceC.replace(" ",""))
lives = 6
printResult(sentence)

while (lives>0 and lettersLeft>0):
    print("")
    print("guess letter")
    lives = guess(lives)
    lettersLeft = printResult(sentence)
    print("")
    print("lives left: " + (str)(lives))
    draw(lives)
if lives == 0:
    print("Unlucky, the sentence was: " + sentence)
else:
    print("congratulations")

print("press enter to exit")
input()
exit()