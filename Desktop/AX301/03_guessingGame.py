#Guessing game

import random
myName = raw_input("Hi what's your name?")
randomNumber=random.randint(1,10)
print "I am thinking of a number..."
guessesTaken = 0

while guessesTaken <4:
	guess = int(raw_input("Guess a number from 1 to 10 "))
	guessesTaken=guessesTaken+1

	if guess > randomNumber:
		print "Your guess is too high. Try again."
	elif guess < randomNumber:
		print "Your guess is too low. Try again."
	elif guess == randomNumber:
		break


if guess == randomNumber:
	print "Congratulations %s! You got it correctly at %d guesses" %(myName,guessesTaken)
elif guess !=randomNumber:
	print "Too bad %s! the correct answer is %d. Try again sucker!" %(myName,guess)