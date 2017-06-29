# The aim of this exercise is to create a functioning 'Battleship' game
# which has the player playing against a computer AI.

# Ex. 1 Look at your past examples and write an import statement which
# will allow you to use random numbers in python.
from random import randint

# Ex. 2 Create an empty list
board = []

# Ex. 3 Using a for loop with the range() function,
# create the game board by putting a list of 5 O's into the board list.
# HINT: Don't forget the python shortcut command '*' which will let you
# put multiple strings at the same time.
for x in range(0, 5):
    board.append(["O"] * 5) # same as ["O","O","O","O","O"]

# Ex. 4 Create a function that will take in the parameter board and print the board out completely.
# HINT: You can use the "".join function as needed.


def print_board(board):
    for row in board:
        print " ".join(row)


# Ex. 5 Create two random functions that will return a random column and row.
# Don't forget to also call the function.
# HINT: The randint() function can be used here (Refer to past exercises)
# HINT: The len(listname) function tells us the number elements in the list.
def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


# Ex. 6 Write some code to announce the launch of the game.
print "Let's play Battleship!"
print_board(board)


# Ex. 7. Use a for loop with a range to allow 3 guesses only.
# Ex. 8. Create two varaibles to take in the user-inputted guesses.
# Ex. 9 Write conditional code which will operate 4 possible scenarios:
# a) the guesses from the user are both correct. b) the guesses are outside the values of the board
# c) The User makes a guess that has already been made. d) If the user
# misses. (You need to mark the missed shot with an 'X' instead of an O)

for turn in range(3):
    guess_row = raw_input("Please choose a row: ")
    guess_col = raw_input("Please choose a column: ")

    if guess_row not in "0123456789" or guess_col not in "0123456789":
        print ("Pick a number not a letter.")
    elif int(guess_row) == ship_row and int(guess_col) == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    elif int(guess_row)>4 or int(guess_row)<0 or int(guess_col)>4 or int(guess_col)<0:
        print "Oops, that's not even in the ocean."
    elif board[int(guess_row)][int(guess_col)] == "X":
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[int(guess_row)][int(guess_col)] = "X"
        
    # Print (turn + 1) here!
        print "Turn", turn + 1
    print_board(board)


# Ex. 10. Print the correct answers out for the user to see.
print ship_row
print ship_col
