from PIL import Image,ImageTk, ImageFilter
import tkinter as tk
from tkinter import filedialog as fd  
# 파일을 사용할 수 있는 라이브러리

img = None
tk_img = None

# 파일 기능을 메뉴로 연결
def open():
    global img,tk_img
    fname = fd.askopenfilename() #
    img = Image.open(fname)
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(250,250,image= tk_img)
    window.update()
    

def quit():
    window.quit()
    
#영상처리 기능을 메뉴로 연결 (영상회전, 흐리게)
def image_rotate():
    out = img.rotate(45)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image = tk_img)
    window.update()

def image_blur():
    global img,tk_img
    out = img.filter(ImageFilter.BLUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image = tk_img)
    window.update()
    
window = tk.Tk()
canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

# 메뉴 생성 (파일, 영상처리 두개의 메뉴 )
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)

filemenu.add_command(label = "열기",command = open)
filemenu.add_command(label = "종료", command = quit)
ipmenu.add_command(label="영상회전", command = image_rotate)
ipmenu.add_command(label="흐리게", command = image_blur)

menubar.add_cascade(label="파일", menu = filemenu)
menubar.add_cascade(label="영상처리", menu = ipmenu)

window.config(menu = menubar) #윈도우창에 메뉴 등록
window.mainloop()
