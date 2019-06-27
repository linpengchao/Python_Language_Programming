# # 数码管绘制，显示时间
# #       6
# #     —————
# #  5 |  1  |   7
# #     —————
# #  4 |     |   2
# #     —————
# #       3
# import turtle
# import time
#
#
# def DigitronDrawLine(draw):
#     if draw:
#         turtle.pendown()
#     else:
#         turtle.penup()
#     turtle.fd(40)
#     turtle.right(90)
#     return
#
#
# def DigitronDrawNum(num, posX, posY):
#     turtle.penup()
#     turtle.goto(posX, posY)
#     if num in [2, 3, 4, 5, 6, 8, 9]:
#         DigitronDrawLine(True)
#     else:
#         DigitronDrawLine(False)
#     if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
#         DigitronDrawLine(True)
#     else:
#         DigitronDrawLine(False)
#     if num in [0, 2, 3, 5, 6, 8, 9]:
#         DigitronDrawLine(True)
#     else:
#         DigitronDrawLine(False)
#     if num in [0, 2, 6, 8]:
#         DigitronDrawLine(True)
#     else:
#         DigitronDrawLine(False)
#     turtle.left(90)
#     if num in [0, 4, 5, 6, 8, 9]:
#         DigitronDrawLine(True)
#     else:
#         DigitronDrawLine(False)
#     if num in [0, 2, 3, 5, 6, 7, 8, 9]:
#         DigitronDrawLine(True)
#     else:
#         DigitronDrawLine(False)
#     if num in [0, 1, 2, 3, 4, 7, 8, 9]:
#         DigitronDrawLine(True)
#     else:
#         DigitronDrawLine(False)
#     turtle.left(180)
#     turtle.penup()
#     return
#
#
# if __name__ == '__main__':
#     timeStructNow = time.gmtime()
#     turtle.setup(800, 400)
#     turtle.hideturtle()
#     turtle.speed(0)
#     turtle.pensize(4)
#     # year
#     DigitronDrawNum(eval(str(timeStructNow.tm_year)[0]), -350, 40)
#     DigitronDrawNum(eval(str(timeStructNow.tm_year)[1]), -350 + 60 * 1, 40)
#     DigitronDrawNum(eval(str(timeStructNow.tm_year)[2]), -350 + 60 * 2, 40)
#     DigitronDrawNum(eval(str(timeStructNow.tm_year)[3]), -350 + 60 * 3, 40)
#     turtle.goto(-350 + 60 * 4, 0)
#     turtle.write('年', font=("Arial", 18, "normal"))
#     # month
#     DigitronDrawNum(eval(str(timeStructNow.tm_mon)[0]), -320 + 60 * 4, 40)
#     try:
#         DigitronDrawNum(eval(str(timeStructNow.tm_mon)[1]), -320 + 60 * 5, 40)
#     except:
#         None
#     turtle.goto(-320 + 60 * 6, 0)
#     turtle.write('月', font=("Arial", 18, "normal"))
#     # day
#     DigitronDrawNum(eval(str(timeStructNow.tm_mday)[0]), -290 + 60 * 6, 40)
#     try:
#         DigitronDrawNum(eval(str(timeStructNow.tm_mday)[1]), -290 + 60 * 7, 40)
#     except:
#         None
#     turtle.goto(-290 + 60 * 8, 0)
#     turtle.write('日', font=("Arial", 18, "normal"))
#     turtle.done()


# # 递归：字符串反转
# def StrReverseStr(str):
#     if str == '':
#         return str
#     else:
#         return StrReverseStr(str[1:])+str[0]
#
#
# if __name__ == '__main__':
#     while True:
#         strResultReverse = StrReverseStr(input())
#         print(strResultReverse)


# # 递归：斐波那契数列
# import sys
# sys.setrecursionlimit(10000) # 例如这里设置为一百万
#
#
# def ListFibonacciSequence(count):
#     if count == 1 or count == 2:
#         return 1
#     else:
#         tempNum = ListFibonacciSequence(count - 1) + ListFibonacciSequence(count - 2)
#         return tempNum
#
#
# if __name__ == '__main__':
#     for tempNum in range(1, 100):
#         tempi = ListFibonacciSequence(tempNum)
#         print('{:3},'.format(tempi))

# # 汉诺塔
# countHanoiMoves = 1
#
#
# def ActHanoiMove(level, src, dist, mid):
#     global countHanoiMoves
#     if level == 1:
#         print('{:}:{:}->{:}'.format(countHanoiMoves, src, dist))
#         countHanoiMoves += 1
#     else:
#         ActHanoiMove(level-1, src, mid, dist)
#         print('{:}:{:}->{:}'.format(countHanoiMoves, src, dist))
#         countHanoiMoves += 1
#         ActHanoiMove(level - 1, src, dist, mid)
# if __name__ == '__main__':
#     ActHanoiMove(4, 'a', 'b', 'c')


# # 科赫雪花
# import turtle
#
#
# def ActSnowLineDraw(length, level):
#     if level == 0:
#         turtle.fd(length)
#         return
#     else:
#         ActSnowLineDraw(length / 3, level - 1)
#         turtle.left(60)
#         ActSnowLineDraw(length / 3, level - 1)
#         turtle.right(120)
#         ActSnowLineDraw(length / 3, level - 1)
#         turtle.left(60)
#         ActSnowLineDraw(length / 3, level - 1)
#
#
# def ActSnowPicDraw(length, level):
#     turtle.pendown()
#     ActSnowLineDraw(length, level)
#     turtle.right(120)
#     ActSnowLineDraw(length, level)
#     turtle.right(120)
#     ActSnowLineDraw(length, level)
#
#
# if __name__ == '__main__':
#     turtle.setup(500, 500)
#     turtle.pensize(2)
#     turtle.penup()
#     turtle.speed(0)
#     turtle.hideturtle()
#     turtle.goto(-150, 90)
#     ActSnowPicDraw(300, 2)
#     turtle.done()

# # 计算乘积
# def cmul(count, result = 1):
#     if count == 1:
#         return result * count
#     else:
#         result = cmul(count - 1)*count
#         return result
#
#
# if __name__ == '__main__':
#     print(eval("cmul({})".format(input())))

# # 斐波那契
# def fbi(n):
#     if n == 1 or n== 2:
#         return 1
#     else:
#         return fbi(n-1)+fbi(n-2)
#
# n = eval(input())
# print(fbi(n))

# # 创建随机密码
# import random
#
# def genpwd(length):
#     return random.randint(10 ** (length - 1), 10 ** length)
#
# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))

# # 计算N开始的5个质数
def cal(n):
    while True:
        for temp in range(2, n):
            if n % temp == 0:
                break
        else:
            return n
        n += 1


def cal1(n):
    if(int(n)==n):
        a = cal(n)
    else:
        a = cal(int(n)+1)
    b = cal(a+1)
    c = cal(b+1)
    d = cal(c + 1)
    e = cal(d + 1)
    print(a, ',', b, ',', c, ',', d, ',', e)

cal1(eval(input()))
