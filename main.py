# import colorgram

import turtle as turtle_module
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle_module.colormode(255)
mint = turtle_module.Turtle()
mint.speed("fastest")
mint.penup()
mint.hideturtle()

color_list = [(229, 232, 240), (222, 157, 105), (238, 220, 230), (238, 217, 199), (97, 170, 213), (235, 65, 81), (218, 232, 226), (229, 118, 145), (238, 202, 96), (125, 189, 164), (29, 121, 164), (234, 72, 58), (178, 182, 216), (35, 115, 70), (24, 38, 79), (167, 210, 179), (235, 157, 178), (104, 63, 85), (170, 55, 38), (26, 133, 235), (241, 158, 148), (38, 154, 196), (26, 93, 63), (53, 169, 135), (76, 73, 26), (4, 81, 109), (31, 72, 37), (21, 59, 113), (152, 206, 218), (189, 159, 61)]

mint.setheading(225)
mint.forward(300)
mint.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    mint.dot(20, random.choice(color_list))
    mint.forward(50)

    if dot_count % 10 == 0:
        mint.setheading(90)
        mint.forward(50)
        mint.setheading(180)
        mint.forward(500)
        mint.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()