""" 包含打开标题界面, 显示标题界面和关闭标题界面函数 """
import pygame

from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.settings import settings # 设置
from assets.scripts.scene_objects.titlescene_base_gameobject import titlescene_base_gameobject # 标题界面基本元素内容

pygame.init()


# 打开标题界面
def open_titlescene(screen, open_titlescene_bool, show_titlescene_bool, max_i, show_homescene_bool):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    if_exit_game, if_exit_scene = exit_game(ifget_esc = False, ifget_enter = True)

    # 绘制标题界面基本元素内容
    titlescene_base_gameobject(screen, screen_size)
    
    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        open_titlescene_bool, show_titlescene_bool, show_homescene_bool = False, True, False
    elif if_exit_scene == True: # 如果按enter键, 则跳过当前场景
        max_i = 255
        open_titlescene_bool, show_titlescene_bool, show_homescene_bool = False, False, True
    else:
        max_i = max_i - 2 # 帧数为120
        open_titlescene_bool, show_titlescene_bool, show_homescene_bool = True, False, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    return open_titlescene_bool, show_titlescene_bool, max_i, show_homescene_bool


# 显示标题界面
def show_titlescene(screen, show_titlescene_bool, close_titlescene_bool, i, show_homescene_bool):
    # 加载屏幕大小和显示时间, 单位秒
    screen_size = settings('screen_size')
    time = 1 # 帧数为120

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    if_exit_game, if_exit_scene = exit_game(ifget_esc = False, ifget_enter = True)

    # 绘制标题界面基本元素内容
    titlescene_base_gameobject(screen, screen_size)

    # 更新计数器
    if i >= settings('fps') * time:
        i = 0
        show_titlescene_bool, close_titlescene_bool, show_homescene_bool = False, True, False
    elif if_exit_scene == True: # 如果按enter键, 则跳过当前场景
        i = 0
        show_titlescene_bool, close_titlescene_bool, show_homescene_bool = False, False, True
    else:
        i = i + 1 # 帧数为120
        show_titlescene_bool, close_titlescene_bool, show_homescene_bool = True, False, False

    return show_titlescene_bool, close_titlescene_bool, i, show_homescene_bool


# 关闭标题界面
def close_titlescene(screen, close_titlescene_bool, open_homescene_bool, min_i, show_homescene_bool):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    if_exit_game, if_exit_scene = exit_game(ifget_esc = False, ifget_enter = True)

    # 绘制标题界面基本元素内容
    titlescene_base_gameobject(screen, screen_size)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        close_titlescene_bool, open_homescene_bool, show_homescene_bool = False, True, False
    elif if_exit_scene == True: # 如果按enter键, 则跳过当前场景
        min_i = 0
        close_titlescene_bool, open_homescene_bool, show_homescene_bool = False, False, True
    else:
        min_i = min_i + 3 # 帧数为120
        close_titlescene_bool, open_homescene_bool, show_homescene_bool = True, False, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_titlescene_bool, open_homescene_bool, min_i, show_homescene_bool