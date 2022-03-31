""" 游戏对象的函数 """
import pygame
import pygame.freetype

from assets.scripts.support.settings import settings # 设置

pygame.init()


# 游戏对象的文字
def game_object(screen, size, text, coordinate, coordinate_type = None, ifreturn = None, change_color = None, new_color = None, language = None, bgcolor = None, if_draw = True, vertical = False, antialiased = True):
    # 绘制对象文字
    if language == 'english':
        font = pygame.freetype.Font(settings('text_font_addness_en'), size)
    else:
        font = pygame.freetype.Font(settings('text_font_addness'), size)

    # 抗锯齿
    font.antialiased = antialiased
    
    # 竖排摆放文本
    font.vertical = vertical

    # 根据change_color决定是否更改颜色
    if change_color == True:
        surface, rect = font.render(text, (new_color), bgcolor)
    else:
        surface, rect = font.render(text, (settings('text_color')), bgcolor)

    # 设置对象的坐标
    if coordinate_type == 'left_centery':
        rect.left, rect.centery = coordinate[0], coordinate[1]
    elif coordinate_type == 'right_centery':
        rect.right, rect.centery = coordinate[0], coordinate[1]
    elif coordinate_type == 'centerx_bottom':
        rect.centerx, rect.bottom = coordinate[0], coordinate[1]
    elif coordinate_type == 'centerx_top':
        rect.centerx, rect.top = coordinate[0], coordinate[1]
    elif coordinate_type == 'topleft':
        rect.topleft = coordinate
    elif coordinate_type == 'topright':
        rect.topright = coordinate
    elif coordinate_type == 'bottomleft':
        rect.bottomleft = coordinate
    elif coordinate_type == 'bottomright':
        rect.bottomright = coordinate
    elif coordinate_type == 'center':
        rect.center = coordinate
    else:
        rect.center = coordinate

    # 根据if_draw绘制对象
    if if_draw == True:
        screen.blit(surface, rect)

    # 根据ifreturn决定是否返回rect
    if ifreturn == True:
        return rect