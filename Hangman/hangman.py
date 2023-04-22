import random
import time
def WannaPlay():
    Ans=input("\nDo you Want to play Hangman (Y/N): ")
    if Ans=="Y" or Ans=="y":
        intro= "HI! {} Here we goo!!! "#EDIT  
        print(intro.format(name))
    elif Ans=="N" or Ans=="n":
        print("(: THANK YOU :)")
        exit()
    else:
        print(")X Invalid Choice X(")
        WannaPlay()
def Difficulty():
    print("\n\t\tChoose Difficulty Level\n")
    print("Press E : Easy")
    print("Press M : Medium")
    print("Press H : Hard")
    diff=input("Enter your Choice: ")
    if(diff=="E" or diff=="e"):
        words=["plant","tree","air","box","book"]
        return words
    elif(diff=="M" or diff=="m"):
        words={"Tree":["It provides Oxygen to us Humans","Fun Fact"]}
    elif(diff=="H" or diff=="h"):
        words={"Tree":["It provides Oxygen to us Humans","Fun Fact"]}
    else:
        print("!! WRONG CHOICE !!")
        print("CHOOSE AGAIN !!")
        Difficulty()
def Rules():
    print(""" RULES OF HANGMAN
    
    
                                                            """)
def wordsrandom():
    rword=random.choice(stack)
    return rword
correct=[]


def CPU():
    print("\n\t\tHANGMAN\n")
    Main_Body()

    
    
    re=input("Do you Want to Play again (Y/N):")
    if re=='Y' or re=='y':
        print("\nSure\n")
        CPU()
    elif re=='N' or re=='n':
        print("Thank you for playing\nI hope you Enjoyed the Game ")
    else:
        print("XXX  Wrong Choice XXX")


def Main_Body():
    word=wordsrandom()
    print("\n\t\tHANGMAN\n")
    print("\n\t\tGUESS THE FOLLOWING WORDS\n")
    HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
# Set up the game
    guesses = []
    wrong=[]
    maxfails = 7
    fails = 0

# Main loop
    while fails < maxfails:

    # Display the current state of the word
        display = ""
        for letter in word:
            if letter in guesses:
                display += letter
            else:
                display += "_"
        if "_" not in display:
            print("Congratulations! You guessed the word!")
            points+=10
            Main_Body()
        print(display)

    # Get a guess from the user
        guess = input("Guess a letter: ").lower()

    # Check if the guess is valid
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        elif guess in guesses or guess in wrong:
            print("You already guessed that letter.")
            continue
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter.")
            continue

    # Add the guess to the list of guesses
    #guesses.append(guess)

    # Check if the guess is in the word
        if guess in word:
            print("Correct!")
            guesses.append(guess)
            print(HANGMAN_PICS[fails])
        else:
            print("OOPS! Wrong Letter")
            wrong.append(guess)
            fails += 1
            print(HANGMAN_PICS[fails])
        
    if fails == maxfails:
        print("Sorry, you ran out of guesses. The word was",word)

#User-Interface
print("\t\tHANGMAN")
name=input("Enter Your Full Name: ")
WannaPlay()
#time.sleep(5)
Rules()
stack=Difficulty()
#time.sleep(5)
#Hangman()
CPU()

