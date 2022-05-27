# 8강 Exercise Program 1
instr, outstr = '',''
count, i = 0, 0

instr = input('문자열을 입력하세요 : ')
count = len(instr)

for i in range(0, count):
    outstr += instr[count - (i + 1)]

print('내용을 거꾸로 출력 --> %s' % outstr)


# 8강 Exercise Program 2
import turtle as t
import random
from tkinter.simpledialog import *

instr = ''
x, y = 300, 300
tx, ty, txtsize = [0] * 3

t.title('거북이 글자쓰기')
t.shape('turtle')
t.setup(width=x+50, height=y+50)
t.screensize(x, y)
t.penup()

instr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

for ch in instr:
    tx = random.randrange(-x/2, y/2)
    ty = random.randrange(-x/2, y/2)
    r = random.random(); g= random.random(); b = random.random()
    txtsize = random.randrange(10, 50)
    t.goto(tx, ty)
    t.pencolor((r,g,b))
    t.write(ch, font = ('맑은 고딕', txtsize, 'bold'))

t.done()


# 9강 Exercise Program 1
import random

def getNumber():
    return random.randrange(1, 46)

lotto = []
num = 0
print('** 로또 추첨을 시작합니다. ** \n')

while True:
    num = getNumber()
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >= 6:
        break

print('추첨된 로또 번호 ==> ', end='')
lotto.sort()
for i in range(0, 6):
    print('%d ' % lotto[i], end='')


# 9강 Exercise Program 2
import random
from tkinter.simpledialog import *

def getString():
    retstr = ''
    retstr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
    return retstr

def getRGB():
    r,g,b=0,0,0
    r = random.random(); g = random.random(); b = random.random()
    return(r,g,b)

def getXYAS(sw, sh):
    x,y,angle,size = 0,0,0,0
    x = random.randrange(-sw / 2, sw / 2)
    y = random.randrange(-sh / 2, sh / 2)
    angle = random.randrange(0, 360)
    size = random.randrange(10, 50)
    return [x, y, angle, size]

import turtle as t
instr = ''
swidth, sheight = 300, 300
tx, ty, tangle, txtsize = [0] * 4

t.title('거북이 글자쓰기(모듈버전)')
t.shape('turtle')
t.setup(width=swidth+50, height=sheight+50)
t.screensize(swidth, sheight)
t.penup()
t.speed(10)

instr = getString()

for ch in instr:
    tx, ty, tangle, txtsize = getXYAS(swidth, sheight)
    r,g,b = getRGB()
    t.goto(tx,ty)
    t.left(tangle)
    t.pencolor((r,g,b))
    t.write(ch, font = ('맑은 고딕', txtsize, 'bold'))

t.done()
