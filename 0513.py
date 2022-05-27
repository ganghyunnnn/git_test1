class Counter:
    def __init__(self):
        self.count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count

a = Counter()
b = Counter()

# a.reset()
a.increment()

# b.reset()
b.increment()
b.increment()

print('카운터 a의 값은', a.get())
print('카운터 b의 값은', b.get())

# 메소드
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel):
        self.channel = channel
    def getChannel(self):
        return self.channel

t = Television(9, 10, True)

t.show()
t.setChannel(11)
t.show()

# 은닉
class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self, age):
        self.__age = age
    def setName(self, name):
        self.__name = name

obj=Student('Hong', 20)
obj.getName

# 원을 클래스로 표현
import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def setRadius(self, r):
        self.__radius = r
    def getRadius(self):
        return self.__radius
    def getArea(self):
        self.area = math.pi * pow(self.__radius, 2)
        return self.area
    def getCircum(self):
        self.circum = 2 * math.pi * self.__radius
        return self.circum

c1 = Circle(10)
print('원의 반지름=', c1.getRadius())
print('원의 넓이=', c1.getArea())
print('원의 둘레=', c1.getCircum())

# 은행계좌
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def withdraw(self, amount):
        self.__balance -= amount
        print('통장에서 ', amount, '가 출금되었음')
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        print('통장에 ', amount, '가 입금되었음')
        return self.__balance
    def getBalance(self):
        print('잔액: ', self.__balance)
        return self.__balance

a = BankAccount()
a.deposit(100)
a.withdraw(10)
a.getBalance()

# 고양이 클래스 (name, age, color)
class Cat:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age
    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color
    def meow(self):
        print('%s: meow' % self.__name)

cat1 = Cat('Missy', 3, 'black')
cat2 = Cat('Lucky', 5, 'yellow')

cat1.meow()
print(cat1.getName(), cat1.getAge(), cat1.getColor())
cat2.meow()
print(cat2.getName(), cat2.getAge(), cat2.getColor())

# 자동차 클래스
class Car:
    def __init__(self, speed=0, gear=1, color='white'):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
    def setSpeed(self, speed):
        self.__speed = speed;
    def setGear(self, gear):
        self.__gear = gear;
    def setColor(self, color):
        self.__color = color;

    def __str__(self):
        return'(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)

myCar = Car()
myCar.setGear(3);
myCar.setSpeed(100);
print(myCar)

# 객체를 함수로 전달할 때
class Rectangle:
    def __init__(self, side=0):
        self.side = side
    def getArea(self):
        return self.side*self.side

def printAreas(r, n):
    while n >= 1:
        print(r.side, '\t', r.getArea())
        r.side = r.side + 1
        n = n - 1

myRect = Rectangle();
count = 5
printAreas(myRect, count)
print('사각형의 변 =', myRect.side)
print('반복횟수=', count)

# hidden
class Rectangle:
    def __init__(self, side=0):
        self.__side = side
    def getArea(self):
        return self.__side ** 2
    def getSide(self):
        return self.__side
    def addSide(self):
        self.__side += 1

def printAreas(r, n):
    while n >= 1:
        print(r.getSide(), '\t', r.getArea())
        r.addSide()
        n -= 1

myRect = Rectangle()
count = 5
printAreas(myRect, count)
print('사각형의 변 =', myRect.getSide())
print('반복횟수=', count)

# 정적 변수
class Television:
    serialNumber = 0
    def __init__(self):
        Television.serialNumber += 1
        self.__number = Television.serialNumber
    def getSerial(self):
        return self.__number

a = Television()
b = Television()
c = Television()

print(a.getSerial(), b.getSerial(), c.getSerial())

# 특수메소드 예제
class Vector2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def __add__(self, other):
        return Vector2D(self.__x + other.__x, self.__y + other.__y)
    def __sub__(self, other):
        return Vector2D(self.__x - other.__x, self.__y - other.__y)
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
    def __str__(self):
        return '(%g, %g)' % (self.__x, self.__y)

u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
print(a)

#class inheritance
class Car:
    __speed = 0
    def upSpeed(self, value):
        self.__speed += value
        print('현재 속도(슈퍼 클래스) : %d' % self.__speed)

    def getSpeed(self):
        return self.__speed

class Sedan(Car):
    def UpSpeed(self,value):
        self.__speed += value
        if self.__speed > 150:
            self.__speed = 150

a = Sedan()
a.upSpeed(200)
print(a.getSpeed())



# Exercise Program 1
class Car:
    name = ''
    speed = 0

    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    def getName(self):
        return self.__name

    def getSpeed(self):
        return self.__speed

car1, car2 = None, None

car1 = Car('아우디', 0)
car2 = Car('벤츠', 30)

print('%s의 현재 속도는 %d입니다.' % (car1.getName(), car1.getSpeed()))
print('%s의 현재 속도는 %d입니다.' % (car2.getName(), car2.getSpeed()))

# Exercise Program2
import turtle
import random as r

class Shape:
    myTurtle = None
    cx, cy = 0, 0

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')

    def setPen(self):
        R = r.random()
        G = r.random()
        B = r.random()
        self.myTurtle.pencolor((R,G,B))
        pSize = r.randrange(1, 10)
        self.myTurtle.pensize(pSize)

    def drawShape(self):
        pass

class Rectangle(Shape):
    width, height = [0] * 2
    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = r.randrange(20, 100)
        self.height = r.randrange(20, 100)

    def drawShape(self):
        sx1, sy1, sx2, sy2 = [0] * 4

        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2
        sx2 = self.cx + self.width / 2
        sy2 = self.cy + self.height / 2

        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)

def screenLeftClick(x,y):
    rect = Rectangle(x,y)
    rect.drawShape()

turtle.title('거북이로 객체지향 사각형 그리기')
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()
