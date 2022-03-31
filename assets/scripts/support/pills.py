""" 包含止痛药, 纱布等回血道具的处理函数 """
import pygame

from assets.scripts.support.bullets_collision import bullets_collision # 子弹碰撞检测
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.detection_position import detection_position # 检测位置
from assets.scripts.support.process_collision import ifopen_collision_detection # 是否打开碰撞检测
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 初始化止痛药碰撞检测
def pills_collision(player_rect, pills_rect):
    # 初始化是否发生碰撞标志
    if_collision = False

    # 碰撞检测
    if player_rect.colliderect(pills_rect) == True:
        if_collision = True

    return if_collision


# 绘制止痛药
def draw_pills(screen, Pills, player_coordinate, player_rect, main_coordinate, Bullets, player_health, chapter_id, draw_menuscene, anti_aliasing):
    # 加载参数和无效止痛药id列表
    text_size = settings('text_size')
    over_pills_id = []

    # 加载读取章节的止痛药字典
    try:
        now_Pills = Pills[str(chapter_id)]
    except KeyError:
        now_Pills = Pills[chapter_id]

    # 读取读取章节的止痛药字典
    for i, Parameter_pills in now_Pills.items():
        # 初始化止痛药参数
        relative_coordinate = Parameter_pills['coordinate'] # 止痛药相对坐标
        vertical = Parameter_pills['vertical'] # 是否竖直
        
        # 根据主坐标计算止痛药目前的坐标
        pills_coordinate = (main_coordinate[0] + relative_coordinate[0], main_coordinate[1] + relative_coordinate[1])

        if detection_position(pills_coordinate) == True: # 检测游戏对象是否在屏幕绘制范围内
            # 根据参数绘制止痛药
            pills_rect = game_object(screen, size = text_size, text = '止痛药', coordinate = pills_coordinate, ifreturn = True, antialiased = anti_aliasing, vertical = vertical)

            # 碰撞检测并将无效对象删除
            if ifopen_collision_detection(pills_coordinate) == True: # 检测是否开启碰撞检测

                # 判断玩家是否为满血或者死亡, 如果不是, 则删除, 并增加血量(不超过100)
                if player_health != 100 and player_health != 0:
                    if_collision = pills_collision(player_rect, pills_rect)

                    if if_collision == True:
                        over_pills_id.append(i)

                        # 如果发生碰撞, 则增加玩家血量
                        player_health = player_health + settings('pills_increase_amount')
                        if player_health > 100: # 限制范围
                            player_health = 100

            # 子弹碰撞检测
            if draw_menuscene == False and player_health > 0:
                Bullets, player_coordinate, pills_coordinate, pills_rect = bullets_collision(screen, Bullets, player_coordinate, pills_coordinate, pills_rect)

    # 删除无效止痛药
    for over_i in over_pills_id:
        del now_Pills[over_i]

    # 更新止痛药字典
    Pills[chapter_id] = now_Pills

    return Pills, Bullets, player_health, chapter_id, draw_menuscene, anti_aliasing