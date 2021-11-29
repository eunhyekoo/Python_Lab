from tkinter import *

window = Tk()
window.title("My calculator")

display  = Entry(window, width = 33, bg = "yellow")
display.grid(row = 0, column  = 0, columnspan = 5)

button_list = [
    '7','8','9','/','C',
    '4','5','6','*','',
    '1','2','3','-','',
    '0','.','=','+','' 
]



def click(key):
    if key == "=":
        result = eval(display.get()) # eval 함수를 사용해서 수식 계산
        s = str(result)
        display.insert(END,"="+s)  # 엔트리 위젯의 끝에 key 추가
    elif key =="C":
        display.delete(0,END)

    else:
        display.insert(END,key)

row_index = 1
col_index = 0

for button_text in button_list:
    def process(t = button_text):
        click(t)
        
    Button(window,text = button_text,width = 5,command=process).grid(row = row_index, column = col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
    
window.mainloop()
