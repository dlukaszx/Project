import sys
sys.path.append('env/Lib/site-packages')
from english_words import english_words_lower_alpha_set as words
import random
import csv


with open('data/proverbs.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

guessed = []
def guess(c, lives):
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
choice = input()

if choice =="word":
    sentence = random.choice(tuple(words))
    
elif choice == "proverb":
    prov = random.choice(data)
    sentence = prov[0].lower()
else:
    print("error")

sentenceC = sentence
lettersLeft=len(sentenceC.replace(" ",""))
lives = 6
printResult(sentence)

while (lives>0 and lettersLeft>0):
    print("")
    print("guess letter")
    c = input().lower()
    lives = guess(c, lives)
    lettersLeft = printResult(sentence)
    print("")
    print("lives left: " + (str)(lives))
    draw(lives)
if lives == 0:
    print("Unlucky, the sentence was: " + sentence)
else:
    print("congratulations")