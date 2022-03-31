""" 包含保存数据的函数 """
from assets.scripts.support.process_file import read_file, write_file # 读取文件, 写入文件
from assets.scripts.support.settings import settings # 设置


def save_data(main_coordinate = None, player_health = None, bullets_number = None, move_sign = None, chapter_id = None, display_mode = None, anti_aliasing = None, language = None, display_size = None, runs_number = None, Pills = None, Zombies = None, iteration = None, training_state = None, data_id = None, draw_blood_strip = None):
    # 保存主坐标
    if main_coordinate != None:
        write_file(settings('main_coordinate_file'), main_coordinate)

    # 保存玩家生命值
    if player_health != None:
        write_file(settings('player_health_file'), player_health)

    # 保存子弹数量
    if bullets_number != None:
        write_file(settings('bullets_number_file'), bullets_number)

    # 保存移动标志
    if move_sign != None:
        write_file(settings('move_sign_file'), move_sign)

    # 保存章节id
    if chapter_id != None:
        write_file(settings('chapter_id_file'), chapter_id)

    # 保存显示模式
    if display_mode != None:
        write_file(settings('display_mode_file'), display_mode)

    # 保存抗锯齿
    if anti_aliasing != None:
        write_file(settings('anti_aliasing_file'), anti_aliasing)

    # 保存语言
    if language != None:
        write_file(settings('language_file'), language)

    # 保存屏幕大小
    if display_size != None:
        write_file(settings('display_size_file'), display_size)

    # 保存运行次数
    if runs_number != None:
        write_file(settings('runs_number_file'), runs_number)

    # 保持止痛药字典
    if Pills != None:
        write_file(settings('pills_file'), Pills)

    # 保存丧尸字典
    if Zombies != None:
        write_file(settings('zombies_file'), Zombies)

    # 保存神经网络迭代次数
    if iteration != None:
        write_file(settings('iteration_file'), iteration)

    # 保存神经网络训练状态
    if training_state != None:
        write_file(settings('training_state_file'), training_state)

    # 保存神经网络当前训练数据的id
    if data_id != None:
        write_file(settings('data_id_file'), data_id)

    # 保存是否绘制血条标志
    if draw_blood_strip != None:
        write_file(settings('draw_blood_strip_file'), draw_blood_strip)