import math
import turtle

player =  turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()

# 각도를 조절하는 메서드
def turnleft():
    player.left(5)
def turnright():
    player.right(5)

#포물선을 그리는 메서드
def fire():
    x = 0
    y = 0
    velocity = 50
    angle = player.heading() # 거북이가 바라보는 현재 각도를 반환
    vx = velocity*math.cos(angle*3.14 / 180.0)
    vy = velocity*math.sin(angle*3.14 / 180.0)
    # 각도와 vx,vy 값을 설정해서 
    print(vx,vy)
    while player.ycor() >= 0: #현재 거북이의 y 좌표 반환
        vx = vx
        vy = vy-10
        x = x+vx
        y = y+vy
        player.goto(x,y)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(fire,"space")
screen.listen()

turtle.done()
