# # BMI计算
#
# BMINumInputHeight, BMINumInputWeight = eval(input(
#     '请输入身高(米)和体重(公斤)[逗号隔开]:'))
# BMINumResultIndex = BMINumInputWeight / BMINumInputHeight ** 2
# # 国际指标   # 国内指标
# if BMINumResultIndex < 18.5:
#     BMIStrTypeIntl, BMIStrTypeInland = '偏瘦', '偏瘦'
# elif 18.5 <= BMINumResultIndex < 24:
#     BMIStrTypeIntl, BMIStrTypeInland = '正常', '正常'
# elif 24 <= BMINumResultIndex < 25:
#     BMIStrTypeIntl, BMIStrTypeInland = '正常', '偏胖'
# elif 25 <= BMINumResultIndex < 28:
#     BMIStrTypeIntl, BMIStrTypeInland = '偏胖', '偏胖'
# elif 28 <= BMINumResultIndex < 30:
#     BMIStrTypeIntl, BMIStrTypeInland = '偏胖', '肥胖'
# else:
#     BMIStrTypeIntl, BMIStrTypeInland = '肥胖', '肥胖'
# print('BMI 指标为:{.3f}, 国际{}, 国内{}'.format(
#     BMINumResultIndex, BMIStrTypeIntl, BMIStrTypeInland))

# # 近似法公式计算圆周率
# pi = 0
# N = 100
# for k in range(N) :
#     pi += 1/pow(16,k)*( \
#     4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
# print("圆周率值是: {}".format(pi))

# # 蒙特卡洛法计算圆周率
# # import random
# # import time
# # import turtle
# #
# # ConstNumTotalDots = eval(input('输入取点数量：'))
# # # 画一个扇形
# # turtle.penup()
# # turtle.setup(500, 500)
# # turtle.hideturtle()
# # turtle.speed(0)
# # turtle.pencolor('blue')
# # turtle.pensize(4)
# # turtle.goto(-200, -200)
# # turtle.pendown()
# # turtle.circle(400, 90)
# # turtle.seth(180)
# # turtle.fd(400)
# # turtle.seth(270)
# # turtle.fd(400)
# # turtle.penup()
# # turtle.pencolor('black')
# # turtle.pensize(2)
# # # 开始打点
# # PiNumInnerDots = 0
# # PiTimeStart = time.perf_counter()
# # for tempCount in range(1, ConstNumTotalDots+1):
# #     tempRandomX, tempRandomY = random.random(), random.random()
# #     turtle.goto(tempRandomX*400-200, tempRandomY*400-200)
# #     turtle.pendown()
# #     turtle.dot()
# #     turtle.penup()
# #     if pow(tempRandomX**2 + tempRandomY**2, 0.5) <= 1.0:
# #         PiNumInnerDots += 1
# # PiNumResult = 4 * PiNumInnerDots/ConstNumTotalDots
# # print('圆周率：{:.15f}'.format(PiNumResult))
# # print('运行时间：{:.3f}'.format(time.perf_counter() - PiTimeStart))
# # turtle.goto(0, 220)
# # turtle.pensize(5)
# # turtle.pendown()
# # turtle.write('PI:{:.15f}'.format(PiNumResult))
# # turtle.penup()
# # turtle.done()

# # 玫瑰花数
# for i in range(1000, 10000):
#     if (eval(str(i)[0]) ** 4 + eval(str(i)[1]) ** 4
#         + eval(str(i)[2]) ** 4 + eval(str(i)[3]) ** 4) == i:
#         print(i)

# 100内素数和
numSum = 0
for i in range(2, 101):
    # 判断素数
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        numSum += i
print(numSum)
