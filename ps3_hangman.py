# Hangman game
#

# -----------------------------------
# Helper code


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secWordChar = []
    for char in secretWord:
        secWordChar += char
    return all(char in lettersGuessed for char in secWordChar)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessing = ''
    
    for char in secretWord:
        if char in lettersGuessed:
            guessing += char
        else:
            guessing += "_ "
            
    return guessing



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    result = ''
    for char in alphabet:
        if char not in lettersGuessed:
            result +=char
        
    return result
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guesses = 8

    print("	Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +  " letter long. \n	-------------")
    
    # If you haven't guessed your word and the computer needs you to enter an input
    while isWordGuessed(secretWord, lettersGuessed) == False:
      print("You have " + str(guesses) + " guesses left." + "\n" + "Available letters: " + str(getAvailableLetters(lettersGuessed)))
      alreadyGuessed = str(getAvailableLetters(lettersGuessed))
      # get a character from the user
      yourChar = input('Please guess a letter: ').lower()
      lettersGuessed += yourChar
      # if you had already entered that character
      if yourChar not in alreadyGuessed:
        print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)) + "\n -----------")
      #if you guessed one of the characters from the secret word
      elif yourChar in secretWord:
        print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)) + "\n -----------")
      #if your character is not in the secret word
      elif yourChar not in secretWord:
        guesses -= 1
        print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)) + "\n -----------")
        #when you run out of guesses
        if guesses == 0:
          print("Sorry, you ran out of guesses. The word was " + secretWord)
          break

    # When "is word guessed?" is True --> you won!
    if isWordGuessed(secretWord, lettersGuessed) == True:
      return("	Congratulations, you won")
 

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
