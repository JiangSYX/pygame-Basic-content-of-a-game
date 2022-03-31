""" 文字游戏-基因突变 """

import pygame

from sys import exit # 退出
from random import randint, uniform # 随机数
from math import sqrt, asin, pi # 开方, 反正弦, 圆周率

""" 开始导入场景支持函数和场景基本元素内容函数 """

# 支持函数
from assets.scripts.support.bullets_collision import bullets_collision # 子弹碰撞检测
from assets.scripts.support.button import button, options_button # 按钮
from assets.scripts.support.create_data import create_data # 创建数据
from assets.scripts.support.detection_position import detection_position # 检测位置
from assets.scripts.support.draw_menu import draw_menu # 绘制菜单
from assets.scripts.support.draw_died import draw_died # 绘制死亡界面
from assets.scripts.support.draw_objects import draw_objects # 绘制游戏对象
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.game_ui import game_UI # 游戏UI
from assets.scripts.support.handle_data import save_data # 保存数据
from assets.scripts.support.neural_network import NeuralNetwork # 神经网络类
from assets.scripts.support.pills import draw_pills # 绘制止痛药
from assets.scripts.support.zombies import draw_zombies # 绘制丧尸
from assets.scripts.support.player import player # 玩家角色
from assets.scripts.support.process_collision import collision_detection, ifopen_collision_detection # 碰撞检测, 是否打开碰撞检测
from assets.scripts.support.process_file import read_file, write_file # 读取文件, 写入文件
from assets.scripts.support.record_sign import record_sign # 记录标志
from assets.scripts.support.settings import settings # 设置
from assets.scripts.support.shooting import text_sound_shoot, draw_bullets, shoot # 开枪射击的文字化声音, 开枪射击

# 界面的基本元素内容的函数
from assets.scripts.scene_objects.startscene_base_gameobject import startscene_base_gameobject # 开始界面基础元素内容
from assets.scripts.scene_objects.titlescene_base_gameobject import titlescene_base_gameobject # 标题界面基本元素内容
from assets.scripts.scene_objects.homescene_base_gameobject import homescene_base_gameobject # 主页基本元素内容
from assets.scripts.scene_objects.optionscene_base_gameobject import optionscene_base_gameobject # 选项界面基本元素内容
from assets.scripts.scene_objects.levelscene_base_gameobject import levelscene_base_gameobject # 章节界面基本元素内容
from assets.scripts.scene_objects.exitscene_base_gameobject import exitscene_base_gameobject # 退出界面基本元素内容
from assets.scripts.scene_objects.aboutscene_base_gameobject import aboutscene_base_gameobject # 关于界面基础元素内容
from assets.scripts.scene_objects.newscene_base_gameobject import newscene_base_gameobject # 新旅途界面基础元素内容
from assets.scripts.scene_objects.loadscene_base_gameobject import loadscene_base_gameobject # 加载界面基础元素内容

""" 开始导入场景函数, 往上为场景支持函数, 往下为场景函数 """

# 打开, 显示, 关闭非游戏内容的界面(主页和关于界面特殊)
from assets.scripts.startscene import open_startscene, show_startscene, close_startscene # 打开开始界面, 显示开始界面和关闭开始界面
from assets.scripts.titlescene import open_titlescene, show_titlescene, close_titlescene # 打开标题界面, 显示标题界面和关闭标题界面
from assets.scripts.homescene import open_homescene, show_homescene, close_homescene # 打开主页, 显示主页和关闭主页
from assets.scripts.optionscene import open_optionscene, show_optionscene, close_optionscene # 打开选项界面, 显示选项界面和关闭选项界面
from assets.scripts.levelscene import open_levelscene, show_levelscene, close_levelscene # 打开章节界面, 显示章节界面和关闭章节界面
from assets.scripts.exitscene import open_exitscene, show_exitscene, close_exitscene # 打开退出界面, 显示退出界面和关闭退出界面
from assets.scripts.aboutscene import open_aboutscene, show_aboutscene, close_aboutscene # 打开关于界面, 显示关于界面和关闭关于界面
from assets.scripts.newscene import open_newscene, show_newscene, close_newscene # 打开新旅途界面, 显示新旅途界面和关闭新旅途界面
from assets.scripts.loadscene import open_loadscene, show_loadscene, close_loadscene # 打开加载界面, 显示加载界面和改变加载界面

# 绘制游戏场景
from assets.scripts.scene_1_village import scene_1_village # 第一个游戏场景--乡村
from assets.scripts.scene_2_highway import scene_2_highway # 第二个游戏场景--公路
from assets.scripts.scene_3_town import scene_3_town # 第三个游戏场景--小镇
from assets.scripts.scene_4_suburb import scene_4_suburb # 第四个游戏场景--郊区
from assets.scripts.scene_5_city import scene_5_city # 第五个游戏场景--城市
from assets.scripts.scene_6_trainstation import scene_6_trainstation # 第六个游戏场景--火车站
from assets.scripts.scene_7_refuge import scene_7_refuge # 第七个游戏场景--避难所

""" 开始调用函数并运行游戏, 主函数先加载游戏数据再加载场景 """

# 主程序
def main():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # pygame.mixer.init()

    pygame.display.set_caption(settings('name'))
    logo = pygame.image.load(settings('logo_addness'))
    pygame.display.set_icon(logo)
    fps = pygame.time.Clock()

    # 设置场景活跃状态
    open_startscene_bool, show_startscene_bool, close_startscene_bool = True, False, False # 打开开始界面, 显示开始界面和关闭开始界面
    open_titlescene_bool, show_titlescene_bool, close_titlescene_bool = False, False, False # 打开标题界面, 显示标题界面和关闭标题界面
    
    open_homescene_bool, show_homescene_bool = False, False # 打开主页, 显示主页
    close_homescene_to_optionscene_bool = False # 关闭主页到选项界面
    close_homescene_to_levelscene_bool = False # 关闭主页到章节界面
    close_homescene_to_exitscene_bool = False # 关闭主页到退出界面
    close_homescene_to_aboutscene_bool = False # 关闭主页到关于界面
    close_homescene_to_newscene_bool = False # 关闭主页到新旅途界面
    close_homescene_to_scene1_village_bool = False # 关闭主页到第一个游戏场景界面
    close_homescene_to_scene2_highway_bool = False # 关闭主页到第二个游戏场景界面
    close_homescene_to_scene3_town_bool = False # 关闭主页到第三个游戏场景界面
    close_homescene_to_scene4_suburb_bool = False # 关闭主页到第四个游戏场景界面
    close_homescene_to_scene5_city_bool = False # 关闭主页到第五个游戏场景界面
    close_homescene_to_scene6_trainstation_bool = False # 关闭主页到第六个游戏场景界面
    close_homescene_to_scene7_refuge_bool = False # 关闭主页到第七个游戏场景界面

    open_optionscene_bool, show_optionscene_bool, close_optionscene_bool = False, False, False # 打开选项界面, 显示选项界面和关闭选项界面
    open_levelscene_bool, show_levelscene_bool, close_levelscene_bool = False, False, False # 打开章节界面, 显示章节界面和关闭章节界面
    open_exitscene_bool, show_exitscene_bool, close_exitscene_bool = False, False, False # 打开退出界面, 显示退出界面和关闭退出界面
    open_aboutscene_bool, show_aboutscene_bool, close_aboutscene_bool = False, False, False # 打开关于界面, 显示关于界面和关闭关于界面
    open_newscene_bool, show_newscene_bool, close_newscene_bool = False, False, False # 打开新旅途界面, 显示新旅途界面和关闭新旅途界面
    open_loadscene_bool, show_loadscene_bool, close_loadscene_bool = False, False, False # 打开加载界面, 显示加载界面和改变加载界面

    scene_1_village_bool = False # 第一个游戏场景
    scene_2_highway_bool = False # 第二个游戏场景
    scene_3_town_bool = False # 第三个游戏场景
    scene_4_suburb_bool = False # 第四个游戏场景
    scene_5_city_bool = False # 第五个游戏场景
    scene_6_trainstation_bool = False # 第六个游戏场景
    scene_7_refuge_bool = False # 第七个游戏场景

    # 初始化游戏对象移动标志
    up_bool, down_bool, left_bool, right_bool = False, False, False, False

    # 初始化检测是否检测移动标志的标志
    move_sign_file = settings('move_sign_file')
    move_base_sign = settings('move_base_sign')
    move_sign = read_file(move_sign_file, base_data = move_base_sign)
    if_up, if_down, if_left, if_right = move_sign['if_up'], move_sign['if_down'], move_sign['if_left'], move_sign['if_right']

    # 初始化游戏对象的检测是否检测移动标志的标志
    chapter_1_objects_number = 19
    chapter_1_objects = {}
    for ids in range(1, chapter_1_objects_number + 1):
        chapter_1_objects[ids] = {'if_up': if_up, 'if_down': if_down, 'if_left': if_left, 'if_right': if_right}

    chapter_2_objects_number = 1
    chapter_2_objects = {}
    for ids in range(1, chapter_2_objects_number + 1):
        chapter_2_objects[ids] = {'if_up': if_up, 'if_down': if_down, 'if_left': if_left, 'if_right': if_right}

    chapter_3_objects_number = 1
    chapter_3_objects = {}
    for ids in range(1, chapter_3_objects_number + 1):
        chapter_3_objects[ids] = {'if_up': if_up, 'if_down': if_down, 'if_left': if_left, 'if_right': if_right}
    
    chapter_4_objects_number = 1
    chapter_4_objects = {}
    for ids in range(1, chapter_4_objects_number + 1):
        chapter_4_objects[ids] = {'if_up': if_up, 'if_down': if_down, 'if_left': if_left, 'if_right': if_right}

    chapter_5_objects_number = 1
    chapter_5_objects = {}
    for ids in range(1, chapter_5_objects_number + 1):
        chapter_5_objects[ids] = {'if_up': if_up, 'if_down': if_down, 'if_left': if_left, 'if_right': if_right}

    chapter_6_objects_number = 1
    chapter_6_objects = {}
    for ids in range(1, chapter_6_objects_number + 1):
        chapter_6_objects[ids] = {'if_up': if_up, 'if_down': if_down, 'if_left': if_left, 'if_right': if_right}

    chapter_7_objects_number = 1
    chapter_7_objects = {}
    for ids in range(1, chapter_7_objects_number + 1):
        chapter_7_objects[ids] = {'if_up': if_up, 'if_down': if_down, 'if_left': if_left, 'if_right': if_right}

    # 初始化键盘是否按下标志
    enter_key = {'enter_w': False, 'enter_s': False, 'enter_a': False, 'enter_d': False}

    # 初始化是否打开倍镜
    if_open_agnifying = False

    # 初始化是否射击
    if_shoot = False

    # 初始化加载界面是否应该获取时间, 是否停止获取随机数和基础时间以及信息id
    loadscene_get_time, if_get_randint, time, message_id = True, True, None, None

    # 初始化是否读取主坐标
    read_main_coordinate = False

    # 初始化是否写入临时文件和是否按下第一章节按钮
    write_temporary_file, enter_chapter_1 = True, False

    # 初始化菜单按钮标志
    home_button_bool, backgame_button_bool, menuexit_button_bool = False, False, False

    # 初始化是否绘制章节名
    draw_chapter_name = False

    # 初始化是否绘制菜单界面
    draw_menuscene = False

    # 初始化是否绘制子弹
    if_draw_bullets = False

    # 初始化角色相对于主坐标移动的相对差值(作用于游戏对象)
    x_dvalue, y_dvalue = 0, 0

    # 设置公共循环计算器
    i, min_i, max_i = 0, 0, 255

    # 初始化关于LSJX界面的表情包id
    first_emoticon, last_emoticon = 1, 50
    emoticon_id = randint(first_emoticon, last_emoticon)

    # 初始化死亡界面的透明度计数器
    died_i = 0

    # 初始化是否死亡
    if_died = False

    # 初始化子弹基础id
    bullets_id = 0

    # 初始化丧尸动作次数
    zombies_action = 0

    # 初始化子弹存储字典
    Bullets = {}

    # 初始化丧尸存储字典
    Zombies = {}

    # 初始化神经网络训练数据(如果数据不存在, 则创建新的数据)
    training_data = create_data()

    # 初始化神经网络
    neural_network = NeuralNetwork(settings('input_nodes'), settings('hidden_nodes'), settings('output_nodes'), settings('learning_rate'))

    # 初始化神经网络是否训练状态
    training_state_file = settings('training_state_file')
    training_base_state = settings('training_base_state')
    training_state = read_file(training_state_file, base_data = training_base_state)

    # 初始化神经网络迭代次数, 如果文件丢失, 则设置为0
    iteration_file = settings('iteration_file')
    base_iteration = settings('base_iteration')
    iteration = read_file(iteration_file, base_data = base_iteration) # 迭代次数

    # 初始化神经网络当前训练数据id, 如果文件丢失, 则设置为0
    data_id_file = settings('data_id_file')
    data_base_id = settings('data_base_id')
    data_id = read_file(data_id_file, base_data = data_base_id)

    # 初始化角色坐标
    player_coordinate = (settings('screen_size')[0]/2, settings('screen_size')[1]/2)

    # 初始化子弹坐标
    bullets_coordinate = (settings('screen_size')[0]/2, settings('screen_size')[1]/2)

    # 初始化游戏对象主坐标, 如果游戏主坐标文件丢失, 则坐标设置为屏幕中间(重新初始化坐标系)
    main_coordinate_file = settings('main_coordinate_file')
    base_coordinate = settings('base_coordinate')
    main_coordinate = read_file(main_coordinate_file, base_data = base_coordinate) # 游戏对象主坐标

    # 初始化角色生命值, 如果生命值文件丢失, 则角色生命值设置为最大(默认最大为100)
    player_health_file = settings('player_health_file')
    player_base_health = settings('player_base_health')
    player_health = read_file(player_health_file, base_data = player_base_health)

    # 初始化角色子弹数量, 如果子弹数量文件丢失, 则子弹数量设置为350
    bullets_number_file = settings('bullets_number_file')
    bullets_base_number = settings('bullets_base_number')
    bullets_number = read_file(bullets_number_file, base_data = bullets_base_number)

    # 初始化当前章节id, 如果章节id文件丢失, 则章节id设置为1(第一章节)
    chapter_id_file = settings('chapter_id_file')
    chapter_base_id = settings('chapter_base_id')
    chapter_id = read_file(chapter_id_file, base_data = chapter_base_id)

    # 初始化显示模式, 如果文件丢失, 则显示模式设置为全屏
    display_mode_file = settings('display_mode_file')
    display_base_mode = settings('display_base_mode')
    display_mode = read_file(display_mode_file, base_data = display_base_mode)

    # 初始化是否打开抗锯齿, 如果文件丢失, 则设置为打开抗锯齿
    anti_aliasing_file = settings('anti_aliasing_file')
    anti_base_aliasing = settings('anti_base_aliasing')
    anti_aliasing = read_file(anti_aliasing_file, base_data = anti_base_aliasing)

    # 初始化语言, 如果语言文件丢失, 则设置为中文
    language_file = settings('language_file')
    language_base = settings('language_base')
    language = read_file(language_file, base_data = language_base)

    # 初始化屏幕大小, 如果文件丢失, 则设置为'MaxXxMaxY',此时为全屏模式. 其他情况为(例)1200x800
    display_size_file = settings('display_size_file')
    display_base_size = settings('display_base_size')
    display_size = read_file(display_size_file, base_data = display_base_size)

    # 初始化运行次数, 如果文件丢失, 则设置为0
    runs_number_file = settings('runs_number_file')
    runs_base_number = settings('runs_base_number')
    runs_number = read_file(runs_number_file, base_data = runs_base_number)

    # 初始化止痛药字典
    pills_file = settings('pills_file')
    pills_base_dictionaries = settings('pills_base_dictionaries')
    Pills = read_file(pills_file, base_data = pills_base_dictionaries)

    # 初始化丧尸字典
    zombies_file = settings('zombies_file')
    zombies_base_dictionaries = settings('zombies_base_dictionaries')
    Zombies = read_file(zombies_file, base_data = zombies_base_dictionaries)

    # 初始化是否绘制血条
    draw_blood_strip_file = settings('draw_blood_strip_file')
    base_draw_blood_strip = settings('base_draw_blood_strip')
    draw_blood_strip = read_file(draw_blood_strip_file, base_data = base_draw_blood_strip)


    # 开始游戏主循环(主坐标不参与循环)
    while True:
        # 更改显示模式
        if display_mode == 'full_screen': # 全屏
            screen = pygame.display.set_mode(settings('screen_size'), pygame.FULLSCREEN)
        elif display_mode == 'window': # 窗口模式
            screen = pygame.display.set_mode(settings('screen_size'))

        # 实时保存游戏数据
        move_sign['if_up'], move_sign['if_down'], move_sign['if_left'], move_sign['if_right'] = if_up, if_down, if_left, if_right
        save_data(chapter_id = chapter_id, runs_number = runs_number, 
                  anti_aliasing = anti_aliasing, language = language, display_mode = display_mode, display_size = display_size, 
                  player_health = int(player_health), bullets_number = int(bullets_number), move_sign = move_sign, 
                  Pills = Pills, Zombies = Zombies, 
                  iteration = iteration, training_state = training_state, data_id = data_id, 
                  draw_blood_strip = draw_blood_strip)

        # 获取鼠标位置
        x, y = pygame.mouse.get_pos()

        # 重新读取当前主坐标
        if if_died == True:
            main_coordinate = read_file(settings('main_coordinate_file'), base_data = None)
            if_died = False

        # 打开开始界面
        if open_startscene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制打开开始界面
            open_startscene_bool, show_startscene_bool, max_i, show_titlescene_bool = open_startscene(screen, open_startscene_bool, show_startscene_bool, max_i, show_titlescene_bool)

        # 显示开始界面
        elif show_startscene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制显示开始界面
            show_startscene_bool, close_startscene_bool, i, show_titlescene_bool = show_startscene(screen, show_startscene_bool, close_startscene_bool, i, show_titlescene_bool)

        # 关闭开始界面
        elif close_startscene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭开始界面
            close_startscene_bool, open_titlescene_bool, min_i, show_titlescene_bool = close_startscene(screen, close_startscene_bool, open_titlescene_bool, min_i, show_titlescene_bool)

        
        # 打开标题界面
        elif open_titlescene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制打开标题界面
            open_titlescene_bool, show_titlescene_bool, max_i, show_homescene_bool = open_titlescene(screen, open_titlescene_bool, show_titlescene_bool, max_i, show_homescene_bool)

        # 显示标题界面
        elif show_titlescene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制显示标题界面
            show_titlescene_bool, close_titlescene_bool, i, show_homescene_bool = show_titlescene(screen, show_titlescene_bool, close_titlescene_bool, i, show_homescene_bool)

        # 关闭标题界面
        elif close_titlescene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭标题界面
            close_titlescene_bool, open_homescene_bool, min_i, show_homescene_bool = close_titlescene(screen, close_titlescene_bool, open_homescene_bool, min_i, show_homescene_bool)


        # 打开主页
        elif open_homescene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制打开主页界面
            open_homescene_bool, show_homescene_bool, max_i, language, runs_number = open_homescene(screen, x, y, open_homescene_bool, show_homescene_bool, max_i, language, runs_number)

        # 显示主页
        elif show_homescene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制显示主页界面
            show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool, language, runs_number, chapter_id = show_homescene(
                screen, x, y, show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool, language, runs_number, chapter_id)

        # 关闭主页到选项界面
        elif close_homescene_to_optionscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭主页界面
            close_homescene_to_optionscene_bool, open_optionscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_optionscene_bool, open_optionscene_bool, min_i, language, runs_number)

        # 关闭主页到章节界面
        elif close_homescene_to_levelscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭主页界面
            close_homescene_to_levelscene_bool, open_levelscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_levelscene_bool, open_levelscene_bool, min_i, language, runs_number)

        # 关闭主页到退出界面
        elif close_homescene_to_exitscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭主页界面
            close_homescene_to_exitscene_bool, open_exitscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_exitscene_bool, open_exitscene_bool, min_i, language, runs_number)

        # 关闭主页到关于界面
        elif close_homescene_to_aboutscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            emoticon_id = randint(first_emoticon, last_emoticon) # 更新表情包id
            # 绘制关闭主页界面
            close_homescene_to_aboutscene_bool, open_aboutscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_aboutscene_bool, open_aboutscene_bool, min_i, language, runs_number)

        # 关闭主页到新旅途界面
        elif close_homescene_to_newscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭主页界面
            close_homescene_to_newscene_bool, open_newscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_newscene_bool, open_newscene_bool, min_i, language, runs_number)

        # 关闭主页到第一个游戏场景界面
        elif close_homescene_to_scene1_village_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭主页界面
            close_homescene_to_scene1_village_bool, open_loadscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_scene1_village_bool, open_loadscene_bool, min_i, language, runs_number)

        # 关闭主页到第二个游戏场景界面
        elif close_homescene_to_scene2_highway_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭主页界面
            close_homescene_to_scene2_highway_bool, open_loadscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_scene2_highway_bool, open_loadscene_bool, min_i, language, runs_number)

        # 关闭主页到第三个游戏场景界面
        elif close_homescene_to_scene3_town_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭主页界面
            close_homescene_to_scene3_town_bool, open_loadscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_scene3_town_bool, open_loadscene_bool, min_i, language, runs_number)

        # 关闭主页到第四个游戏场景界面
        elif close_homescene_to_scene4_suburb_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭主页界面
            close_homescene_to_scene4_suburb_bool, open_loadscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_scene4_suburb_bool, open_loadscene_bool, min_i, language, runs_number)

        # 关闭主页到第五个游戏场景界面
        elif close_homescene_to_scene5_city_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭主页界面
            close_homescene_to_scene5_city_bool, open_loadscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_scene5_city_bool, open_loadscene_bool, min_i, language, runs_number)

        # 关闭主页到第六个游戏场景界面
        elif close_homescene_to_scene6_trainstation_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭主页界面
            close_homescene_to_scene6_trainstation_bool, open_loadscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_scene6_trainstation_bool, open_loadscene_bool, min_i, language, runs_number)

        # 关闭主页到第七个游戏场景界面
        elif close_homescene_to_scene7_refuge_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭主页界面
            close_homescene_to_scene7_refuge_bool, open_loadscene_bool, min_i, language, runs_number = close_homescene(screen, x, y, close_homescene_to_scene7_refuge_bool, open_loadscene_bool, min_i, language, runs_number)


        # 打开选项界面
        elif open_optionscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制打开选项界面
            open_optionscene_bool, show_optionscene_bool, max_i, anti_aliasing, language, display_mode, display_size = open_optionscene(screen, x, y, open_optionscene_bool, show_optionscene_bool, max_i, anti_aliasing, language, display_mode, display_size)

        # 显示选项界面
        elif show_optionscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制显示选项界面
            show_optionscene_bool, close_optionscene_bool, anti_aliasing, language, display_mode, display_size = show_optionscene(screen, x, y, show_optionscene_bool, close_optionscene_bool, anti_aliasing, language, display_mode, display_size)

        # 关闭选项界面
        elif close_optionscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭选项界面
            close_optionscene_bool, open_homescene_bool, min_i, anti_aliasing, language, display_mode, display_size = close_optionscene(screen, x, y, close_optionscene_bool, open_homescene_bool, min_i, anti_aliasing, language, display_mode, display_size)


        # 打开章节界面
        elif open_levelscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制打开章节界面
            open_levelscene_bool, show_levelscene_bool, max_i, chapter_id, language = open_levelscene(screen, x, y, open_levelscene_bool, show_levelscene_bool, max_i, chapter_id, language)

        # 显示章节界面
        elif show_levelscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制显示章节界面
            show_levelscene_bool, close_levelscene_bool, chapter_id, language, runs_number, read_main_coordinate, main_coordinate, x_dvalue, y_dvalue, write_temporary_file, enter_chapter_1, Pills, Zombies, zombies_action = show_levelscene(screen, x, y, show_levelscene_bool, close_levelscene_bool, chapter_id, language, runs_number, player_health, bullets_number, read_main_coordinate, x_dvalue, y_dvalue, write_temporary_file, enter_chapter_1, Pills, Zombies, zombies_action)

        # 关闭章节界面
        elif close_levelscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭章节界面
            close_levelscene_bool, open_homescene_bool, min_i, chapter_id, language = close_levelscene(screen, x, y, close_levelscene_bool, open_homescene_bool, min_i, chapter_id, language)


        # 打开退出界面
        elif open_exitscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制打开退出界面
            open_exitscene_bool, show_exitscene_bool, max_i, language = open_exitscene(screen, x, y, open_exitscene_bool, show_exitscene_bool, max_i, language)

        # 显示退出界面
        elif show_exitscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制显示退出界面
            show_exitscene_bool, close_exitscene_bool, language = show_exitscene(screen, x, y, show_exitscene_bool, close_exitscene_bool, language)

        # 关闭退出界面
        elif close_exitscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭退出界面
            close_exitscene_bool, open_homescene_bool, min_i, language = close_exitscene(screen, x, y, close_exitscene_bool, open_homescene_bool, min_i, language)


        # 打开关于界面
        elif open_aboutscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制打开关于界面
            open_aboutscene_bool, show_aboutscene_bool, max_i, language = open_aboutscene(screen, x, y, open_aboutscene_bool, show_aboutscene_bool, max_i, language, emoticon_id)

        # 显示关于界面
        elif show_aboutscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制显示关于界面
            show_aboutscene_bool, close_aboutscene_bool, language = show_aboutscene(screen, x, y, show_aboutscene_bool, close_aboutscene_bool, language, emoticon_id)

        # 关闭关于界面
        elif close_aboutscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭关于界面
            close_aboutscene_bool, open_homescene_bool, min_i, language = close_aboutscene(screen, x, y, close_aboutscene_bool, open_homescene_bool, min_i, language, emoticon_id)


        # 打开新旅途界面
        elif open_newscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制打开新旅途界面
            open_newscene_bool, show_newscene_bool, max_i, language = open_newscene(screen, x, y, open_newscene_bool, show_newscene_bool, max_i, language)

        # 显示新旅途界面
        elif show_newscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制显示新旅途界面
            show_newscene_bool, close_newscene_bool, language, runs_number, chapter_id, main_coordinate, read_main_coordinate, player_health, bullets_number, x_dvalue, y_dvalue, Pills, Zombies, iteration, data_id, training_state, neural_network = show_newscene(screen, x, y, show_newscene_bool, close_newscene_bool, language, runs_number, chapter_id, read_main_coordinate, player_health, bullets_number, x_dvalue, y_dvalue, Pills, Zombies, iteration, data_id, training_state, neural_network)

        # 关闭新旅途界面
        elif close_newscene_bool == True:
            pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制关闭新旅途界面
            close_newscene_bool, open_homescene_bool, min_i, language = close_newscene(screen, x, y, close_newscene_bool, open_homescene_bool, min_i, language)


        # 打开加载界面
        elif open_loadscene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制打开加载界面
            open_loadscene_bool, show_loadscene_bool, max_i, chapter_id, if_get_randint, message_id = open_loadscene(screen, open_loadscene_bool, show_loadscene_bool, max_i, chapter_id, if_get_randint, message_id)

        # 显示加载界面
        elif show_loadscene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制显示加载界面
            show_loadscene_bool, close_loadscene_bool, i, chapter_id, time, loadscene_get_time, open_homescene_bool, message_id = show_loadscene(screen, show_loadscene_bool, close_loadscene_bool, i, chapter_id, time, loadscene_get_time, open_homescene_bool, message_id)

        # 关闭加载界面
        elif close_loadscene_bool == True:
            pygame.mouse.set_visible(False) # 隐藏鼠标
            # 绘制关闭加载界面
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool, min_i, chapter_id, message_id = close_loadscene(
                screen, close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool, min_i, chapter_id, time, message_id)


        # 第一个场景-乡村
        elif scene_1_village_bool == True:
            if draw_menuscene == False:
                pygame.mouse.set_visible(False) # 隐藏鼠标(前提是不允许绘制菜单界面)
            elif draw_menuscene == True:
                pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制第一个场景-乡村
            scene_1_village_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_1_objects, draw_blood_strip = scene_1_village(
                screen, scene_1_village_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_1_objects, draw_blood_strip)


        # 第二个场景-公路
        elif scene_2_highway_bool == True:
            if draw_menuscene == False:
                pygame.mouse.set_visible(False) # 隐藏鼠标(前提是不允许绘制菜单界面)
            elif draw_menuscene == True:
                pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制第二个场景-公路
            scene_2_highway_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_2_objects, draw_blood_strip = scene_2_highway(
                screen, scene_2_highway_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_2_objects, draw_blood_strip)


        # 第三个场景-小镇
        elif scene_3_town_bool == True:
            if draw_menuscene == False:
                pygame.mouse.set_visible(False) # 隐藏鼠标(前提是不允许绘制菜单界面)
            elif draw_menuscene == True:
                pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制第三个场景-小镇
            scene_3_town_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_3_objects, draw_blood_strip = scene_3_town(
                screen, scene_3_town_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_3_objects, draw_blood_strip)


        # 第四个场景-郊区
        elif scene_4_suburb_bool == True:
            if draw_menuscene == False:
                pygame.mouse.set_visible(False) # 隐藏鼠标(前提是不允许绘制菜单界面)
            elif draw_menuscene == True:
                pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制第四个场景-郊区
            scene_4_suburb_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_4_objects, draw_blood_strip = scene_4_suburb(
                screen, scene_4_suburb_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_4_objects, draw_blood_strip)


        # 第五个场景-城市
        elif scene_5_city_bool == True:
            if draw_menuscene == False:
                pygame.mouse.set_visible(False) # 隐藏鼠标(前提是不允许绘制菜单界面)
            elif draw_menuscene == True:
                pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制第五个场景-城市
            scene_5_city_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_5_objects, draw_blood_strip = scene_5_city(
                screen, scene_5_city_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_5_objects, draw_blood_strip)


        # 第六个场景-火车站
        elif scene_6_trainstation_bool == True:
            if draw_menuscene == False:
                pygame.mouse.set_visible(False) # 隐藏鼠标(前提是不允许绘制菜单界面)
            elif draw_menuscene == True:
                pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制第六个场景-火车站
            scene_6_trainstation_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_6_objects, draw_blood_strip = scene_6_trainstation(
                screen, scene_6_trainstation_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_6_objects, draw_blood_strip)


        # 第七个场景-避难所
        elif scene_7_refuge_bool == True:
            if draw_menuscene == False:
                pygame.mouse.set_visible(False) # 隐藏鼠标(前提是不允许绘制菜单界面)
            elif draw_menuscene == True:
                pygame.mouse.set_visible(True) # 显示鼠标
            # 绘制第七个场景-避难所
            scene_7_refuge_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_7_objects, draw_blood_strip = scene_7_refuge(
                screen, scene_7_refuge_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_7_objects, draw_blood_strip)


        # 让最近绘制的屏幕可见
        pygame.display.flip()

        # 限制帧数
        fps.tick(settings('fps'))


# 开始运行程序
if __name__ == '__main__':
    main()