""" 包含打开章节界面, 显示章节界面和关闭章节界面函数 """
import pygame

from sys import exit # 退出
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.process_file import read_file, write_file # 读取文件, 写入文件
from assets.scripts.support.settings import settings # 设置
from assets.scripts.support.handle_data import save_data # 保存数据
from assets.scripts.scene_objects.levelscene_base_gameobject import levelscene_base_gameobject # 章节界面基本元素内容

pygame.init()


# 打开章节界面
def open_levelscene(screen, x, y, open_levelscene_bool, show_levelscene_bool, max_i, chapter_id, language):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    levelscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = False, chapter_id = chapter_id)
    
    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        open_levelscene_bool, show_levelscene_bool = False, True
    else:
        max_i = max_i - settings('animation_speed') - 3 # 帧数为120
        open_levelscene_bool, show_levelscene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    return open_levelscene_bool, show_levelscene_bool, max_i, chapter_id, language


# 显示章节界面
def show_levelscene(screen, x, y, show_levelscene_bool, close_levelscene_bool, chapter_id, language, runs_number, player_health, bullets_number, read_main_coordinate, x_dvalue, y_dvalue, write_temporary_file, enter_chapter_1, Pills, Zombies, zombies_action):
    # 加载屏幕大小, 读取主坐标(不保存和返回)
    screen_size = settings('screen_size')
    main_coordinate = read_file(settings('main_coordinate_file'), base_data = settings('base_coordinate'))

    # 存储临时章节id文件和主坐标文件
    if write_temporary_file == True:
        write_file(settings('temporary_chapter_id_file'), chapter_id)
        write_file(settings('temporary_main_coordinate_file'), main_coordinate)
        write_file(settings('temporary_Pills_file'), Pills)
        write_file(settings('temporary_Zombies_file'), Zombies)
        write_temporary_file = False

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 绘制章节界面基本元素内容
    one_button_bool, two_button_bool, three_button_bool, four_button_bool, five_button_bool, six_button_bool, seven_button_bool, back_button_bool, chapter_id = levelscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = True, chapter_id = chapter_id)

    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN: # 返回主页
                show_levelscene_bool, close_levelscene_bool = False, True
                write_temporary_file, enter_chapter_1 = True, False # 重新初始化是否存储临时文件标志和是否按下第一章节按钮
                # 如果玩家按其他按钮后但是又按回当前章节按钮, 则数据不变
                if chapter_id == read_file(settings('temporary_chapter_id_file'), base_data = None):
                    main_coordinate = read_file(settings('temporary_main_coordinate_file'), base_data = None)
                    Pills = read_file(settings('temporary_Pills_file'), base_data = None)
                    Zombies = read_file(settings('temporary_Zombies_file'), base_data = None)
                    zombies_action = 0
                    read_main_coordinate = True # 游戏重新读取主坐标
            elif event.key == pygame.K_1: # 第一章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 1:
                    chapter_id = 1
                    enter_chapter_1 = True # 玩家按下了第一章节按钮
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.key == pygame.K_2: # 第二章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 2:
                    chapter_id = 2
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.key == pygame.K_3: # 第三章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 3:
                    chapter_id = 3
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.key == pygame.K_4: # 第四章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 4:
                    chapter_id = 4
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.key == pygame.K_5: # 第五章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 5:
                    chapter_id = 5
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.key == pygame.K_6: # 第六章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 6:
                    chapter_id = 6
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.key == pygame.K_7: # 第七章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 7:
                    chapter_id = 7
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.key == pygame.K_8: # 返回主页
                show_levelscene_bool, close_levelscene_bool = False, True
                write_temporary_file, enter_chapter_1 = True, False # 重新初始化是否存储临时文件标志和是否按下第一章节按钮
                # 如果玩家按其他按钮后但是又按回当前章节按钮, 则数据不变
                if chapter_id == read_file(settings('temporary_chapter_id_file'), base_data = None):
                    main_coordinate = read_file(settings('temporary_main_coordinate_file'), base_data = None)
                    Pills = read_file(settings('temporary_Pills_file'), base_data = None)
                    Zombies = read_file(settings('temporary_Zombies_file'), base_data = None)
                    zombies_action = 0
                    read_main_coordinate = True # 游戏重新读取主坐标
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and back_button_bool == True: # 返回主页
                show_levelscene_bool, close_levelscene_bool = False, True
                write_temporary_file, enter_chapter_1 = True, False # 重新初始化是否存储临时文件标志和是否按下第一章节按钮
                # 如果玩家按其他按钮后但是又按回当前章节按钮, 则数据不变
                if chapter_id == read_file(settings('temporary_chapter_id_file'), base_data = None):
                    main_coordinate = read_file(settings('temporary_main_coordinate_file'), base_data = None)
                    Pills = read_file(settings('temporary_Pills_file'), base_data = None)
                    Zombies = read_file(settings('temporary_Zombies_file'), base_data = None)
                    zombies_action = 0
                    read_main_coordinate = True # 游戏重新读取主坐标
            elif event.button == 1 and one_button_bool == True: # 第一章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 1:
                    chapter_id = 1
                    enter_chapter_1 = True # 玩家按下了第一章节按钮
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.button == 1 and two_button_bool == True: # 第二章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 2:
                    chapter_id = 2
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.button == 1 and three_button_bool == True: # 第三章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 3:
                    chapter_id = 3
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.button == 1 and four_button_bool == True: # 第四章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 4:
                    chapter_id = 4
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.button == 1 and five_button_bool == True: # 第五章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 5:
                    chapter_id = 5
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.button == 1 and six_button_bool == True: # 第六章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 6:
                    chapter_id = 6
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            elif event.button == 1 and seven_button_bool == True: # 第七章
                show_levelscene_bool, close_levelscene_bool = True, False
                if chapter_id != 7:
                    chapter_id = 7
                    main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                    read_main_coordinate = True # 游戏创建重新读取主坐标
                    Pills = settings('pills_base_dictionaries') # 重新初始化止痛药字典
                    Zombies = settings('zombies_base_dictionaries') # 重新初始化丧尸字典
                    zombies_action = 0 # 重新初始化丧尸活动次数
                else:
                    x_dvalue, y_dvalue = 0, 0 # 重新初始化x, y差值
            else:
                show_levelscene_bool, close_levelscene_bool = True, False

    # 更新运行次数(如果玩家第一次进入游戏没有玩, 进入章节界面后没有按第一章节按钮, 运行次数为1, 如果按第一章节按钮, 则运行次数还是1, 如果按了其他章节按钮再按第一章节按钮, 运行次数还是1)
    if chapter_id != settings('chapter_base_id'):
        # 玩家改变章节, 运行次数变成1(用于玩家没有开始玩或者玩过了但是改变想章节)
        runs_number = 1
    elif chapter_id == settings('chapter_base_id') and \
         int(main_coordinate[0]) == settings('base_coordinate')[0] and int(main_coordinate[1]) == settings('base_coordinate')[1] and \
         int(player_health) == settings('player_base_health') and int(bullets_number) == settings('bullets_base_number'):
        # 玩家没有改变章节, 运行次数为1, 运行次数只可以在开始新旅途界面变成默认值(玩家进入游戏但是没有玩)
        if enter_chapter_1 == True:
            runs_number = 1

    # 实时保存游戏对象的主坐标(主坐标不可以导入, 但是要返回)
    save_data(main_coordinate = main_coordinate)

    return show_levelscene_bool, close_levelscene_bool, chapter_id, language, runs_number, read_main_coordinate, main_coordinate, x_dvalue, y_dvalue, write_temporary_file, enter_chapter_1, Pills, Zombies, zombies_action


# 关闭章节界面
def close_levelscene(screen, x, y, close_levelscene_bool, open_homescene_bool, min_i, chapter_id, language):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    levelscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = False, chapter_id = chapter_id)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        close_levelscene_bool, open_homescene_bool = False, True
    else:
        min_i = min_i + settings('animation_speed') + 3 # 帧数为120
        close_levelscene_bool, open_homescene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_levelscene_bool, open_homescene_bool, min_i, chapter_id, language