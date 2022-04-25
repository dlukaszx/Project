#draw _ for not guessed letter and print letter if it was guessed properly
#count letters left for win condition

def printResult(guessedWords, guessed):
    lettersLeft = 0
    for c in guessedWords:
        if c in guessed:
            print(c, end="")
        elif c == " ":
            print("   ", end="")
        else:
            print(" _ ", end ="")
            lettersLeft += 1
    return lettersLeft
    