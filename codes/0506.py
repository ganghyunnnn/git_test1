# 11장
inFp = None
inStr = ''

inFp = open('data1.txt', 'r', encoding='UTF8')

while True:
    inStr = inFp.readline()
    if inStr == '':
        break;
    print(inStr, end='')

inFp.close()

# Self study 11-1
inFp = None
inStr = ''

inFp = open('data1.txt', 'r', encoding='UTF8')
line = 0

while True:
    inStr = inFp.readline()
    line += 1
    if inStr == '':
        break;
    print('%d : %s' % (line, inStr), end='')

inFp.close()

# code 11-07.py
outFp = None
outStr = ''

outFp = open('data2.txt', 'w', encoding='UTF8')

while True:
    outStr = input('내용 입력 : ')
    if outStr != '':
        outFp.writelines(outStr + '\n')
    else:
        break

outFp.close()
print('--- 정상적으로 파일에 씀 ---')

# Self study 11-3
outFp = None
outStr = ''

file = input('파일명 : ')
outFp = open(file, 'w', encoding='UTF8')

while True:
    outStr = input('내용 입력 : ')
    if outStr != '':
        outFp.writelines(outStr + '\n')
    else:
        break

outFp.close()
print('--- 정상적으로 파일에 씀 ---')

# Code 11-10.py
inFp, outFp = None, None
inStr = ''

inFp = open('C:/Windows/notepad.exe', 'rb')
outFp = open('C:/Temp/notepad.exe', 'wb')

while True:
    inStr = inFp.read(1)
    if not inStr:
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print('--- 이진 파일이 정상적으로 복사되었음 ---')

# Code 11-15.py
num1 = input('숫자 -->')
num2 = input('숫자 -->')

try:
    num1 = int(num1)
    num2 = int(num2)
    while True:
        res = num1 / num2
except ValueError:
    print('문자열은 숫자로 변환할 수 없습니다.')

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except KeyboardInterrupt:
    print('Ctrl+C를 눌렀군요.')

# Exercise Program 1
inFp, outFp = None, None
inStr, outStr = '', ''
i = 0
secu = 0

secuYN = input(' 1. 암호화 2. 암호해석 중 선택 : ')
inFname = input('입력 파일명을 입력하세요 : ')
outFname = input('출력 파일명을 입력하세요 : ')

if secuYN == '1':
    secu = 100
elif secuYN == '2':
    secu = -100

inFp = open(inFname, 'r', encoding='utf-8')
outFp = open(outFname, 'w', encoding='utf-8')

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ''
    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2

    outFp.wirte(outStr)

outFp.close()
inFp.close()
print('%s --> %s 변환 완료' % (inFname, outFname))

# Exercise Program 2
from tkinter import *

def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ''
    for i in range(0, XSIZE):
        tmpString = ''
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += '#%02x%02x%02x ' % (data,data,data)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []

window = Tk()
window.title('흑백 사진 보기')
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state='normal')

loadImage(filename)
displayImage(inImage)
filename = 'RAW/tree.raw'
canvas.pack()
window.mainloop()
