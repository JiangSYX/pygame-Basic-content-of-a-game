""" 包含打开关于界面, 显示关于界面和关闭关于界面函数 """
import pygame

from sys import exit # 退出
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.settings import settings # 设置
from assets.scripts.scene_objects.aboutscene_base_gameobject import aboutscene_base_gameobject # 关于界面基础元素内容

pygame.init()


# 打开关于界面
def open_aboutscene(screen, x, y, open_aboutscene_bool, show_aboutscene_bool, max_i, language, emoticon_id):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    aboutscene_base_gameobject(screen, x, y, screen_size, language, emoticon_id, ifopen_click = False)
    
    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        open_aboutscene_bool, show_aboutscene_bool = False, True
    else:
        max_i = max_i - settings('animation_speed') # 帧数为120
        open_aboutscene_bool, show_aboutscene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    return open_aboutscene_bool, show_aboutscene_bool, max_i, language


# 显示关于界面
def show_aboutscene(screen, x, y, show_aboutscene_bool, close_aboutscene_bool, language, emoticon_id):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 绘制关于界面基本元素内容
    back_button_bool = aboutscene_base_gameobject(screen, x, y, screen_size, language, emoticon_id, ifopen_click = True)

    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN: # 返回主页
                show_aboutscene_bool, close_aboutscene_bool = False, True
            elif event.key == pygame.K_1: # 返回主页
                show_aboutscene_bool, close_aboutscene_bool = False, True
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and back_button_bool == True: # 返回主页
                show_aboutscene_bool, close_aboutscene_bool = False, True
            else:
                show_aboutscene_bool, close_aboutscene_bool = True, False

    return show_aboutscene_bool, close_aboutscene_bool, language


# 关闭关于界面
def close_aboutscene(screen, x, y, close_aboutscene_bool, open_homescene_bool, min_i, language, emoticon_id):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    aboutscene_base_gameobject(screen, x, y, screen_size, language, emoticon_id, ifopen_click = False)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        close_aboutscene_bool, open_homescene_bool = False, True
    else:
        min_i = min_i + settings('animation_speed') # 帧数为120
        close_aboutscene_bool, open_homescene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_aboutscene_bool, open_homescene_bool, min_i, language