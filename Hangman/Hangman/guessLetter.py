#guess letter, if it is not a letter or it was previously used, lose live
#letter will change to lower if it was typed as upper

def guess(lives, guessed, sentence):
    c = input()
    if len(c)==1 and c.isalpha():
        c = c.lower()
    else:
        print("wrong input, live lost")
        return (lives - 1, guessed)
    if c in guessed:
        print("You have already guessed that letter, chance lost")
        return (lives - 1, guessed)
    elif c in sentence:
        print(c.upper() + " in guessed sentence")
        guessed.append(c)
        return (lives, guessed)
    else:
        print("not this time")
        return (lives - 1, guessed)