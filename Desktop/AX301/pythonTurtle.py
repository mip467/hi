import turtle
import sys

bob = turtle.Turtle()

def triangle (color, length):
	bob.fillcolor(color)
	bob.begin_fill()
	x = 0
	while x < 3:
		bob.forward(length)
		bob.right(360/3)
		x = x +1
	bob.end_fill()

input_color = raw_input("What color do you want your triangle to have?")
input_length = int(raw_input("What is the length for your triangle?"))	

triangle(input_color,input_length)

turtle.done()		