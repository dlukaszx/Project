#predefined drawings, if number of lives changes, this should be changed too

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
