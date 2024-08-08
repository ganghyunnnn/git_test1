# Exercise Program1
from tkinter import *
from time import *

fnameList = ['cat.gif','cat2.gif','cat3.gif','cat4.gif','cat5.gif','dog.gif','dog2.gif','dog3.gif','dog4.gif']
photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = 'GIF/' + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file='GIF/' + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

window = Tk()
window.geometry('230x250')
window.title('사진 앨범 보기')

btnPrev = Button(window, text = '<< 이전', command = clickPrev)
btnNext = Button(window, text = '다음 >>', command = clickNext)

photo = PhotoImage(file = 'GIF/' + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 50, y = 10)
btnNext.place(x = 130, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()

# Exercise Program2
from tkinter import *
from tkinter.filedialog import *

def func_open():
    filename = askopenfilename(parent = window, filetypes = (('GIF 파일', '*gif'), ('모든 파일', '*.*')))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

window = Tk()
window.geometry('400x400')
window.title('명화 감상하기')

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = func_exit)

window.mainloop()
