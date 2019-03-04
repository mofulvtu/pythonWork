"""
   desc: 绘制五角星
         循环：for/while
   author: liuzg
   date: 2019/2/26

"""

import turtle
import time


def main():
    turtle.begin_fill()
    for num in range(5):
        turtle.forward(200)
        turtle.right(144)
        turtle.end_fill()


def test2():
    turtle.begin_fill()
    i = 1
    while i <= 5:
        turtle.forward(200)
        turtle.right(144)
        turtle.end_fill()
        i += 1
    time.sleep(2)


def curvemove():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
        turtle.color('red','pink')
        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(111.65)
        curvemove()
        turtle.left(120)
        curvemove()
        turtle.forward(111.65)
        turtle.end_fill()
        turtle.done()


if __name__ == '__main__':
    curvemove()
