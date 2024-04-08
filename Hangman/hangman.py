#Importing Libraries
import random
import time
import datetime
#Function Defination
def WannaPlay():
    #Asking User to Play the Hangman
    try:
        Ans= input("\nDo you Want to play Hangman (y/n): ")
        if Ans.lower() not in ('y', 'n'):
            raise ValueError("Invalid input! Please enter 'y' or 'n'.")
    except ValueError as e:
        WannaPlay()
#Action based on user input
    if Ans.upper() == 'Y':
        intro= "Hello! {} 😊\n(: I hope you will enjoy this Game 😁:)"  
        print(intro.format(name))
    elif Ans.upper()=='N':
        print("(: THANK YOU :)")
        exit()
#user can choose the level of difficulty
def Difficulty():
    print("\n\t\tChoose Difficulty Level\n")
    print("Press E : Easy")
    print("Press M : Medium")
    print("Press H : Hard")
    diff=input("Enter your Choice: ")
    if(diff=="E" or diff=="e"):
        words = ['apple', 'baby', 'beach', 'bird', 'book', 'box', 'bus', 'cake', 'cat', 'chair', 'chicken', 'cloud', 'coin', 'computer', 'cup', 'dog', 'door', 'duck', 'egg', 'eye', 'fish', 'flower', 'food', 'frog', 'game', 'girl', 'guitar', 'hat', 'house', 'jacket', 'key', 'kite', 'lemon', 'light', 'lion', 'lock', 'love', 'map', 'money', 'moon', 'mouse', 'music', 'nail', 'nose', 'orange', 'paper', 'pen', 'pencil', 'phone', 'picture', 'pig', 'plane', 'plant', 'rabbit', 'radio', 'rainbow', 'rat', 'river', 'road', 'rock', 'room', 'rope', 'rose', 'sail', 'sand', 'sea', 'ship', 'shoe', 'shirt', 'sky', 'snake', 'snow', 'sock', 'song', 'spider', 'spoon', 'star', 'stone', 'sun', 'table', 'tea', 'tent', 'tiger', 'toe', 'tooth', 'train','tree', 'truck', 'turtle', 'umbrella', 'vegetable', 'water', 'whale', 'wheel', 'wind', 'window', 'wolf']
    elif(diff=="M" or diff=="m"):
        words = ['Largesse', 'Latent', 'Laudable', 'Limpid', 'Loquacious', 'Lugubrious', 'Magnanimous', 'Malfeasance', 'Malign', 'Manifest','Aberration', 'Acquiesce', 'Aesthetic', 'Alacrity', 'Ambivalent', 'Anomaly', 'Antithesis', 'Apathy', 'Arduous', 'Assuage', 'Avarice', 'Bellicose', 'Benevolent', 'Bombastic', 'Capricious', 'Cathartic', 'Cogent', 'Conundrum', 'Corpulent', 'Credulous', 'Cynical', 'Deleterious', 'Demure', 'Denigrate', 'Deprecate', 'Deride', 'Despot', 'Dilatory', 'Disparage', 'Dissident', 'Egregious', 'Eloquent', 'Emulate', 'Enigmatic', 'Epitome', 'Equanimity', 'Esoteric', 'Euphemism', 'Exacerbate', 'Exalt', 'Exemplary', 'Extol', 'Fastidious', 'Fatuous', 'Fecund', 'Felicity', 'Flippant', 'Garrulous', 'Gregarious', 'Hackneyed', 'Hegemony', 'Hubris', 'Iconoclast', 'Idiosyncrasy', 'Ignominy', 'Impervious', 'Impetuous', 'Implacable', 'Importune', 'Impugn', 'Inchoate', 'Inculcate', 'Indefatigable', 'Indolent', 'Ineffable', 'Ineluctable', 'Inexorable', 'Ingenuous', 'Inimical', 'Inscrutable', 'Insidious', 'Insipid', 'Insolent', 'Intrepid', 'Intransigent', 'Invective', 'Invidious', 'Irascible', 'Jocular', 'Juxtapose', 'Lachrymose', 'Lament', 'Languid']
    elif(diff=="H" or diff=="h"):
        words = ['Acquiesce', 'Adjudicate', 'Ambiguous', 'Anomaly', 'Antithesis', 'Apparition', 'Articulate', 'Assiduous', 'Avarice', 'Bellicose', 'Belligerent', 'Bombastic', 'Capricious', 'Clandestine', 'Coalesce', 'Collusion', 'Conundrum', 'Copious', 'Corpulent', 'Culpable', 'Delineate', 'Deride', 'Despotism', 'Disseminate', 'Ebullient', 'Eccentric', 'Eclectic', 'Effervescent', 'Egregious', 'Elicit', 'Emulate', 'Enigmatic', 'Ephemeral', 'Epitome', 'Equanimity', 'Equivocal', 'Esoteric', 'Exacerbate', 'Excoriate', 'Exculpate', 'Exigent', 'Extricate', 'Fastidious', 'Fatuous', 'Fecund', 'Felicity', 'Flippant', 'Florid', 'Fractious', 'Grandiloquent', 'Harbinger', 'Histrionic', 'Iconoclast', 'Idiosyncrasy', 'Ignominious', 'Imbroglio', 'Imperious', 'Impervious', 'Implacable', 'Inadvertent', 'Inchoate', 'Ineffable', 'Ineluctable', 'Inexorable', 'Ingenuous', 'Inimical', 'Inscrutable', 'Insidious', 'Insouciant', 'Interlocutor', 'Intransigent', 'Invective', 'Invidious', 'Irascible', 'Juxtaposition', 'Lascivious', 'Lethargic', 'Loquacious', 'Lugubrious', 'Magnanimous', 'Malfeasance', 'Mellifluous', 'Mendacious', 'Mercurial', 'Metamorphosis',    'Misanthrope',    'Misnomer',    'Mitigate',    'Moribund',    'Multifarious',    'Nascent',    'Nebulous',    'Neologism',    'Nihilism']
    else:
        print("!! WRONG CHOICE !!")
        print("CHOOSE AGAIN !!")
        Difficulty()
    #return list of words in lowercase
    return words
#rules of Hangman
def Rules():
    print("""\n RULES OF HANGMAN

The game starts with choosing a random word and telling the player how many letters are in the word.

The player then start guessing letters one at a time. For every incorrect guess, a part of a stick figure is drawn (commonly called a "gallows"), representing a man being hanged.

The number of incorrect guesses allowed is 7. Once the limit is reached, the game is over and the players looses.

If the player correctly guess a letter, he/she will be awarded with +10 points. The guessing player(s) continue to guess letters until they either correctly guess the whole word or reach the limit of incorrect guesses.

The game can be played as a competition between multiple players, with the player(s) with the most points at the end of the game declared the winner.

Type "exit" to exit the game :) 
    
                                                            """)
#select Random word from list of word
def wordsrandom():
    random_word=random.choice(word_list)
    return random_word.lower()
#it will show Final Score of User
def reports(name,points,rounds):
        print("\n\t\tReport")
        line1="\nName: {}"
        line2="Rounds: {}"
        line3="points: {}"
        print(line1.format(name.upper()))
        print(line2.format(rounds))
        print(line3.format(points))
        print("\n\t\tYou Played Well")
#it enter the data into a file thats stores data of user that have played the game
def Enter_Data(name,points,rounds,time,date):
    in_data='''\n{0}\t{1}\t{2}\t\t{3}\t{4}\n'''
    try:
        fileptr=open('Hangman_History.txt','a')
        fileptr.write(in_data.format(date,time,name,rounds,points))
    finally:
        fileptr.close()
#it will print the data that is store in the file
def Print_Data():
    try:
        fileptr=open('Hangman_History.txt','r')
        print("\n\t\tHistory")
        out_data='''\nDATE\t\tTIME\t\tNAME\t\tROUNDS\tPOINTS\n'''
        print(out_data)
        print(fileptr.read())
    finally:
        fileptr.close()
#Ask user to play Again
def PlayAgain():
    re=input("Do you Want to Play again (Y/N):")
    if re=='Y' or re=='y':
        print("\nSure\n")
        CPU()
    elif re=='N' or re=='n':
        print("Thank you for playing\nI hope you Enjoyed the Game ")
        print("\n\t\tCredits")
        print("\nNAME: AKSHAT PANDEY")
        print("\nSAP ID:500101788")
        print("\nBatch: B-9")
    else:
        print("XXX  Wrong Choice XXX")
        print("\nEnter Again\n")
        PlayAgain()
def CPU():
    local_time=datetime.datetime.now()
    date=local_time.strftime("%x") #store Date in MM/DD/YY Format 
    time=local_time.strftime("%X") #Store TIme 24 Hour Format
    points=0        #stores points obtained by user
    rounds=1        #Count the rounds
    print("\n\t\tHANGMAN\n")
    print("\n\t\tROUND 1")
    Main_Body(points,rounds)
    Enter_Data(name,points,rounds,time,date)
    Print_Data()
    PlayAgain()
def Main_Body(points,rounds):
    word=wordsrandom() #Random Word
    #Hangman Stick figure
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
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
# Local Variable Required
    guesses = []    #stores All the Correct Guesses
    wrong=[]        #stores All the wrong Guesses
    maxfails = 7    #Maximum chance a user have
    fails = 0       #Store no. of wrong guesses 

# Main loop
    while fails < maxfails:
    # Display the current state of the word in Dashes (_)
        display = ""
        for letter in word:
            if letter in guesses:
                display += letter
            else:
                display += "_ "
        #if guess the correct word
        if "_" not in display:
            print("\nCongratulations! You guessed the word!")
            print("You passed to Next Round")
            points+=10
            break
        print("GUESS-> ",end="")
        print(display)
        print("\nWrong: ",end="")
        for i in wrong:
            print(i,end=" ")

    # Get a guess from the user
        guess = input("\nGuess a letter: ").lower()

    # Check if the guess is valid or user want forcefull exit
        if guess=="exit":
            print("\nExitting the System")
            break
    # If user enter more than 1 letter  
        elif len(guess) != 1:
            print("\nPlease enter a single letter.")
            continue
    # If user Entered a letter more than 1 time
        elif guess in guesses or guess in wrong:
            print("\nYou already guessed that letter.")
            continue
    # If user Entered a special character  
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("\nPlease enter a letter.")
            continue
    # Check if the guess is in the word
        if guess in word:
            print("Correct!")
            guesses.append(guess)
            print("\n"+HANGMAN_PICS[fails])
    # If user Entered wrong letter
        else:
            print("OOPS! Wrong Letter")
            wrong.append(guess)
            fails += 1
            print(HANGMAN_PICS[fails])
    #Oustside the Loop
    #if user Run out chances
    if fails == maxfails:
        print("\nSorry, you ran out of guesses. The word was",word)
        reports(name,points,rounds)
    #if user want to exit forcefully
    elif guess=="exit":
        reports(name,points,rounds)
    #if user guessed the word
    else:
        rounds+=1
        stm="\n\t\tRound {}"
        print(stm.format(rounds))
        Main_Body(points,rounds)

#FUNCTION CALLING

#User-Interface
print("\t\tHANGMAN")
name=input("\nEnter Your Full Name: ").title()
WannaPlay()
time.sleep(2)
Rules()
word_list=Difficulty()
time.sleep(2)
CPU()
#Thank You
#by akshat Pandey 
