""" 包含绘制丧尸和丧尸逻辑关系的函数 """
import pygame
import numpy

from random import randint # 随机数

from assets.scripts.support.bullets_collision import bullets_collision # 子弹碰撞检测
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.detection_position import detection_position # 检测位置
from assets.scripts.support.process_collision import ifopen_collision_detection # 是否打开碰撞检测
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 初始化丧尸碰撞检测
def zombies_collision(player_rect, zombies_rect):
    # 初始化是否发生碰撞标志
    if_collision = False

    # 碰撞检测
    if player_rect.colliderect(zombies_rect) == True:
        if_collision = True

    return if_collision


# 绘制丧尸
def draw_zombies(screen, Zombies, player_coordinate, player_rect, main_coordinate, Bullets, player_health, chapter_id, zombies_action, neural_network, draw_menuscene, anti_aliasing):
    # 加载参数和无效丧尸id列表
    text_size = settings('text_size')
    over_zombies_id = []

    # 加载读取章节的丧尸字典
    try:
        now_zombies = Zombies[str(chapter_id)]
    except KeyError:
        now_zombies = Zombies[chapter_id]

    # 读取读取章节的丧尸字典
    for i, Parameter_zombies in now_zombies.items():
        # 初始化丧尸参数
        zombies_health = Parameter_zombies['health'] # 丧尸的生命值
        relative_coordinate = Parameter_zombies['coordinate'] # 丧尸相对坐标
        if_died = Parameter_zombies['if_died'] # 死亡标志
        body = Parameter_zombies['body'] # 尸体展示形式
        vertical = Parameter_zombies['vertical'] # 是否竖直
        
        # 根据主坐标计算丧尸目前的坐标
        zombies_coordinate = (main_coordinate[0] + relative_coordinate[0], main_coordinate[1] + relative_coordinate[1])

        if detection_position(zombies_coordinate) == True: # 检测游戏对象是否在屏幕绘制范围内
            if if_died == False: # 判断丧尸是否已经死亡, 如果没有死, 绘制丧尸
                # 神经网络计算丧尸移动决策
                inputs = []
                query_data = [int(player_coordinate[0]), int(player_coordinate[1]), int(zombies_coordinate[0]), int(zombies_coordinate[1])]
                for item in query_data: # 加载查询数据(输入数据 = (坐标 + 最小负值的绝对值的偏移值)/(最大值 + 最小负值绝对值 + 最小负值的绝对值的偏移值) + 0.01)
                    new = ((item + abs(settings('min_training_data')))/(abs(settings('max_training_data')) + abs(settings('min_training_data'))*2)) + 0.01
                    inputs.append(new)
                outputs = neural_network.query(inputs) # 查询神经网络
                label = numpy.argmax(outputs) + 1

                # 根据查询根据实时更改AI相对坐标
                if label == 1 and draw_menuscene == False: # 向上
                    relative_coordinate = (zombies_coordinate[0] - main_coordinate[0], zombies_coordinate[1] - settings('zombies_speed') - main_coordinate[1])
                elif label == 2 and draw_menuscene == False: # 向下
                    relative_coordinate = (zombies_coordinate[0] - main_coordinate[0], zombies_coordinate[1] + settings('zombies_speed') - main_coordinate[1])
                elif label == 3 and draw_menuscene == False: # 向左
                    relative_coordinate = (zombies_coordinate[0] - settings('zombies_speed') - main_coordinate[0], zombies_coordinate[1] - main_coordinate[1])
                elif label == 4 and draw_menuscene == False: # 向右
                    relative_coordinate = (zombies_coordinate[0] + settings('zombies_speed') - main_coordinate[0], zombies_coordinate[1] - main_coordinate[1])
                elif label == 5 and draw_menuscene == False: # 左上
                    relative_coordinate = (zombies_coordinate[0] - settings('zombies_speed') - main_coordinate[0], zombies_coordinate[1] - settings('zombies_speed') - main_coordinate[1])
                elif label == 6 and draw_menuscene == False: # 右上
                    relative_coordinate = (zombies_coordinate[0] + settings('zombies_speed') - main_coordinate[0], zombies_coordinate[1] - settings('zombies_speed') - main_coordinate[1])
                elif label == 7 and draw_menuscene == False: # 左下
                    relative_coordinate = (zombies_coordinate[0] - settings('zombies_speed') - main_coordinate[0], zombies_coordinate[1] + settings('zombies_speed') - main_coordinate[1])
                elif label == 8 and draw_menuscene == False: # 右下
                    relative_coordinate = (zombies_coordinate[0] + settings('zombies_speed') - main_coordinate[0], zombies_coordinate[1] + settings('zombies_speed') - main_coordinate[1])

                # 计算丧尸坐标
                zombies_coordinate = (main_coordinate[0] + relative_coordinate[0], main_coordinate[1] + relative_coordinate[1])

                # 根据参数绘制丧尸
                zombies_rect = game_object(screen, size = text_size, text = '丧尸', coordinate = zombies_coordinate, ifreturn = True, antialiased = anti_aliasing, vertical = vertical)

                # 碰撞检测修改玩家生命值
                if ifopen_collision_detection(zombies_coordinate) == True: # 检测是否开启碰撞检测, 检测角色与丧尸的碰撞

                    if_collision = zombies_collision(player_rect, zombies_rect)

                    if if_collision == True:
                        # 如果发生碰撞, 则减少玩家血量
                        if zombies_action % settings('fps') == 0 and draw_menuscene == False:
                            player_health = player_health - settings('zombies_reduce_amount')
                            if player_health < 0: # 限制范围
                                player_health = 0
                            zombies_action = zombies_action + 2
                        else:
                        	zombies_action = zombies_action + 2

                # 子弹碰撞检测, 并计算丧尸生命值
                if draw_menuscene == False and player_health > 0:
                    Bullets, player_coordinate, zombies_coordinate, zombies_rect, zombies_health = bullets_collision(screen, Bullets, player_coordinate, zombies_coordinate, zombies_rect, zombies_health = zombies_health)

                # 更新丧尸生命值和坐标
                Parameter_zombies['health'] = zombies_health
                Parameter_zombies['coordinate'] = relative_coordinate
                now_zombies[i] = Parameter_zombies

                # 检测生命值为0的无效丧尸
                if int(zombies_health) <= 0:
                	over_zombies_id.append(i)

            elif if_died == True: # 如果丧尸已经死亡, 绘制尸体或者血肉
                zombies_rect = game_object(screen, size = text_size, text = body, coordinate = zombies_coordinate, ifreturn = True, antialiased = anti_aliasing, vertical = vertical)

                # 子弹碰撞检测
                if draw_menuscene == False and player_health > 0:
                    Bullets, player_coordinate, zombies_coordinate, zombies_rect = bullets_collision(screen, Bullets, player_coordinate, zombies_coordinate, zombies_rect)

                # 更新尸体或者血肉坐标
                Parameter_zombies['coordinate'] = relative_coordinate
                now_zombies[i] = Parameter_zombies

    # 修改无效丧尸参数
    for over_i in over_zombies_id:
        way = randint(1, 2)
        if way == 1:
            body = '尸体'
        elif way == 2:
            body = '血肉'
        now_zombies[over_i]['if_died'] = True
        now_zombies[over_i]['body'] = body

    # 更新丧尸字典
    Zombies[chapter_id] = now_zombies

    return Zombies, Bullets, player_health, chapter_id, zombies_action, neural_network, draw_menuscene, anti_aliasing