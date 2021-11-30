import turtle
import random

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

#터틀이 그려지는 screen을 가져옴
screen = player.getscreen()
asteroids = []

# 소행성 그리기
for i in range(30):
    a1 = turtle.Turtle()
    a1.color("red")
    a1.shape("circle")
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300,300), random.randint(-300,300))
    asteroids.append(a1)
    
def turnleft():
    player.left(30)
def turnright():
    player.right(30)

def turnup():
    player.forward(20)


screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(turnup)
screen.listen()

def play():
    player.forward(2)
    
    for a in asteroids:
        a.right(random.randint(-180,180))
        a.forward(2)
        
        if player.distance(a)<20:
            player.write("clear")
            a.ht() #hideturtle
    # ontimer -> 일정한 시간이 지난뒤 실행할 함수
    screen.ontimer(play,1000)  # 20밀리초가 지난후 play 함수 호출

screen.ontimer(play,1000)
turtle.done()
