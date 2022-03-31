""" 包含创建神经网络训练数据的函数 """ 
"""此文件代码是单独的一个程序, main.py只负责是否运行这个程序 """
import json

from random import randint, shuffle
from assets.scripts.support.settings import settings # 设置
from assets.scripts.support.process_file import read_file, write_file # 读取文件, 写入文件


def create_data():
    # 获取文件地址
    file = settings('training_data_file')

    try:
        with open(file) as objects:
            output = json.load(objects)
    except FileNotFoundError:
        output = make_data(file)
    except json.decoder.JSONDecodeError:
        output = make_data(file)

    return output


def make_data(addness):
    # 初始化
    data = [] # 空数据列表
    ids = 0 # 次数id

    # 初始化方向
    up = settings('nn_up')
    down = settings('nn_down')
    left = settings('nn_left')
    right = settings('nn_right')
    up_left = settings('nn_upleft')
    up_right = settings('nn_upright')
    down_left = settings('nn_downleft')
    down_right = settings('nn_downright')

    # 初始化控制参数
    number = settings('training_data_number')
    maxs = settings('max_training_data')
    mins = settings('min_training_data')


    # 生成水平向上移动数据   [ up ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        x = randint(mins, maxs)

        target_x, ai_x = x, x

        target_y = randint(mins, maxs)
        ai_y = randint(mins, maxs)

        # 处理向上移动(ai在角色下面)
        if ai_x == target_x and ai_y > target_y:
            direction = up

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 生成水平向下移动数据   [ down ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        x = randint(mins, maxs)

        target_x, ai_x = x, x

        target_y = randint(mins, maxs)
        ai_y = randint(mins, maxs)

        # 处理向下移动(ai在角色上面)
        if ai_x == target_x and ai_y < target_y:
            direction = down

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 生成水平向左移动数据   [ left ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        y = randint(mins, maxs)

        target_y, ai_y = y, y

        target_x = randint(mins, maxs)
        ai_x = randint(mins, maxs)

        # 处理向左移动(ai在角色右面)
        if ai_x > target_x and ai_y == target_y:
            direction = left

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 生成水平向右移动数据   [ right ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        y = randint(mins, maxs)

        target_y, ai_y = y, y

        target_x = randint(mins, maxs)
        ai_x = randint(mins, maxs)

        # 处理向右移动(ai在角色左面)
        if ai_x < target_x and ai_y == target_y:
            direction = right

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 生成斜向左上移动数据    [ up-left ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        target_x = randint(mins, maxs)
        target_y = randint(mins, maxs)
        ai_x = randint(mins, maxs)
        ai_y = randint(mins, maxs)

        # 处理左上移动(ai在角色右下方)
        if ai_x > target_x and ai_y > target_y:
            direction = up_left

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 生成斜向右上移动数据    [ up-right ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        target_x = randint(mins, maxs)
        target_y = randint(mins, maxs)
        ai_x = randint(mins, maxs)
        ai_y = randint(mins, maxs)

        # 处理右上移动(ai在角色左下方)
        if ai_x < target_x and ai_y > target_y:
            direction = up_right

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 生成斜向左下移动数据    [ down-left ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        target_x = randint(mins, maxs)
        target_y = randint(mins, maxs)
        ai_x = randint(mins, maxs)
        ai_y = randint(mins, maxs)

        # 处理左下移动(ai在角色右上方)
        if ai_x > target_x and ai_y < target_y:
            direction = down_left

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 生成斜向右下移动数据    [ down-right ]
    while ids != int(number/2)/4:
        # 定义元素列表
        item = []

        # 随机生成数据
        target_x = randint(mins, maxs)
        target_y = randint(mins, maxs)
        ai_x = randint(mins, maxs)
        ai_y = randint(mins, maxs)

        # 处理右下移动(ai在角色左上方)
        if ai_x < target_x and ai_y < target_y:
            direction = down_right

            # 如果符合条件, id加1
            ids = ids + 1

            # 写入列表
            item.append(direction)
            item.append(target_x)
            item.append(target_y)
            item.append(ai_x)
            item.append(ai_y)

            data.append(item)

        # 不符合条件返回
        else:
            continue


    # 重新初始化id
    ids = 0


    # 打乱数据
    shuffle(data)

    # 写入数据
    write_file(addness, data)

    return data