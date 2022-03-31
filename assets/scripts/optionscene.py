""" 包含打开选项界面, 显示选项界面和关闭选项界面函数 """
import pygame

from sys import exit # 退出
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.settings import settings # 设置
from assets.scripts.scene_objects.optionscene_base_gameobject import optionscene_base_gameobject # 选项界面基本元素内容

pygame.init()


# 打开选项界面
def open_optionscene(screen, x, y, open_optionscene_bool, show_optionscene_bool, max_i, anti_aliasing, language, display_mode, display_size):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制选项界面基本元素内容
    optionscene_base_gameobject(screen, x, y, screen_size, anti_aliasing, language, display_mode, display_size, ifopen_click = False)
    
    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        open_optionscene_bool, show_optionscene_bool = False, True
    else:
        max_i = max_i - settings('animation_speed') - 3 # 帧数为120
        open_optionscene_bool, show_optionscene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    return open_optionscene_bool, show_optionscene_bool, max_i, anti_aliasing, language, display_mode, display_size


# 显示选项界面
def show_optionscene(screen, x, y, show_optionscene_bool, close_optionscene_bool, anti_aliasing, language, display_mode, display_size):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 绘制选项界面基本元素内容
    back_button_bool, anti_aliasing_left_bool, anti_aliasing_right_bool, restore_default_settings_bool, chinese_button_bool, english_button_bool, display_mode_left_bool, display_mode_right_bool = optionscene_base_gameobject(screen, x, y, screen_size, anti_aliasing, language, display_mode, display_size, ifopen_click = True)

    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN: # 返回主页
                show_optionscene_bool, close_optionscene_bool = False, True
            elif event.key == pygame.K_1: # 全屏
                show_optionscene_bool, close_optionscene_bool = True, False
                display_mode = 'full_screen'
            elif event.key == pygame.K_2: # 窗口模式
                show_optionscene_bool, close_optionscene_bool = True, False
                display_mode = 'window'
            elif event.key == pygame.K_3: # 当前窗口大小
                show_optionscene_bool, close_optionscene_bool = True, False
            elif event.key == pygame.K_4: # 下级窗口大小
                show_optionscene_bool, close_optionscene_bool = True, False
            elif event.key == pygame.K_5: # 抗锯齿开
                show_optionscene_bool, close_optionscene_bool = True, False
                anti_aliasing = True
            elif event.key == pygame.K_6: # 抗锯齿关
                show_optionscene_bool, close_optionscene_bool = True, False
                anti_aliasing = False
            elif event.key == pygame.K_7: # 默认设置
                show_optionscene_bool, close_optionscene_bool = True, False
                display_mode = 'full_screen' # 显示模式默认设置
                anti_aliasing = True # 抗锯齿默认设置
            elif event.key == pygame.K_8: # 返回主页
                show_optionscene_bool, close_optionscene_bool = False, True
            elif event.key == pygame.K_9: # 语言变成中文
                show_optionscene_bool, close_optionscene_bool = True, False
                language = 'chinese'
            elif event.key == pygame.K_0: # 语言变成英文
                show_optionscene_bool, close_optionscene_bool = True, False
                language = 'english'
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and back_button_bool == True: # 返回主页
                show_optionscene_bool, close_optionscene_bool = False, True
            elif event.button == 1 and display_mode_left_bool == True: # 左边调整显示模式
                show_optionscene_bool, close_optionscene_bool = True, False
                # 根据条件改变显示模式
                if display_mode == 'full_screen':
                    display_mode = 'window'
                elif display_mode == 'window':
                    display_mode = 'full_screen'
            elif event.button == 1 and display_mode_right_bool == True: # 右边调整显示模式
                show_optionscene_bool, close_optionscene_bool = True, False
                # 根据条件改变显示模式
                if display_mode == 'full_screen':
                    display_mode = 'window'
                elif display_mode == 'window':
                    display_mode = 'full_screen'
            elif event.button == 1 and anti_aliasing_left_bool == True: # 左边调整抗锯齿
                show_optionscene_bool, close_optionscene_bool = True, False
                # 根据条件关闭是否打开抗锯齿
                if anti_aliasing == True:
                    anti_aliasing = False
                elif anti_aliasing == False:
                    anti_aliasing = True
            elif event.button == 1 and anti_aliasing_right_bool == True: # 右边调整抗锯齿
                show_optionscene_bool, close_optionscene_bool = True, False
                # 根据条件关闭是否打开抗锯齿
                if anti_aliasing == True:
                    anti_aliasing = False
                elif anti_aliasing == False:
                    anti_aliasing = True
            elif event.button == 1 and chinese_button_bool == True: # 中文按钮
                show_optionscene_bool, close_optionscene_bool = True, False
                language = 'chinese'
            elif event.button == 1 and english_button_bool == True: # 英文按钮
                show_optionscene_bool, close_optionscene_bool = True, False
                language = 'english'
            elif event.button == 1 and restore_default_settings_bool == True: # 恢复默认设置
                show_optionscene_bool, close_optionscene_bool = True, False
                display_mode = 'full_screen' # 显示模式默认设置
                anti_aliasing = True # 抗锯齿默认设置
            else:
                show_optionscene_bool, close_optionscene_bool = True, False

    return show_optionscene_bool, close_optionscene_bool, anti_aliasing, language, display_mode, display_size


# 关闭选项界面
def close_optionscene(screen, x, y, close_optionscene_bool, open_homescene_bool, min_i, anti_aliasing, language, display_mode, display_size):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制选项界面基本元素内容
    optionscene_base_gameobject(screen, x, y, screen_size, anti_aliasing, language, display_mode, display_size, ifopen_click = False)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        close_optionscene_bool, open_homescene_bool = False, True
    else:
        min_i = min_i + settings('animation_speed') + 3 # 帧数为120
        close_optionscene_bool, open_homescene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_optionscene_bool, open_homescene_bool, min_i, anti_aliasing, language, display_mode, display_size