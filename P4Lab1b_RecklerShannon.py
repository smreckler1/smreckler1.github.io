#Title: Shannon Reckler
#Date: 11/2/25
#Assignment Name: P4 Lab 1 Part B
#A brief description of the project: Assignment assess student understanding of decision structures

import turtle
win = turtle.Screen()  
t = turtle.Turtle()

t.pensize(3)           
t.pencolor("blue")     
t.shape("turtle")

t.penup()
t.goto(-100, 0) 
t.pendown()
t.setheading(0)

t.forward(55)
t.left(90)
t.forward(55)
t.left(90)
t.forward(50)
t.right(90)
t.forward(55)
t.right(90)
t.forward(50)

t.penup()
t.goto(50, 0)
t.pendown()
t.setheading(90)

t.forward(125)

t.right(90)
t.circle(-30, 180)

t.left(135)
t.forward(80)

win.mainloop()  
