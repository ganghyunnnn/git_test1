# 10강

#
from tkinter import *

window = Tk()
window.title('윈도창 연습')
window.geometry('400x100')
window.resizable(width=FALSE, height=FALSE)

window.mainloop()

#
from tkinter import *
window = Tk()

label1 = Label(window, text = 'COOKBOOK~~ Python을')
label2 = Label(window, text = '열심히', font = ('궁서체', 30), fg = 'blue')
label3 = Label(window, text = '공부 중입니다.', bg = 'magenta', width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()

# PhotoImage()
from tkinter import *
window = Tk()

photo = PhotoImage(file = 'GIF/cat.gif')
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()

#
from tkinter import *
window = Tk()

photo1 = PhotoImage(file='GIF/cat.gif')
photo2 = PhotoImage(file='GIF/cat2.gif')
label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)

window.mainloop()

# Button()
from tkinter import *
window = Tk()

button1 = Button(window, text='파이썬 종료', fg='red', command=quit)
button1.pack()

window.mainloop()

# Button()
from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo('강아지 버튼', '강아지가 귀엽죠? ^^')

window = Tk()

photo = PhotoImage(file = 'GIF/dog2.gif')
button1 = Button(window, image=photo, command=myFunc())
button1.pack()

window.mainloop()

# 두 숫자 사이의 완전수 찾기(완전수, 완전수 개수)
# 모든 약수를 더하면 자기 자신 ex)6
def is_pn(num):
    a =[]
    for i in range(1, num):
        if num % i == 0:
            a.append(i)
    if sum(a)==num:
        return True
    else:
        return False

num1, num2 = map(int, input('Please give me two numbers :').split(','))

pn = []
for i in range(num1, num2+1):
    if is_pn(i) == True:
        pn.append(i)

print(f'두 수 사이의 완전수: {pn}')
print('두 수 사이의 완전수 개수: ' + str(len(pn)))

# 두 숫자 중 큰 숫자를 출력하는 함수(max2), 작은 수 출력 (min2)
def max2(num1, num2):
    if num1 > num2:
        return num1
    else: return num2

def min2(num1, num2):
    if num1 > num2:
        return num2
    else: return num1

num1, num2 = map(int, input('Please give me two numbers :').split(','))

a = max2(num1, num2)
b = min2(num1, num2)

if num1 != num2:
    print('큰 수: %d' % a)
    print('작은 수: %d' % b)
else:
    print('두 수가 같습니다.')

#한 줄
def max3(n,m):
    return n if n > m else m

# 윤년 (4, 1000으로 나누어지는 연도, but 100,으로 나누어떨어지면 윤년 x)
def year(num):
    if num % 100 == 0:
        if num % 1000 == 0:
            return True
        else:
            return False
    elif num % 4 == 0:
        return True

input = int(input('input a year'))

if year(input) == True:
    print('%d년은 윤년입니다.' % input)
else:
    print('%d년은 윤년이 아닙니다.' % input)
