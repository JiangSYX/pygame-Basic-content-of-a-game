""" 包含打开新游戏界面, 显示新游戏界面和关闭新游戏界面函数 """
import pygame

from sys import exit # 退出
from os import remove # 删除文件
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.process_file import read_file # 读取文件
from assets.scripts.support.settings import settings # 设置
from assets.scripts.support.neural_network import NeuralNetwork # 神经网络类
from assets.scripts.support.handle_data import save_data # 保存数据
from assets.scripts.scene_objects.newscene_base_gameobject import newscene_base_gameobject # 新旅途界面基础元素内容

pygame.init()


# 打开新旅途界面
def open_newscene(screen, x, y, open_newscene_bool, show_newscene_bool, max_i, language):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    newscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = False)
    
    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        open_newscene_bool, show_newscene_bool = False, True
    else:
        max_i = max_i - settings('animation_speed') # 帧数为120
        open_newscene_bool, show_newscene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    return open_newscene_bool, show_newscene_bool, max_i, language


# 显示新旅途界面
def show_newscene(screen, x, y, show_newscene_bool, close_newscene_bool, language, runs_number, chapter_id, read_main_coordinate, player_health, bullets_number, x_dvalue, y_dvalue, Pills, Zombies, iteration, data_id, training_state, neural_network):
    # 加载屏幕大小和读取主坐标
    screen_size = settings('screen_size')
    main_coordinate = read_file(settings('main_coordinate_file'), base_data = settings('base_coordinate'))

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 绘制关于界面基本元素内容
    back_button_bool, yes_button_bool = newscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = True)

    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # 返回主页
                show_newscene_bool, close_newscene_bool = False, True
                x_dvalue, y_dvalue = 0, 0 # 重新初始化差值

            elif event.key == pygame.K_RETURN: # 创建新旅途
                show_newscene_bool, close_newscene_bool = False, True
                runs_number = settings('runs_base_number') # 运行次数设置为默认状态
                chapter_id = settings('chapter_base_id') # 章节设置为默认状态
                main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                read_main_coordinate = True # 游戏创建重新读取主坐标
                player_health = settings('player_base_health') # 玩家生命值设置为默认状态
                bullets_number = settings('bullets_base_number') # 子弹数量设置为默认状态
                Pills = settings('pills_base_dictionaries') # 止痛药字典设置为默认状态
                Zombies = settings('zombies_base_dictionaries') # 丧尸字典设置为默认状态
                iteration = settings('base_iteration') # 迭代次数设置为默认状态 
                data_id = settings('data_base_id') # 训练数据id设置为默认状态 
                training_state = settings('training_base_state') # 训练状态设置为默认状态

                # 删除权值文件, 重新初始化神经网络
                remove(settings('weight_input_to_hidden'))
                remove(settings('weight_hidden_to_output'))
                neural_network = NeuralNetwork(settings('input_nodes'), settings('hidden_nodes'), settings('output_nodes'), settings('learning_rate'))

            elif event.key == pygame.K_1: # 创建新旅途
                show_newscene_bool, close_newscene_bool = False, True
                runs_number = settings('runs_base_number') # 运行次数设置为默认状态
                chapter_id = settings('chapter_base_id') # 章节设置为默认状态
                main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                read_main_coordinate = True # 游戏创建重新读取主坐标
                player_health = settings('player_base_health') # 玩家生命值设置为默认状态
                bullets_number = settings('bullets_base_number') # 子弹数量设置为默认状态
                Pills = settings('pills_base_dictionaries') # 止痛药字典设置为默认状态
                Zombies = settings('zombies_base_dictionaries') # 丧尸字典设置为默认状态
                iteration = settings('base_iteration') # 迭代次数设置为默认状态 
                data_id = settings('data_base_id') # 训练数据id设置为默认状态 
                training_state = settings('training_base_state') # 训练状态设置为默认状态

                # 删除权值文件, 重新初始化神经网络
                remove(settings('weight_input_to_hidden'))
                remove(settings('weight_hidden_to_output'))
                neural_network = NeuralNetwork(settings('input_nodes'), settings('hidden_nodes'), settings('output_nodes'), settings('learning_rate'))

            elif event.key == pygame.K_2: # 返回主页
                show_newscene_bool, close_newscene_bool = False, True
                x_dvalue, y_dvalue = 0, 0 # 重新初始化差值
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and back_button_bool == True: # 返回主页
                show_newscene_bool, close_newscene_bool = False, True
                x_dvalue, y_dvalue = 0, 0 # 重新初始化差值

            elif event.button == 1 and yes_button_bool == True: # 创建新旅途
                show_newscene_bool, close_newscene_bool = False, True
                runs_number = settings('runs_base_number') # 运行次数设置为默认状态
                chapter_id = settings('chapter_base_id') # 章节设置为默认状态
                main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
                read_main_coordinate = True # 游戏创建重新读取主坐标
                player_health = settings('player_base_health') # 玩家生命值设置为默认状态
                bullets_number = settings('bullets_base_number') # 子弹数量设置为默认状态
                Pills = settings('pills_base_dictionaries') # 止痛药字典设置为默认状态
                Zombies = settings('zombies_base_dictionaries') # 丧尸字典设置为默认状态
                iteration = settings('base_iteration') # 迭代次数设置为默认状态 
                data_id = settings('data_base_id') # 训练数据id设置为默认状态 
                training_state = settings('training_base_state') # 训练状态设置为默认状态

                # 删除权值文件, 重新初始化神经网络
                remove(settings('weight_input_to_hidden'))
                remove(settings('weight_hidden_to_output'))
                neural_network = NeuralNetwork(settings('input_nodes'), settings('hidden_nodes'), settings('output_nodes'), settings('learning_rate'))

            else:
                show_newscene_bool, close_newscene_bool = True, False

    # 实时保存游戏对象的主坐标(主坐标不可以导入, 但是要返回)
    save_data(main_coordinate = main_coordinate)

    return show_newscene_bool, close_newscene_bool, language, runs_number, chapter_id, main_coordinate, read_main_coordinate, player_health, bullets_number, x_dvalue, y_dvalue, Pills, Zombies, iteration, data_id, training_state, neural_network


# 关闭新旅途界面
def close_newscene(screen, x, y, close_newscene_bool, open_homescene_bool, min_i, language):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    newscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = False)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        close_newscene_bool, open_homescene_bool = False, True
    else:
        min_i = min_i + settings('animation_speed') # 帧数为120
        close_newscene_bool, open_homescene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_newscene_bool, open_homescene_bool, min_i, language