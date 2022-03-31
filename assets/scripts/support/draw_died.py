""" 包含玩家死亡时的画面以及处理玩家数据 """
import pygame

from os import remove # 删除文件
from assets.scripts.support.settings import settings # 设置
from assets.scripts.support.neural_network import NeuralNetwork # 神经网络类

pygame.init()


def draw_died(screen, draw_menuscene, died_i, open_loadscene_bool, scene_1_village_bool, i, min_i, max_i, runs_number, chapter_id, main_coordinate, read_main_coordinate, player_health, bullets_number, Pills, Zombies, iteration, data_id, training_state, neural_network, enter_key, x_dvalue, y_dvalue, if_died, Bullets, zombies_action, if_up, if_down, if_left, if_right, up_bool, down_bool, left_bool, right_bool, if_open_agnifying, if_shoot):
    # 当角色生命值为0时, 绘制透明度逐渐变化的膜
    if int(player_health) == 0:
        surface = pygame.Surface(settings('screen_size'))
        surface.set_alpha(died_i)
        surface.fill(settings('background_color'))
        screen.blit(surface, (0, 0))

        if died_i < 255:
            if draw_menuscene == False:
                died_i = died_i + 3
        else:
            died_i = 255

        # 死亡界面绘制结束, 重新初始化所有参数
        if died_i == 255:
            open_loadscene_bool, scene_1_village_bool = True, False
            died_i, if_died = 0, True
            i, min_i, max_i = 0, 0, 255 # 重新初始化计数器
            # 重新初始化键盘按下标志
            enter_key['enter_w'], enter_key['enter_s'], enter_key['enter_a'], enter_key['enter_d'] = False, False, False, False
            # 重新初始化移动标志和是否开启移动标志
            if_up, if_down, if_left, if_right = True, True, True, True
            up_bool, down_bool, left_bool, right_bool = False, False, False, False
            if_open_agnifying, if_shoot = False, False # 重新初始化射击和打开倍镜标志
            x_dvalue, y_dvalue = 0, 0 # 重新初始化xy差值
            runs_number = settings('runs_base_number') # 运行次数设置为默认状态
            chapter_id = settings('chapter_base_id') # 章节设置为默认状态
            main_coordinate = settings('base_coordinate') # 主坐标设置为默认状态
            read_main_coordinate = True # 游戏创建重新读取主坐标
            player_health = settings('player_base_health') # 玩家生命值设置为默认状态
            bullets_number = settings('bullets_base_number') # 子弹数量设置为默认状态
            Pills = settings('pills_base_dictionaries') # 止痛药字典设置为默认状态
            Zombies = settings('zombies_base_dictionaries') # 丧尸字典设置为默认状态
            Bullets = {} # 子弹字典设置为空
            iteration = settings('base_iteration') # 迭代次数设置为默认状态 
            data_id = settings('data_base_id') # 训练数据id设置为默认状态 
            training_state = settings('training_base_state') # 训练状态设置为默认状态
            zombies_action = 0 # 重新初始化丧尸动作计数器

            # 删除权值文件, 重新初始化神经网络
            remove(settings('weight_input_to_hidden'))
            remove(settings('weight_hidden_to_output'))
            neural_network = NeuralNetwork(settings('input_nodes'), settings('hidden_nodes'), settings('output_nodes'), settings('learning_rate'))

    return draw_menuscene, died_i, open_loadscene_bool, scene_1_village_bool, i, min_i, max_i, runs_number, chapter_id, main_coordinate, read_main_coordinate, player_health, bullets_number, Pills, Zombies, iteration, data_id, training_state, neural_network, enter_key, x_dvalue, y_dvalue, if_died, Bullets, zombies_action, if_up, if_down, if_left, if_right, up_bool, down_bool, left_bool, right_bool, if_open_agnifying, if_shoot