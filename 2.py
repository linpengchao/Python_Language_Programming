# # turtle绘图
# import turtle
#
# turtle.setup(800, 400)
# turtle.speed(400)
# turtle.penup()
# turtle.goto(-300, 0)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor('green')
# turtle.seth(-45)
# for i in range(4):
#     turtle.circle(40, 90)
#     turtle.circle(-40, 90)
# turtle.circle(40, 45)
# turtle.fd(100)
# turtle.circle(40, 180)
# turtle.fd(30)
# turtle.done()

# # turtle square
# import turtle
#
# turtle.setup(400, 400)
# turtle.penup()
# turtle.goto(-100, -100)
# turtle.pendown()
# turtle.pensize(8)
# turtle.pencolor('black')
# for i in range(1, 5):
#     turtle.fd(200)
#     turtle.seth(90*i)
# turtle.done()

# # turtle 6
# import turtle
#
# turtle.setup(400, 400)
# turtle.penup()
# turtle.goto(-100, -100)
# turtle.pendown()
# turtle.pensize(8)
# turtle.pencolor('black')
# for i in range(1, 7):
#     turtle.fd(100)
#     turtle.seth(60*i)
# turtle.done()

# # turtle 9
# import turtle
#
# turtle.setup(400, 400)
# turtle.penup()
# turtle.goto(-100, -100)
# turtle.pendown()
# turtle.pensize(8)
# turtle.pencolor('black')
# for i in range(1, 10):
#     turtle.fd(100)
#     turtle.seth(80*i)
# turtle.done()

# turtle 44
import turtle

turtle.setup(400, 400)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.pensize(8)
turtle.pencolor('black')
for i in range(4):
    turtle.seth(45 + 90*i)
    turtle.fd(100)
    turtle.seth(45 + 90*i + 90)
    turtle.circle(100, 45)
    turtle.seth(270 + 90*i)
    turtle.fd(100)
turtle.done()
