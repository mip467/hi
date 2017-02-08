import turtle

pen = turtle.Turtle()

def circle(size, color):
	pen.fillcolor(color)
	pen.begin_fill()
	pen.circle(size)
	pen.end_fill

def triangle(length, color):
	pen.fillcolor(color)
	pen.begin_fill()

	x = 0
	while x < 3:
		pen.forward(length)
		pen.right(120)
		x = x + 1

	pen.end_fill

def star(length, color):
	pen.forward(length)
	pen.right(144)
	
	x = 0
	while x < 5:
		pen.forward(length)
		pen.right(144)
		x = x + 1

	pen.end_fill()

shape = raw_input("What shape - circle / triangle / star?")
input_length = raw_input("How large is your shape? Type a number.")
input_color = raw_input("Which color?")
if shape == "circle":
	circle(int(input_length), input_color)
elif shape == "triangle":
	triangle(int(input_length), input_color)
elif shape == "star":
	star(int(input_length), input_color)



