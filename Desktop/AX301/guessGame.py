from Tkinter import *
import random 

class Application(frame):
	def __init__(self, master): 
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		self.number = random.randint(1,101)

	def create_widgets(self):
		Label(self, text = "There's a number between 1 and 100.").grid(row = 0, colomn = 0, sticky = W)
		Label(self, text = "Guess the number in as few guesses as possible.").grid(row = 0, colomn = 0, sticky = W)


		Label(self, text = "Take a guess.").grid(row = 0, colomn = 0, sticky = W)
		self.guess_ent = Entry(self)
		self.guess_ent.grid(row = 2, colomn = 1, sticky = W)

		Label(self, text = "Click submit to start game.").grid(row = 0, colomn = 0, sticky = W)
		Button(self, text = "Submit.", command = self.run_game.grid(row = 0, colomn = 0, sticky = W)

		
