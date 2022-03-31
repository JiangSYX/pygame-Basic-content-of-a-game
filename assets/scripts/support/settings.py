""" 包含程序设置函数 """
import pygame

from random import randint, uniform # 随机数

pygame.init()


# 设置
def settings(types):
    # 基础设置
    Name = '文字游戏-基因突变'

    info = pygame.display.Info()
    ScreenSize = (info.current_w, info.current_h)

    # 游戏名字
    if types == 'name':
        output = Name

    # 屏幕大小
    elif types == 'screen_size':
        output = ScreenSize

    # 帧数
    elif types == 'fps':
        output = 120

    # 图片地址
    elif types == 'logo_addness': # logo的地址(背景透明)
        output = 'assets/images/logo.ico'

    elif types == 'mine_logo': # 我的logo的地址(图片背景颜色与背景颜色相同)
        output = 'assets/images/mine_logo.png'

    # 颜色
    elif types == 'background_color': # 背景颜色
        output = (237, 237, 237)

    elif types == 'text_color': # 文字颜色
        output = (0, 0, 0)

    elif types == 'button_above_color': # 鼠标在按钮上面时按钮的颜色
        output = (127, 127, 127)

    # 字体
    elif types == 'text_font_addness': # 字体地址
        output = 'assets/fonts/simkai.ttf'

    elif types == 'text_font_addness_en': # 英文字体地址
        output = 'assets/fonts/cambria.ttc'

    elif types == 'text_size': # 字体大小
        output = 25

    elif types == 'text_sound_size': # 文字化声音的大小
        output = 15

    # 游戏对象
    elif types == 'main_coordinate_file': # 游戏对象的主坐标文件
        output = 'assets/datas/main_coordinate.json'

    elif types == 'base_coordinate': # 主坐标基础数据
        output = (ScreenSize[0]/2, ScreenSize[1]/2)

    # 角色
    elif types == 'player_health_file': # 角色的生命值文件
        output = 'assets/datas/player_health.json'

    elif types == 'player_base_health': # 玩家生命值基础数据
        output = 100

    elif types == 'bullets_number_file': # 角色的子弹数量文件
        output = 'assets/datas/bullets_number.json'

    elif types == 'bullets_base_number': # 子弹数量基础数据
        output = 350

    elif types == 'max_player_speed': # 最大的速度
        output = 3

    elif types == 'middel_player_speed': # 中等的速度
        output = 2

    elif types == 'min_player_speed': # 最小的速度
        output = 1

    elif types == 'move_sign_file': # 移动标志文件地址
        output = 'assets/datas/move_sign.json'

    elif types == 'move_base_sign': # 移动标志基本内容
        output = {'if_up': True, 'if_down': True, 'if_left': True, 'if_right': True}

    elif types == 'draw_blood_strip_file': # 是否绘制血条的标志的文件地址
        output = 'assets/datas/draw_blood_strip.json'

    elif types == 'base_draw_blood_strip': # 是否绘制血条的基础标志
        output = True

    # 章节id
    elif types == 'chapter_id_file': # 章节id的文件
        output = 'assets/datas/chapter_id.json'

    elif types == 'chapter_base_id': # 章节id基础数据
        output = 1

    # 显示模式
    elif types == 'display_mode_file': # 显示模式文件
        output = 'assets/datas/display_mode.json'

    elif types == 'display_base_mode': # 显示模式基础数据
        output = 'full_screen'

    # 抗锯齿
    elif types == 'anti_aliasing_file': # 是否打开抗锯齿文件
        output = 'assets/datas/anti_aliasing.json'

    elif types == 'anti_base_aliasing': # 抗锯齿基础数据
        output = True

    # UI语言
    elif types == 'language_file': # UI语言文件
        output = 'assets/datas/language.json'

    elif types == 'language_base': # 语言基础数据
        output = 'chinese'

    # 屏幕大小
    elif types == 'display_size_file': # 屏幕大小文件
        output = 'assets/datas/display_size.json'

    elif types == 'display_base_size': # 屏幕大小的基础数据
        output = 'MaxXxMaxY'

    # 运行次数
    elif types == 'runs_number_file': # 运行次数文件
        output = 'assets/datas/runs_number.json'

    elif types == 'runs_base_number': # 运行次数的基础数据
        output = 0

    # 动画速度
    elif types == 'animation_speed': # 单次动画速度
        output = 14

    # 临时文件
    elif types == 'temporary_chapter_id_file': # 临时存储章节id文件
        output = 'assets/datas/temporary_chapter_id.json'

    elif types == 'temporary_main_coordinate_file': # 临时存储主坐标文件
        output = 'assets/datas/temporary_main_coordinate.json'

    elif types == 'temporary_Pills_file': # 临时存储止痛药文件
        output = 'assets/datas/temporary_Pills.json'

    elif types == 'temporary_Zombies_file': # 临时存储丧尸文件
        output = 'assets/datas/temporary_Zombies.json'

    # 子弹
    elif types == 'bullets_speed': # 子弹速度
        output = 7

    elif types == 'bullets_length': # 子弹长度
        output = 7

    elif types == 'bullets_width': # 子弹宽度
        output = 2

    elif types == 'bullets_max_number': # 限制子弹数量
        output = 20

    elif types == 'bullets_damage': # 子弹伤害
        output = 25

    # 止痛药
    elif types == 'pills_increase_amount': # 止痛药增加量
        output = randint(15, 25)

    elif types == 'pills_file': # 止痛药字典文件
        output = 'assets/datas/pills.json'

    elif types == 'pills_base_dictionaries': # 止痛药基础字典(章节 | ((止痛药id(坐标, 竖直))(止痛药id(坐标, 竖直))))
        output = {
                    1: {1: {'coordinate': (-3, 205), 'vertical': True}}, 
                    2: {1: {'coordinate': (20, 200), 'vertical': False}, 2: {'coordinate': (-100, 400), 'vertical': False}}, 
                    3: {1: {'coordinate': (400, -150), 'vertical': False}, 2: {'coordinate': (150, 320), 'vertical': False}}, 
                    4: {1: {'coordinate': (300, 300), 'vertical': False}}, 
                    5: {1: {'coordinate': (220, -100), 'vertical': False}}, 
                    6: {1: {'coordinate': (20, -400), 'vertical': False}, 2: {'coordinate': (200, 400), 'vertical': False}}, 
                    7: {}
                }

    # 丧尸
    elif types == 'zombies_reduce_amount': # 丧尸的伤害
        output = 1

    elif types == 'zombies_speed': # 丧尸移动速度
        output = 2

    elif types == 'zombies_file': # 丧尸字典文件
        output = 'assets/datas/zombies.json'

    elif types == 'zombies_base_dictionaries': # 丧尸基础字典(章节 | ((丧尸id(生命值, 坐标, 死亡标志, 尸体展示内容, 竖直))(丧尸id(生命值, 坐标, 死亡标志, 尸体展示内容, 竖直))))
        output = {
                    1: {1: {'health': 100, 'coordinate': (400, 100), 'if_died': False, 'body': None, 'vertical': False}, 2: {'health': 100, 'coordinate': (400, 200), 'if_died': False, 'body': None, 'vertical': False}},
                    2: {},
                    3: {},
                    4: {},
                    5: {},
                    6: {},
                    7: {}
                }

    # 神经网络
    elif types == 'input_nodes': # 输入层节点个数
        output = 4

    elif types == 'hidden_nodes': # 隐藏层节点个数
        output = 200

    elif types == 'output_nodes': # 输出层节点个数
        output = 8

    elif types == 'learning_rate': # 学习率
        output = 0.1

    elif types == 'base_iteration': # 基础迭代次数
        output = 1

    elif types == 'max_iteration': # 最大迭代次数
        output = 10

    elif types == 'iteration_file': # 迭代次数文件地址
        output = 'assets/datas/iteration.json'

    elif types == 'data_base_id': # 基础训练数据id
        output = 0

    elif types == 'data_id_file': # 训练数据id文件地址
        output = 'assets/datas/data_id.json'

    elif types == 'training_base_state': # 基础训练状态
        output = True

    elif types == 'training_state_file': # 训练状态文件地址
        output = 'assets/datas/training_state.json'

    elif types == 'training_data_number': # 训练数据数量
        output = 100000

    elif types == 'max_training_data': # 最大的训练数据
        output = 1000

    elif types == 'min_training_data': # 最小的训练数据
        output = -100

    elif types == 'training_data_file': # 训练数据文件地址
        output = 'assets/datas/training_data.json'

    elif types == 'weight_input_to_hidden': # 输入层到隐藏层权值文件地址
        output = 'assets/datas/weight_input_to_hidden'

    elif types == 'weight_hidden_to_output': # 隐藏层到输出层权值文件地址
        output = 'assets/datas/weight_hidden_to_output'

    # 神经网络移动标志
    elif types == 'nn_up': # 向上
        output = 1

    elif types == 'nn_down': # 向下
        output = 2

    elif types == 'nn_left': # 向左
        output = 3

    elif types == 'nn_right': # 向右
        output = 4

    elif types == 'nn_upleft': # 左上
        output = 5

    elif types == 'nn_upright': # 右上
        output = 6

    elif types == 'nn_downleft': # 左下
        output = 7

    elif types == 'nn_downright': # 右下
        output = 8

    return output