""" 包含选项界面基本元素内容函数 """
import pygame

from assets.scripts.support.button import button, options_button # 按钮
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 绘制选项界面的基本元素内容(应用于打开选项界面, 显示选项界面, 关闭选项界面)
def optionscene_base_gameobject(screen, x, y, screen_size, anti_aliasing, language, display_mode, display_size, ifopen_click = False):
    # 初始化返回主页按钮
    if language == 'chinese':
        back_button_text = '返回'
    elif language == 'english':
        back_button_text = 'BACK'
    back_button_text_size = 20
    back_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2)
    back_button_diamond_side_length = 100

    # 绘制显示模式消息和按钮
    if language == 'chinese':
        game_object(screen, size = 25, text = '显示模式', coordinate = (screen_size[0]/2-200, screen_size[1]/2-270), coordinate_type = 'left_centery')
    elif language == 'english':
        game_object(screen, size = 25, text = 'display mode', coordinate = (screen_size[0]/2-200, screen_size[1]/2-270), coordinate_type = 'left_centery', language = 'english')
    # 绘制显示模式左边和右边按钮
    display_mode_left_bool = options_button(screen, x, y, text = '<', size = 22, coordinate = (screen_size[0]/2+20, screen_size[1]/2-270), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese')
    display_mode_right_bool = options_button(screen, x, y, text = '>', size = 22, coordinate = (screen_size[0]/2+180, screen_size[1]/2-270), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese')
    # 绘制显示模式消息
    if display_mode == 'full_screen':
        if language == 'chinese':
            game_object(screen, size = 22, text = '全屏', coordinate = (screen_size[0]/2+100, screen_size[1]/2-270))
        elif language == 'english':
            game_object(screen, size = 22, text = 'full screen', coordinate = (screen_size[0]/2+100, screen_size[1]/2-270), language = 'english')
    elif display_mode == 'window':
        if language == 'chinese':
            game_object(screen, size = 22, text = '窗口模式', coordinate = (screen_size[0]/2+100, screen_size[1]/2-270))
        elif language == 'english':
            game_object(screen, size = 22, text = 'window', coordinate = (screen_size[0]/2+100, screen_size[1]/2-270), language = 'english')

    # 绘制窗口大小消息和按钮
    # 根据显示模式决定是否允许改变窗口大小
    if display_mode == 'full_screen': # 不允许
        if language == 'chinese':
            game_object(screen, size = 25, text = '窗口大小', coordinate = (screen_size[0]/2-200, screen_size[1]/2-220), coordinate_type = 'left_centery', change_color = True, new_color = settings('button_above_color'))
        elif language == 'english':
            game_object(screen, size = 25, text = 'window size', coordinate = (screen_size[0]/2-200, screen_size[1]/2-220), coordinate_type = 'left_centery', change_color = True, new_color = settings('button_above_color'), language = 'english')
        # 绘制窗口大小左边和右边按钮
        game_object(screen, size = 22, text = '<', coordinate = (screen_size[0]/2+20, screen_size[1]/2-220), coordinate_type = 'center', change_color = True, new_color = settings('button_above_color'))
        game_object(screen, size = 22, text = '>', coordinate = (screen_size[0]/2+180, screen_size[1]/2-220), coordinate_type = 'center', change_color = True, new_color = settings('button_above_color'))
        screen_size_left_bool, screen_size_right_bool = False, False
        if display_size == 'MaxXxMaxY':
            game_object(screen, size = 22, text = str(settings('screen_size')[0]) + 'x' + str(settings('screen_size')[1]), coordinate = (screen_size[0]/2+100, screen_size[1]/2-220), change_color = True, new_color = settings('button_above_color'))
    elif display_mode == 'window': # 允许
        if language == 'chinese':
            game_object(screen, size = 25, text = '窗口大小', coordinate = (screen_size[0]/2-200, screen_size[1]/2-220), coordinate_type = 'left_centery')
        elif language == 'english':
            game_object(screen, size = 25, text = 'window size', coordinate = (screen_size[0]/2-200, screen_size[1]/2-220), coordinate_type = 'left_centery', language = 'english')
        # 绘制窗口大小左边和右边按钮
        screen_size_left_bool = options_button(screen, x, y, text = '<', size = 22, coordinate = (screen_size[0]/2+20, screen_size[1]/2-220), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese')
        screen_size_right_bool = options_button(screen, x, y, text = '>', size = 22, coordinate = (screen_size[0]/2+180, screen_size[1]/2-220), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese')
        if display_size == 'MaxXxMaxY':
            game_object(screen, size = 22, text = str(settings('screen_size')[0]) + 'x' + str(settings('screen_size')[1]), coordinate = (screen_size[0]/2+100, screen_size[1]/2-220))

    # 绘制抗锯齿消息和按钮
    if language == 'chinese':
        game_object(screen, size = 25, text = '抗锯齿', coordinate = (screen_size[0]/2-200, screen_size[1]/2-170), coordinate_type = 'left_centery')
    elif language == 'english':
        game_object(screen, size = 25, text = 'anti-aliasing ', coordinate = (screen_size[0]/2-200, screen_size[1]/2-170), coordinate_type = 'left_centery', language = 'english')
    # 绘制抗锯齿左边和右边按钮
    anti_aliasing_left_bool = options_button(screen, x, y, text = '<', size = 22, coordinate = (screen_size[0]/2+20, screen_size[1]/2-170), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese') 
    anti_aliasing_right_bool = options_button(screen, x, y, text = '>', size = 22, coordinate = (screen_size[0]/2+180, screen_size[1]/2-170), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese')
    # 绘制抗锯齿消息
    if anti_aliasing == True:
        if language == 'chinese':
            game_object(screen, size = 22, text = '开', coordinate = (screen_size[0]/2+100, screen_size[1]/2-170))
        elif language == 'english':
            game_object(screen, size = 22, text = 'ON', coordinate = (screen_size[0]/2+100, screen_size[1]/2-170), language = 'english')
    elif anti_aliasing == False:
        if language == 'chinese':
            game_object(screen, size = 22, text = '关', coordinate = (screen_size[0]/2+100, screen_size[1]/2-170))
        elif language == 'english':
            game_object(screen, size = 22, text = 'OFF', coordinate = (screen_size[0]/2+100, screen_size[1]/2-170), language = 'english')

    # 绘制恢复默认设置按钮
    if language == 'chinese':
        restore_default_settings_bool = options_button(screen, x, y, text = '恢复默认设置', size = 22, coordinate = (screen_size[0]/2, screen_size[1]/2-100), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese')
    elif language == 'english':
        restore_default_settings_bool = options_button(screen, x, y, text = 'restore default settings', size = 22, coordinate = (screen_size[0]/2, screen_size[1]/2-100), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'english')

    # 绘制分界线和绘制返回按钮
    pygame.draw.line(screen, settings('text_color'), (screen_size[0]/2-200, screen_size[1]/2), (screen_size[0]/2+200, screen_size[1]/2), 2)
    if language == 'chinese':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click)
    elif language == 'english':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')

    # 语言消息绘制中文和英文按钮
    if language == 'chinese':
        game_object(screen, size = 25, text = '用户界面语言', coordinate = (screen_size[0]/2, screen_size[1]/2+120), coordinate_type = 'center')
    elif language == 'english':
        game_object(screen, size = 25, text = 'user interface language', coordinate = (screen_size[0]/2, screen_size[1]/2+120), coordinate_type = 'center', language = 'english')
    # 绘制中文和英文按钮
    chinese_button_bool = options_button(screen, x, y, text = '简体中文', size = 22, coordinate = (screen_size[0]/2, screen_size[1]/2+200), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'chinese')
    english_button_bool = options_button(screen, x, y, text = 'English', size = 22, coordinate = (screen_size[0]/2, screen_size[1]/2+250), draw_types = 1, ifopen_click = ifopen_click, coordinate_type = 'center', language = 'english')
    # 绘制语言消息
    if language == 'chinese':
        game_object(screen, size = 22, text = '>', coordinate = (screen_size[0]/2-75, screen_size[1]/2+200))
    elif language == 'english':
        game_object(screen, size = 22, text = '>', coordinate = (screen_size[0]/2-75, screen_size[1]/2+250))

    # 根据是否打开点击处理而返回按钮点击标志
    if ifopen_click == True:
        return back_button_bool, anti_aliasing_left_bool, anti_aliasing_right_bool, restore_default_settings_bool, chinese_button_bool, english_button_bool, display_mode_left_bool, display_mode_right_bool