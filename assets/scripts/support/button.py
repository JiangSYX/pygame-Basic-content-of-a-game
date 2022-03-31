""" 包含按钮函数 """
import pygame

from math import sqrt, asin, pi # 开方, 反正弦, 圆周率
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 绘制按钮
def button(screen, x, y, text, text_size, center_coordinate, diamond_side_length, ifopen_click = False, language = 'chinese'):
    # 初始化鼠标是否在按钮上面标志和鼠标在按钮上面时按钮内部文字大小变化范围
    if_above = False
    text_size_dvalue = 1

    # 初始化菱形的半长
    diamond_half_height = (int(sqrt(2))/2)*diamond_side_length # 菱形背景框的半高(diamond_side_length为菱形背景框边长)

    # 初始化菱形背景的坐标
    diamond_coordinate_left = (center_coordinate[0] - diamond_half_height, center_coordinate[1]) 
    diamond_coordinate_up = (center_coordinate[0], center_coordinate[1] - diamond_half_height)
    diamond_coordinate_right = (center_coordinate[0] + diamond_half_height, center_coordinate[1])
    diamond_coordinate_down = (center_coordinate[0], center_coordinate[1] + diamond_half_height)

    # 绘制菱形背景
    pygame.draw.polygon(screen, settings('background_color'), [diamond_coordinate_left, diamond_coordinate_up, diamond_coordinate_right, diamond_coordinate_down], 0)
    pygame.draw.polygon(screen, settings('text_color'), [diamond_coordinate_left, diamond_coordinate_up, diamond_coordinate_right, diamond_coordinate_down], 2)

    # 获取鼠标x到菱形边的距离
    distance_mouse = diamond_half_height - abs(center_coordinate[1] - y)

    # 处理鼠标是否在菱形里面
    if x >= center_coordinate[0] - distance_mouse and x <= center_coordinate[0] + distance_mouse and \
       y >= center_coordinate[1] - diamond_half_height and y <= center_coordinate[1] + diamond_half_height and \
       ifopen_click == True:
        # 改变按钮和内部边框, 响应鼠标在菱形里面
        distance = 10 # 内部边框到菱形边的距离

        # 初始化内部菱形边框的坐标
        frame_coordinate_left = (diamond_coordinate_left[0] + distance, diamond_coordinate_left[1])
        frame_coordinate_up = (diamond_coordinate_up[0], diamond_coordinate_up[1] + distance)
        frame_coordinate_right = (diamond_coordinate_right[0] - distance, diamond_coordinate_right[1])
        frame_coordinate_down = (diamond_coordinate_down[0], diamond_coordinate_down[1] - distance)

        # 绘制内部文字和内部边框
        game_object(screen, text_size - text_size_dvalue, text, center_coordinate, change_color = True, new_color = settings('button_above_color'), language = language)
        pygame.draw.polygon(screen, settings('button_above_color'), [frame_coordinate_left, frame_coordinate_up, frame_coordinate_right, frame_coordinate_down], 1)
    
        # 鼠标在按钮上面, if_above设置为True
        if_above = True

    else: # 鼠标不在菱形里面, 绘制按钮内部的文字和内部边框
        distance = 7 # 内部边框到菱形边的距离

        # 初始化内部菱形边框的坐标
        frame_coordinate_left = (diamond_coordinate_left[0] + distance, diamond_coordinate_left[1])
        frame_coordinate_up = (diamond_coordinate_up[0], diamond_coordinate_up[1] + distance)
        frame_coordinate_right = (diamond_coordinate_right[0] - distance, diamond_coordinate_right[1])
        frame_coordinate_down = (diamond_coordinate_down[0], diamond_coordinate_down[1] - distance)

        # 绘制内部文字和内部边框
        game_object(screen, text_size, text, center_coordinate, language = language)
        pygame.draw.polygon(screen, settings('text_color'), [frame_coordinate_left, frame_coordinate_up, frame_coordinate_right, frame_coordinate_down], 1)

        # 鼠标不在按钮上面, if_above设置为False
        if_above = False

    # 返回鼠标是否在按钮上面
    return if_above


# 绘制选项界面的按钮
def options_button(screen, x, y, text, size, coordinate, draw_types = 1, ifopen_click = False, coordinate_type = 'center', language = 'chinese'):
    # 加载检测鼠标是否在按钮上面的标志
    if_above = False

    # 初始化常规按钮
    if language == 'chinese':
        font = pygame.font.Font(settings('text_font_addness'), size)
    elif language == 'english':
        font = pygame.font.Font(settings('text_font_addness_en'), size)

    surface = font.render(text, True, (settings('text_color')))
    rect = surface.get_rect()
    rect.center = coordinate

    # 绘制按钮并且响应鼠标(type = 1, 按钮形式为普遍的变小, 颜色变成灰色)
    if draw_types == 1:

        # 按钮坐标点在中间
        if ifopen_click == True and coordinate_type == 'center' and \
           x >= coordinate[0] - rect.width/2 and x <= coordinate[0] + rect.width/2 and \
           y >= coordinate[1] - rect.height/2 and y <= coordinate[1] + rect.height/2:

            # 初始化变化后的按钮
            if language == 'chinese':
                font = pygame.font.Font(settings('text_font_addness'), size - 1)
            elif language == 'english':
                font = pygame.font.Font(settings('text_font_addness_en'), size - 1)

            surface = font.render(text, True, (settings('button_above_color')))
            rect = surface.get_rect()
            rect.center = coordinate

            screen.blit(surface, rect) # 绘制变化后的按钮
    
            if_above = True

        else: # 鼠标不在按钮上面
            screen.blit(surface, rect) # 鼠标不在按钮上面, 直接绘制常规按钮

            if_above = False

    # 返回按钮是否在鼠标上面
    return if_above