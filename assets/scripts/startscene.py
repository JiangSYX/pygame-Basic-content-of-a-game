""" 包含打开开始界面, 显示开始界面和关闭开始界面的函数 """
import pygame

from sys import exit # 退出
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.settings import settings # 设置
from assets.scripts.scene_objects.startscene_base_gameobject import startscene_base_gameobject # 开始界面基础元素内容

pygame.init()


# 打开开始界面
def open_startscene(screen, open_startscene_bool, show_startscene_bool, max_i, show_titlescene_bool):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    if_exit_game, if_exit_scene = exit_game(ifget_esc = True, ifget_enter = True)

    # 绘制开始界面基本元素内容
    startscene_base_gameobject(screen, screen_size)

    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        open_startscene_bool, show_startscene_bool, show_titlescene_bool = False, True, False
    elif if_exit_game == True: # 如果玩家按esc键, 则退出游戏
        exit()
    elif if_exit_scene == True: # 如果玩家按确定键, 则直接进入游戏
        max_i = 255
        open_startscene_bool, show_startscene_bool, show_titlescene_bool = False, False, True
    else:
        max_i = max_i - 2 # 帧数为120
        open_startscene_bool, show_startscene_bool, show_titlescene_bool = True, False, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return open_startscene_bool, show_startscene_bool, max_i, show_titlescene_bool


# 显示开始界面
def show_startscene(screen, show_startscene_bool, close_startscene_bool, i, show_titlescene_bool):
    # 加载屏幕大小和显示时间, 单位秒
    screen_size = settings('screen_size')
    time = 1 # 帧数为120

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    if_exit_game, if_exit_scene = exit_game(ifget_esc = True, ifget_enter = True)

    # 绘制开始界面基本元素内容
    startscene_base_gameobject(screen, screen_size)

    # 更新计数器
    if i >= settings('fps') * time:
        i = 0
        show_startscene_bool, close_startscene_bool, show_titlescene_bool = False, True, False
    elif if_exit_game == True: # 如果玩家按esc键, 则退出游戏
        exit()
    elif if_exit_scene == True: # 如果玩家按确定键, 则直接进入游戏
        i = 0
        show_startscene_bool, close_startscene_bool, show_titlescene_bool = False, False, True
    else:
        i = i + 1 # 帧数为120
        show_startscene_bool, close_startscene_bool, show_titlescene_bool = True, False, False

    return show_startscene_bool, close_startscene_bool, i, show_titlescene_bool


# 关闭开始界面
def close_startscene(screen, close_startscene_bool, open_homescene_bool, min_i, show_titlescene_bool):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    if_exit_game, if_exit_scene = exit_game(ifget_esc = True, ifget_enter = True)

    # 绘制开始界面基本元素内容
    startscene_base_gameobject(screen, screen_size)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        close_startscene_bool, open_homescene_bool, show_titlescene_bool = False, True, False
    elif if_exit_game == True: # 如果玩家按esc键, 则退出游戏
        exit()
    elif if_exit_scene == True: # 如果玩家按确定键, 则直接进入游戏
        min_i = 0
        close_startscene_bool, open_homescene_bool, show_titlescene_bool = False, False, True
    else:
        min_i = min_i + 3 # 帧数为120
        close_startscene_bool, open_homescene_bool, show_titlescene_bool = True, False, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_startscene_bool, open_homescene_bool, min_i, show_titlescene_bool