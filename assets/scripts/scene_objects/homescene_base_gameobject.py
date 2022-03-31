""" 包含主页基本元素内容函数 """
from assets.scripts.support.button import button # 按钮
from assets.scripts.support.game_object import game_object # 游戏对象


# 绘制主页的基本元素内容(应用于打开主页, 显示主页和关闭主页)
def homescene_base_gameobject(screen, x, y, screen_size, language, runs_number, ifopen_click = False):
    # 初始化开始游戏按钮
    if language == 'chinese':
        if runs_number == 0:
            start_button_text = '开始新旅途'
        else:
            start_button_text = '返回旅途'
    elif language == 'english':
        if runs_number == 0:
            start_button_text = 'Start a New Journey'
        else:
            start_button_text = 'Return the Journey'
    start_button_text_size = 25
    start_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2)
    start_button_diamond_side_length = 300

    # 初始化章节按钮
    if language == 'chinese':
        level_button_text = '章节'
    elif language == 'english':
        level_button_text = 'chapters'
    level_button_text_size = 25
    level_button_center_coordinate = (screen_size[0]/2+250, screen_size[1]/2)
    level_button_diamond_side_length = 200

    # 初始化选项按钮
    if language == 'chinese':
        options_button_text = '选项'
    elif language == 'english':
        options_button_text = 'options'
    options_button_text_size = 25
    options_button_center_coordinate = (screen_size[0]/2-250, screen_size[1]/2)
    options_button_diamond_side_length = 200

    # 初始化关于按钮
    if language == 'chinese':
        about_button_text = '关于'
    elif language == 'english':
        about_button_text = 'about'
    about_button_text_size = 20
    about_button_center_coordinate = (screen_size[0]/2-150, screen_size[1]/2-50)
    about_button_diamond_side_length = 100

    # 初始化退出按钮
    if language == 'chinese':
        exit_button_text = '退出'
    elif language == 'english':
        exit_button_text = 'exit'
    exit_button_text_size = 20
    exit_button_center_coordinate = (screen_size[0]/2+150, screen_size[1]/2+50)
    exit_button_diamond_side_length = 100

    # 初始化新游戏按钮
    if language == 'chinese':
        new_button_text = '新旅途'
    elif language == 'english':
        new_button_text = 'new'
    new_button_text_size = 20
    new_button_center_coordnate = (screen_size[0]-75, 75)
    new_button_diamond_side_length = 100

    # 绘制按钮(根据运行次数绘制新游戏按钮)
    if language == 'chinese':
        start_button_bool = button(screen, x, y, start_button_text, start_button_text_size, start_button_center_coordinate, start_button_diamond_side_length, ifopen_click = ifopen_click)
        level_button_bool = button(screen, x, y, level_button_text, level_button_text_size, level_button_center_coordinate, level_button_diamond_side_length, ifopen_click = ifopen_click)
        options_button_bool = button(screen, x, y, options_button_text, options_button_text_size, options_button_center_coordinate, options_button_diamond_side_length, ifopen_click = ifopen_click)
        about_button_bool = button(screen, x, y, about_button_text, about_button_text_size, about_button_center_coordinate, about_button_diamond_side_length, ifopen_click = ifopen_click)
        exit_button_bool = button(screen, x, y, exit_button_text, exit_button_text_size, exit_button_center_coordinate, exit_button_diamond_side_length, ifopen_click = ifopen_click)
        if runs_number != 0:
            new_button_bool = button(screen, x, y, new_button_text, new_button_text_size, new_button_center_coordnate, new_button_diamond_side_length, ifopen_click = ifopen_click)
        else:
            new_button_bool = False
    elif language == 'english':
        start_button_bool = button(screen, x, y, start_button_text, start_button_text_size, start_button_center_coordinate, start_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        level_button_bool = button(screen, x, y, level_button_text, level_button_text_size, level_button_center_coordinate, level_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        options_button_bool = button(screen, x, y, options_button_text, options_button_text_size, options_button_center_coordinate, options_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        about_button_bool = button(screen, x, y, about_button_text, about_button_text_size, about_button_center_coordinate, about_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        exit_button_bool = button(screen, x, y, exit_button_text, exit_button_text_size, exit_button_center_coordinate, exit_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        if runs_number != 0:
            new_button_bool = button(screen, x, y, new_button_text, new_button_text_size, new_button_center_coordnate, new_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        else:
            new_button_bool = False

    # 根据是否打开点击处理而返回按钮点击标志
    if ifopen_click == True:
        return start_button_bool, level_button_bool, options_button_bool, about_button_bool, exit_button_bool, new_button_bool