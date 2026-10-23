# import turtle
#
# # -- setup --
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
#
# # -- functions --
#
# def DrawPoly(someturtle, somesides, somesize):
#     angle = 360 / somesize
#     for i in range(somesize):
#         someturtle.forward(somesize)
#         someturtle.left(angle)
# def DrawSpiral(someturtle, angle):
#     size = 1
#     for i in range(100):
#         someturtle.forward(size)
#         someturtle.right(angle)
#         size = size + 2
#
# def DrawEquitriangle(someturtle, somesize):
#     DrawPoly(someturtle, 3 , somesize)
#
# def DrawStar(someturtle, size):
#     for i in range(5):
#         someturtle.forward(size)
#         someturtle.right(144)
#
# def DrawSprite(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
#
#  # -- exercises --
#
#  # # Exercise 1
#  # tess.pencolor("hotpink")
#  # tess.pensize(3)
#  # DrawPoly(tess, 8, 50)
#
# # #Exercise 2
#  # for i in range(20):
# #     DrawPoly(tess, 4, 100)
#   #     tess.left(18)
#
#         # Exercise 3--
# # tess.pencolor("blue")
# # tess.pensize(1)
# # tess.penup()
# # tess.goto(-150, 0)
# # tess.pendown()
# # DrawSpiral(tess, 90)
# # tess.penup()
# # tess.goto(150, 0)
# # tess.setheading(0)
# # tess.pendown()
# # DrawSpiral(tess, 89)
#
# # Exercise 4 --
# # DrawEquitriangle(tess,100)
#
#
# # Exercise 5 --
# # tess.color("hotpink")
# # for i in range(5):
# #     DrawStar(tess, 50)
# #     tess.penup()
# #     tess.forward(350)
# #     tess.right(144)
# #     tess.pendown()
#
#
# # Exercise 6 --
#
# DrawSprite(tess, 15, 120)
#
#
#
#
#
#
