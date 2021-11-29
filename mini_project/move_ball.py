from tkinter import *
import random
import time

color_list = ["yellow","green","blue","red","orange","pink","grey"]
balls_list = []

class Ball:
    def __init__(self,canvas,color,size,x,y,xspeed, yspeed):
        self.canvas = canvas
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.id = canvas.create_oval(x,y,x+size,y+size,fill= color)
        
    def move(self):
        
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1,y1,x2,y2) = self.canvas.coords(self.id)
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= WIDTH : # 공의 좌표가 음수이거나 오른쪽 경계를 넘으면
            self.xspeed =- self.xspeed # 스피드를 - 마이너스로 변경하면 반대로 움직임.
WIDTH = 800
HEIGHT = 400

window = Tk()
canvas = Canvas(window,width=WIDTH, height = HEIGHT)
canvas.pack()


for i in range(10):
    color = random.choice(color_list)
    size  = random.randrange(10,100)
    xspeed  = random.randrange(1,10)
    yspeed = random.randrange(1,10)
    balls_list.append(Ball(canvas,color,size,0,0,xspeed,yspeed))
    print(balls_list)
    
while True:
    for ball in balls_list:
        ball.move()
    
    #윈도우 업데이트를 해줘야 변경된 사항이 그려짐
    window.update()
    time.sleep(0.03)
    
window.mainloop()
