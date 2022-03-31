""" 包含章节界面基本元素内容函数 """
import pygame

from assets.scripts.support.button import button # 按钮
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 绘制章节界面的基本元素内容(应用于打开章节界面, 显示章节界面和关闭章节界面)
def levelscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = False, chapter_id = 0):
    # 初始化第一章节按钮
    if language == 'chinese':
        one_button_text = '乡村'
    elif language == 'english':
        one_button_text = 'village'
    one_button_text_size = 20
    one_button_center_coordinate = (screen_size[0]/2-300, screen_size[1]/2)
    one_button_diamond_side_length = 100

    # 初始化第二章节按钮
    if language == 'chinese':
        two_button_text = '公路'
    elif language == 'english':
        two_button_text = 'road'
    two_button_text_size = 20
    two_button_center_coordinate = (screen_size[0]/2-200, screen_size[1]/2)
    two_button_diamond_side_length = 100

    # 初始化第三章节按钮
    if language == 'chinese':
        three_button_text = '小镇'
    elif language == 'english':
        three_button_text = 'town'
    three_button_text_size = 20
    three_button_center_coordinate = (screen_size[0]/2-100, screen_size[1]/2)
    three_button_diamond_side_length = 100

    # 初始化第四章节按钮
    if language == 'chinese':
        four_button_text = '郊区'
    elif language == 'english':
        four_button_text = 'suburb'
    four_button_text_size = 20
    four_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2)
    four_button_diamond_side_length = 100

    # 初始化第五章节按钮
    if language == 'chinese':
        five_button_text = '城市'
    elif language == 'english':
        five_button_text = 'city'
    five_button_text_size = 20
    five_button_center_coordinate = (screen_size[0]/2+100, screen_size[1]/2)
    five_button_diamond_side_length = 100

    # 初始化第六章节按钮
    if language == 'chinese':
        six_button_text = '火车站'
    elif language == 'english':
        six_button_text = 'train'
    six_button_text_size = 20
    six_button_center_coordinate = (screen_size[0]/2+200, screen_size[1]/2)
    six_button_diamond_side_length = 100

    # 初始化第七章节按钮
    if language == 'chinese':
        seven_button_text = '避难所'
    elif language == 'english':
        seven_button_text = 'refuge'
    seven_button_text_size = 20
    seven_button_center_coordinate = (screen_size[0]/2+300, screen_size[1]/2)
    seven_button_diamond_side_length = 100

    # 初始化返回主页按钮
    if language == 'chinese':
        back_button_text = '返回'
    elif language == 'english':
        back_button_text = 'BACK'
    back_button_text_size = 20
    back_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2+100)
    back_button_diamond_side_length = 100

    # 显示当前章节数
    if language == 'chinese':
        if chapter_id == 1:
            chapter_name = '乡村'
            background_text = 'I'
        elif chapter_id == 2:
            chapter_name = '公路'
            background_text = 'II'
        elif chapter_id == 3:
            chapter_name = '小镇'
            background_text = 'III'
        elif chapter_id == 4:
            chapter_name = '郊区'
            background_text = 'IV'
        elif chapter_id == 5:
            chapter_name = '城市'
            background_text = 'V'
        elif chapter_id == 6:
            chapter_name = '火车站'
            background_text = 'VI'
        elif chapter_id == 7:
            chapter_name = '避难所'
            background_text = 'VII'

        # 绘制文字背景
        """
        game_object(screen, size = 700, text = background_text, coordinate = (screen_size[0]/2, screen_size[1]/2), language = 'english', change_color = True, new_color = settings('button_above_color'))
        surface = pygame.Surface(screen_size)
        surface.set_alpha(128)
        surface.fill(settings('background_color'))
        screen.blit(surface, (0, 0))
        """

        # 绘制当前章节名字
        game_object(screen, size = 50, text = chapter_name, coordinate = (screen_size[0]/2, screen_size[1]/2-125))
    
    elif language == 'english':
        if chapter_id == 1:
            chapter_name = 'Village'
            background_text = 'I'
        elif chapter_id == 2:
            chapter_name = 'Highway'
            background_text = 'II'
        elif chapter_id == 3:
            chapter_name = 'Town'
            background_text = 'III'
        elif chapter_id == 4:
            chapter_name = 'Suburb'
            background_text = 'IV'
        elif chapter_id == 5:
            chapter_name = 'City'
            background_text = 'V'
        elif chapter_id == 6:
            chapter_name = 'Train Station'
            background_text = 'VI'
        elif chapter_id == 7:
            chapter_name = 'Refuge'
            background_text = 'VII'

        # 绘制文字背景
        """
        game_object(screen, size = 700, text = background_text, coordinate = (screen_size[0]/2, screen_size[1]/2), language = 'english', change_color = True, new_color = settings('button_above_color'))
        surface = pygame.Surface(screen_size)
        surface.set_alpha(128)
        surface.fill(settings('background_color'))
        screen.blit(surface, (0, 0))
        """

        # 绘制当前章节名字
        game_object(screen, size = 50, text = chapter_name, coordinate = (screen_size[0]/2, screen_size[1]/2-125), language = 'english')

    # 绘制按钮
    if language == 'chinese':
        one_button_bool = button(screen, x, y, one_button_text, one_button_text_size, one_button_center_coordinate, one_button_diamond_side_length, ifopen_click = ifopen_click)
        two_button_bool = button(screen, x, y, two_button_text, two_button_text_size, two_button_center_coordinate, two_button_diamond_side_length, ifopen_click = ifopen_click)
        three_button_bool = button(screen, x, y, three_button_text, three_button_text_size, three_button_center_coordinate, three_button_diamond_side_length, ifopen_click = ifopen_click)
        four_button_bool = button(screen, x, y, four_button_text, four_button_text_size, four_button_center_coordinate, four_button_diamond_side_length, ifopen_click = ifopen_click)
        five_button_bool = button(screen, x, y, five_button_text, five_button_text_size, five_button_center_coordinate, five_button_diamond_side_length, ifopen_click = ifopen_click)
        six_button_bool = button(screen, x, y, six_button_text, six_button_text_size, six_button_center_coordinate, six_button_diamond_side_length, ifopen_click = ifopen_click)
        seven_button_bool = button(screen, x, y, seven_button_text, seven_button_text_size, seven_button_center_coordinate, seven_button_diamond_side_length, ifopen_click = ifopen_click)
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click)
    elif language == 'english':
        one_button_bool = button(screen, x, y, one_button_text, one_button_text_size, one_button_center_coordinate, one_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        two_button_bool = button(screen, x, y, two_button_text, two_button_text_size, two_button_center_coordinate, two_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        three_button_bool = button(screen, x, y, three_button_text, three_button_text_size, three_button_center_coordinate, three_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        four_button_bool = button(screen, x, y, four_button_text, four_button_text_size, four_button_center_coordinate, four_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        five_button_bool = button(screen, x, y, five_button_text, five_button_text_size, five_button_center_coordinate, five_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        six_button_bool = button(screen, x, y, six_button_text, six_button_text_size, six_button_center_coordinate, six_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        seven_button_bool = button(screen, x, y, seven_button_text, seven_button_text_size, seven_button_center_coordinate, seven_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')

    # 根据是否打开点击处理而返回按钮点击标志
    if ifopen_click == True:
        return one_button_bool, two_button_bool, three_button_bool, four_button_bool, five_button_bool, six_button_bool, seven_button_bool, back_button_bool, chapter_id