""" 包含绘制第一个游戏场景乡村的函数 """
import numpy

from assets.scripts.support.bullets_collision import bullets_collision # 子弹碰撞检测
from assets.scripts.support.draw_menu import draw_menu # 绘制菜单
from assets.scripts.support.draw_died import draw_died # 绘制死亡界面
from assets.scripts.support.draw_objects import draw_objects # 绘制游戏对象
from assets.scripts.support.detection_position import detection_position # 检测位置
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.game_ui import game_UI # 游戏UI
from assets.scripts.support.handle_data import save_data # 保存数据
from assets.scripts.support.pills import draw_pills # 绘制止痛药
from assets.scripts.support.zombies import draw_zombies # 绘制丧尸
from assets.scripts.support.player import player # 玩家角色
from assets.scripts.support.process_collision import collision_detection, ifopen_collision_detection # 碰撞检测, 是否打开碰撞检测
from assets.scripts.support.process_file import read_file # 读取文件
from assets.scripts.support.record_sign import record_sign # 记录标志
from assets.scripts.support.settings import settings # 设置


# 第一个场景-乡村
def scene_1_village(screen, scene_1_village_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, main_coordinate, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_1_objects, draw_blood_strip):
    # 加载参数
    scene_name = '乡村'
    text_size = settings('text_size')
    runs_number = 1 # 运行次数改为大于0


    # 更新迭代次数与训练标志
    if iteration <= settings('max_iteration'):
        if data_id == settings('training_data_number'):
            iteration = iteration + 1
            training_state = True # 继续训练神经网络
            data_id = 0 # 当前迭代结束, 开始下一次迭代, 数据id归零
            
            if iteration == settings('max_iteration') + 1:
                training_state = False

        else:
            training_state = True # 继续训练神经网络
    else:
        iteration = iteration + 1 # 将迭代次数超值, 下次循环将不会判断
        training_state = False # 停止训练神经网络


    # 训练神经网络, 每次循环训练一个数据(每次迭代10万数据, 一共迭代10次)
    if training_state == True:
        train_data = training_data[data_id]
        # 加载输入数据(输入数据 = (坐标 + 最小负值的绝对值的偏移值)/(最大值 + 最小负值绝对值 + 最小负值的绝对值的偏移值) + 0.01)
        inputs = []
        for item in train_data[1:]:
            new = ((item + abs(settings('min_training_data')))/(abs(settings('max_training_data')) + abs(settings('min_training_data'))*2)) + 0.01
            inputs.append(new)

        # 加载目标数据
        targets = numpy.zeros(settings('output_nodes')) + 0.01 # 创建一个输出层神经元个数的列表, 元素值为0.01
        targets[int(train_data[0]) - 1] = 0.99 # 用0.99代替正确元素的位置

        # 训练神经网络
        neural_network.train(inputs, targets)

        # 数据id增加
        data_id = data_id + 1


    # 判断是否重新读取主坐标和初始化x, y偏值
    if read_main_coordinate == True:
        main_coordinate = read_file(settings('main_coordinate_file'), base_data = settings('base_coordinate'))
        x_dvalue, y_dvalue = 0, 0
        read_main_coordinate = False


    # 绘制背景颜色
    screen.fill(settings('background_color'))


    # 绘制角色, 如果不允许绘制菜单, 则暂停游戏
    up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, player_rect, x, y, if_open_agnifying, if_shoot, draw_menuscene, draw_chapter_name, i, min_i, max_i, scene_1_village_bool, open_homescene_bool, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, enter_key, died_i, zombies_action, anti_aliasing, draw_blood_strip = player(
        screen, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, draw_menuscene, draw_chapter_name, i, min_i, max_i, scene_1_village_bool, open_homescene_bool, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, enter_key, died_i, zombies_action, anti_aliasing, draw_blood_strip)


    # 根据差值更改游戏对象的主坐标
    main_coordinate = (main_coordinate[0] + x_dvalue, main_coordinate[1] + y_dvalue)


    # 绘制对象并检测是否碰撞(一个一个检测, 每一个都有对应的移动标志字典, 检测字典中的同一个参数, 如果其中一个字典的移动标志改变, 则主移动标志改变)
    # # object 1
    ids = 1
    text_1 = '墙墙墙墙墙墙墙'
    object_1_coordinate = (main_coordinate[0] + 95, main_coordinate[1] - 100)
    object_1_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_1_dictionaries, enter_key = draw_objects(
        screen, text_1, text_size, object_1_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_1_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_1_dictionaries['if_up'], object_1_dictionaries['if_down'], object_1_dictionaries['if_left'], object_1_dictionaries['if_right']
    
    # # object 2
    ids = 2
    text_2 = '墙墙墙墙墙墙墙墙墙墙墙墙墙墙'
    object_2_coordinate = (main_coordinate[0] + 170, main_coordinate[1] + 185 - 100)
    object_2_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_2_dictionaries, enter_key = draw_objects(
        screen, text_2, text_size, object_2_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_2_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_2_dictionaries['if_up'], object_2_dictionaries['if_down'], object_2_dictionaries['if_left'], object_2_dictionaries['if_right']

    # # object 3
    ids = 3
    text_3 = '墙墙墙墙墙墙墙墙墙墙墙墙墙墙'
    object_3_coordinate = (main_coordinate[0] + 8, main_coordinate[1] + 375 - 100)
    object_3_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_3_dictionaries, enter_key = draw_objects(
        screen, text_3, text_size, object_3_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_3_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_3_dictionaries['if_up'], object_3_dictionaries['if_down'], object_3_dictionaries['if_left'], object_3_dictionaries['if_right']

    # # object 4
    ids = 4
    text_4 = '墙墙墙'
    object_4_coordinate = (main_coordinate[0] + 65, main_coordinate[1] + 198 - 100)
    object_4_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_4_dictionaries, enter_key = draw_objects(
        screen, text_4, text_size, object_4_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_4_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_4_dictionaries['if_up'], object_4_dictionaries['if_down'], object_4_dictionaries['if_left'], object_4_dictionaries['if_right']

    # # object 5
    ids = 5
    text_5 = '墙'
    object_5_coordinate = (main_coordinate[0] + 145, main_coordinate[1] + 198 - 100)
    object_5_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_5_dictionaries, enter_key = draw_objects(
        screen, text_5, text_size, object_5_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_5_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_5_dictionaries['if_up'], object_5_dictionaries['if_down'], object_5_dictionaries['if_left'], object_5_dictionaries['if_right']

    # # object 6
    ids = 6
    text_6 = '门'
    object_6_coordinate = (main_coordinate[0] + 118, main_coordinate[1] + 198 - 100)
    object_6_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_6_dictionaries, enter_key = draw_objects(
        screen, text_6, text_size, object_6_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_6_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing, if_detection = False)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_6_dictionaries['if_up'], object_6_dictionaries['if_down'], object_6_dictionaries['if_left'], object_6_dictionaries['if_right']

    # # object 7
    ids = 7
    text_7 = '墙墙墙墙墙墙'
    object_7_coordinate = (main_coordinate[0] + 40, main_coordinate[1] + 285 - 100)
    object_7_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_7_dictionaries, enter_key = draw_objects(
        screen, text_7, text_size, object_7_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_7_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_7_dictionaries['if_up'], object_7_dictionaries['if_down'], object_7_dictionaries['if_left'], object_7_dictionaries['if_right']

    # # object 8
    ids = 8
    text_8 = '马桶'
    object_8_coordinate = (main_coordinate[0] + 104, main_coordinate[1] + 335 - 100)
    object_8_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_8_dictionaries, enter_key = draw_objects(
        screen, text_8, text_size, object_8_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_8_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_8_dictionaries['if_up'], object_8_dictionaries['if_down'], object_8_dictionaries['if_left'], object_8_dictionaries['if_right']

    # # object 9
    ids = 9
    text_9 = '墙墙墙墙墙墙墙墙墙墙墙墙墙墙'
    object_9_coordinate = (main_coordinate[0] - 155, main_coordinate[1] + 185 - 100)
    object_9_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_9_dictionaries, enter_key = draw_objects(
        screen, text_9, text_size, object_9_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_9_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_9_dictionaries['if_up'], object_9_dictionaries['if_down'], object_9_dictionaries['if_left'], object_9_dictionaries['if_right']

    # # object 10
    ids = 10
    text_10 = '门'
    object_10_coordinate = (main_coordinate[0] + 10, main_coordinate[1] + 198 - 100)
    object_10_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_10_dictionaries, enter_key = draw_objects(
        screen, text_10, text_size, object_10_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_10_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing, if_detection = False)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_10_dictionaries['if_up'], object_10_dictionaries['if_down'], object_10_dictionaries['if_left'], object_10_dictionaries['if_right']

    # # object 11
    ids = 11
    text_11 = '墙墙墙墙墙'
    object_11_coordinate = (main_coordinate[0] - 75, main_coordinate[1] + 198 - 100)
    object_11_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_11_dictionaries, enter_key = draw_objects(
        screen, text_11, text_size, object_11_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_11_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_11_dictionaries['if_up'], object_11_dictionaries['if_down'], object_11_dictionaries['if_left'], object_11_dictionaries['if_right']

    # # object 12
    ids = 12
    text_12 = '床床床'
    object_12_coordinate = (main_coordinate[0] - 127, main_coordinate[1] + 325 - 100)
    object_12_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_12_dictionaries, enter_key = draw_objects(
        screen, text_12, text_size, object_12_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_12_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_12_dictionaries['if_up'], object_12_dictionaries['if_down'], object_12_dictionaries['if_left'], object_12_dictionaries['if_right']

    # # object 13
    ids = 13
    text_13 = '床床床'
    object_13_coordinate = (main_coordinate[0] - 100, main_coordinate[1] + 325 - 100)
    object_13_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_13_dictionaries, enter_key = draw_objects(
        screen, text_13, text_size, object_13_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_13_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_13_dictionaries['if_up'], object_13_dictionaries['if_down'], object_13_dictionaries['if_left'], object_13_dictionaries['if_right']

    # # object 14
    ids = 14
    text_14 = '沙发沙发'
    object_14_coordinate = (main_coordinate[0] + 145, main_coordinate[1])
    object_14_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_14_dictionaries, enter_key = draw_objects(
        screen, text_14, text_size, object_14_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_14_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_14_dictionaries['if_up'], object_14_dictionaries['if_down'], object_14_dictionaries['if_left'], object_14_dictionaries['if_right']

    # # object 15
    ids = 15
    text_15 = '电视'
    object_15_coordinate = (main_coordinate[0] - 127, main_coordinate[1])
    object_15_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_15_dictionaries, enter_key = draw_objects(
        screen, text_15, text_size, object_15_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_15_dictionaries, enter_key, vertical = True, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_15_dictionaries['if_up'], object_15_dictionaries['if_down'], object_15_dictionaries['if_left'], object_15_dictionaries['if_right']

    # # object 16
    ids = 16
    text_16 = '门门'
    object_16_coordinate = (main_coordinate[0] - 15, main_coordinate[1] - 100)
    object_16_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_16_dictionaries, enter_key = draw_objects(
        screen, text_16, text_size, object_16_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_16_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing, if_detection = False)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_16_dictionaries['if_up'], object_16_dictionaries['if_down'], object_16_dictionaries['if_left'], object_16_dictionaries['if_right']

    # # object 17
    ids = 17
    text_17 = '墙墙墙墙墙'
    object_17_coordinate = (main_coordinate[0] - 103, main_coordinate[1] - 100)
    object_17_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_17_dictionaries, enter_key = draw_objects(
        screen, text_17, text_size, object_17_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_17_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_17_dictionaries['if_up'], object_17_dictionaries['if_down'], object_17_dictionaries['if_left'], object_17_dictionaries['if_right']

    # # object 18
    ids = 18
    text_18 = '栏杆栏杆栏杆栏杆栏杆栏杆栏杆'
    object_18_coordinate = (main_coordinate[0] - 215, main_coordinate[1] - 127)
    object_18_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_18_dictionaries, enter_key = draw_objects(
        screen, text_18, text_size, object_18_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_18_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_18_dictionaries['if_up'], object_18_dictionaries['if_down'], object_18_dictionaries['if_left'], object_18_dictionaries['if_right']

    # # object 19
    ids = 19
    text_19 = '栏杆栏杆栏杆栏杆栏杆栏杆栏杆'
    object_19_coordinate = (main_coordinate[0] - 565, main_coordinate[1] - 127)
    object_19_dictionaries = {'up_bool': up_bool, 'down_bool': down_bool, 'left_bool': left_bool, 'right_bool': right_bool, 'if_up': chapter_1_objects[ids]['if_up'], 'if_down': chapter_1_objects[ids]['if_down'], 'if_left': chapter_1_objects[ids]['if_left'], 'if_right': chapter_1_objects[ids]['if_right']}
    player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_19_dictionaries, enter_key = draw_objects(
        screen, text_19, text_size, object_19_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_19_dictionaries, enter_key, vertical = False, antialiased = anti_aliasing)
    chapter_1_objects[ids]['if_up'], chapter_1_objects[ids]['if_down'], chapter_1_objects[ids]['if_left'], chapter_1_objects[ids]['if_right'] = object_19_dictionaries['if_up'], object_19_dictionaries['if_down'], object_19_dictionaries['if_left'], object_19_dictionaries['if_right']

    # # 初始化游戏对象字典列表
    Dictionaries = [object_1_dictionaries, object_2_dictionaries, object_3_dictionaries, object_4_dictionaries, object_5_dictionaries, 
                    object_6_dictionaries, object_7_dictionaries, object_8_dictionaries, object_9_dictionaries, object_10_dictionaries,
                    object_11_dictionaries, object_12_dictionaries, object_13_dictionaries, object_14_dictionaries, object_15_dictionaries, 
                    object_16_dictionaries, object_17_dictionaries, object_18_dictionaries, object_19_dictionaries]

    # # 记录游戏对象标志并计算主标志
    up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, enter_key = record_sign(up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, Dictionaries, enter_key)


    # 绘制止痛药并检测是否碰撞
    Pills, Bullets, player_health, chapter_id, draw_menuscene, anti_aliasing = draw_pills(screen, Pills, player_coordinate, player_rect, main_coordinate, Bullets, player_health, chapter_id, draw_menuscene, anti_aliasing)


    # 绘制丧尸并检测是否碰撞
    Zombies, Bullets, player_health, chapter_id, zombies_action, neural_network, draw_menuscene, anti_aliasing = draw_zombies(screen, Zombies, player_coordinate, player_rect, main_coordinate, Bullets, player_health, chapter_id, zombies_action, neural_network, draw_menuscene, anti_aliasing)


    # 绘制UI, 如果不允许绘制菜单, 则暂停ui的动态部分
    player_health, bullets_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, draw_blood_strip = game_UI(screen, player_health, bullets_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, draw_blood_strip, scene_name = scene_name)

    
    # 绘制死亡界面
    draw_menuscene, died_i, open_loadscene_bool, scene_1_village_bool, i, min_i, max_i, runs_number, chapter_id, main_coordinate, read_main_coordinate, player_health, bullets_number, Pills, Zombies, iteration, data_id, training_state, neural_network, enter_key, x_dvalue, y_dvalue, if_died, Bullets, zombies_action, if_up, if_down, if_left, if_right, up_bool, down_bool, left_bool, right_bool, if_open_agnifying, if_shoot = draw_died(
        screen, draw_menuscene, died_i, open_loadscene_bool, scene_1_village_bool, i, min_i, max_i, runs_number, chapter_id, main_coordinate, read_main_coordinate, player_health, bullets_number, Pills, Zombies, iteration, data_id, training_state, neural_network, enter_key, x_dvalue, y_dvalue, if_died, Bullets, zombies_action, if_up, if_down, if_left, if_right, up_bool, down_bool, left_bool, right_bool, if_open_agnifying, if_shoot)


    # 绘制菜单界面(玩家按下确定退出键后, 因为已经重新初始化了draw_menuscene, 此时应该继续绘制菜单)
    if draw_menuscene == True or (scene_1_village_bool == False and open_homescene_bool == True):
        home_button_bool, backgame_button_bool, menuexit_button_bool = draw_menu(screen, x, y, home_button_bool, backgame_button_bool, menuexit_button_bool)


    # 实时保存游戏对象的主坐标(主坐标不可以返回)
    save_data(main_coordinate = main_coordinate)


    return scene_1_village_bool, open_homescene_bool, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, read_main_coordinate, runs_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, Pills, chapter_id, Zombies, zombies_action, neural_network, iteration, data_id, training_state, training_data, enter_key, died_i, open_loadscene_bool, if_died, anti_aliasing, chapter_1_objects, draw_blood_strip