import turtle

t= turtle.Turtle()
window = turtle.Screen()

window.setup(600, 600a
window.bgcolor("black")

t.hideturtle()
t.speed(10)
t.pensize(10)
t.pencolor("white")

#t.down()
#t.forward(600)
#t.up()

#가로선 그리기
for i in range(3):
    t.up()
    t.goto(-300,i*200-300)
    t.down()
    t.forward(600)
t.left(90)

# 세로선 그리기
for i in range(1,3):
    t.up()
    t.goto(i*200-300,-300)
    t.down()
    t.forward(600)

t.pencolor("green")
t.up()

# x 표시 그리기
def draw_x(x,y):
    t.up( )
    t.goto(x+20, y-20)
    t.setheading(-45)
    t.down( )
    t.forward(226)
    t.up( )
    t.goto(x+180,y-20)
    t.setheading(-135)
    t.down( )
    t.forward(226)
    t.up( )


# 0 표시를 그린다.
def draw_o(x,y):
    t.up( )
    t.goto(x+100, y-180)
    t.setheading(0)
    t.down( )
    t.circle(80)
    t.up( )
    
board = ["","","","","","","","",""]
nextTurn = "X"
   
def draw(board):
    x = -300
    y = 300
    for piece in board:
        if piece == "X":
            draw_x(x,y)
        elif piece == "O":
            draw_o(x,y)
            
        x = x+200
        if x>= 100:
            x = -300
            y = y-200
            

# 사용자가 보드를 클릭하면 해당되는 칸을 찾는다
def click(x,y):
    global nextTurn, board
    #print(x,"",y)
    column = (x+300) // 200
    row = -(y-300)//200
    cell = column + row*3
    cell = int(cell)
    print(row,"",column)
    board[cell] = nextTurn
    
    if nextTurn == "X":
        nextTurn = "O"
    else:
        nextTurn = "X"
    draw(board)

#draw(board)
window.onscreenclick(click)
turtle.mainloop()
turtle.bye()
