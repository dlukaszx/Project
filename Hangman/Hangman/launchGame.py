import sys
sys.path.append('env/Lib/site-packages')
from english_words import english_words_lower_alpha_set as words
import random
import csv
from drawHangman import draw
from guessLetter import guess
from printResults import printResult


def game():

    #prepare data dor proverbs
    with open('data/proverbs.csv') as f:
        reader = csv.reader(f)
        data = list(reader)

    #list of guessed characters
    guessed = []

    #select game mode
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
            print("Error, type word or proverb")

    #prepare winning/losing condition, number of lives might be balanced in the future
    sentenceC = sentence
    lettersLeft = len(sentenceC.replace(" ",""))
    lives = 6

    printResult(sentence, guessed)

    #main loop with letter guessing, checking results and drawing
    while (lives>0 and lettersLeft>0):   
        print("\nGuess letter")
        lives, guessed = guess(lives, guessed, sentence)
        lettersLeft = printResult(sentence, guessed)
        print("\nLives left: " + (str)(lives))
        draw(lives)

    if lives == 0:
        print("Unlucky, the sentence was: " + sentence)
    else:
        print("Congratulations")

    print("Press enter to exit or type reset to start again")
    state = input()

    #option to play next game
    if state == "reset":
        game()