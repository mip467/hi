#import required modules
import random

#pictures for stages of game
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\<-|----- Aaron getting hanged by the students of AX301:D
 / \  |
      |
=========''']

def getRandomWord(words):
	splitWordList = words.split()
	wordIndex = random.randint(0,len(splitWordList)-1)
	return splitWordList[wordIndex]

#get guess from user
def getGuess(guessedLetter):
	while True:
		print ("Guess a letter!")
		guess = raw_input(">>")
		guess = guess.lower()

		#check if the in put is acceptable
		if guess not in "abcdefghijklmnopqrstuvwxyz":
			print "Please ener an alphabet letter!"
		elif len(guess) !=1:
			print "Please enter only one letter"
		elif guess in guessedLetter:
			print "you have already guessed this letter. Try another one!"
		else:
			return guess

#print all information
def displayBoard(HANGMANPICS,missedLetters,correctlLetters,secretWord):
	print HANGMANPICS[len(missedLetters)]
	print ''
	print "You have taken %d incorrect guesses" %len(missedLetters)
	
	#print all wrongly guessed letters
	for i in missedLetters:
		print i

	#set blanks to hold all letters for secretWord
	blanks = '_'*len(secretWord)

	for i in range(len(secretWord)):
		if secretWord[i] in correctlLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1]
	print blanks



#set up database of words that we can choose from
words = "table chair monitor lamp screen hangman computer pencil eraser tower drawer camera red yellow black green orange pink"
print "HANGMAN"
print "Let's start guessing the word!"

#choose a random word from the word database
secretWord = getRandomWord(words)

missedLetters = ""
correctlLetters = ""
gameIsDone = False

#main loop
while True:
	displayBoard(HANGMANPICS,missedLetters,correctlLetters,secretWord)
	combinedLetters = missedLetters+correctlLetters
	guess = getGuess(combinedLetters)

	#if user guessed the correct letter
	if guess in secretWord:
		correctLetters = correctlLetters + guess

		#check if player has found all the letters
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctlLetters:
				foundAllLetters = False
				break
		
		if foundAllLetters:
			print "Yes, you guessed it correctly! The correct word is %s!" % secretWord
			gameIsDone = True

	#if user guessed the wrong letter
	else:
		missedLetters = missedLetters + guess

		#check if player has made 6 wrong attempts
		if (len(missedLetters)) == 6:
			displayBoard(HANGMANPICS,missedLetters,correctlLetters,secretWord)
			print "You have lost"
			print "The correct word is %s." %secretWord
			gameIsDone = True

	if gameIsDone == True:
		answer = raw_input("Do you want to play again?")
		answer = answer.lower()
		if answer == "yes":
			missedLetters = ""
			correctlLetters = ""
			secretWord = getRandomWord(words)
			gameIsDone = False
		else:
			break;