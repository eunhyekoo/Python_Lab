import turtle
import random 

screen = turtle.Screen()
image1 = "./rabbit.gif"
image2= "./turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.shape(image1)
t1.penup()
t1.goto(-300,0)


t2.shape(image2)
t2.penup()
t2.goto(-300,-200)

t1.pendown()
t2.pendown()

for i in range(10):
    d1 = random.randint(1,60)
    t1.forward(d1)
    d2 = random.randint(1,60)
    t2.forward(d2)

if d1 >d2 :
    #print("토끼 승")
    t1.write("토끼 승")
elif d1<d2:
    #print("거북이 승")
    t2.write("거북이 승")
    
turtle.done()
