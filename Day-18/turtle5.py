# import colorgram
#
# colors=colorgram.extract('dotpaint.jpg',6)
#
# # first_color=colors[0]
# # rgb=first_color.rgb
# # print(rgb)
# list=[]
# for x in colors:
#
#     rgb=x.rgb
#     list.append(rgb)
# print(list)


import colorgram
rgb_colors =[]
colors= colorgram.extract('dotpaint.jpg',30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)

output:-
color_list=[(249, 248, 248), (232, 241, 239), (1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7)]
