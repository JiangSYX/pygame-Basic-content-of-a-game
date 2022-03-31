""" 包含检测子弹是否碰撞到游戏对象和子弹碰撞游戏对象的文字化声音函数 """
import pygame

from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 子弹碰撞游戏对象后的文字化声音
def collision_textsound(screen, bullets_coordinate):
    # 创建文字声音
    collision_sound_text = '啪'
    collision_sound_size = settings('text_sound_size')

    # 绘制文字化子弹碰撞声音
    game_object(screen, size = collision_sound_size, text = collision_sound_text, coordinate = bullets_coordinate)


# 子弹碰撞检测
def bullets_collision(screen, Bullets, player_coordinate, gameobject_coordinate, gameobject_rect, zombies_health = None):
    # 初始化发生碰撞的子弹字典
    over_bullets_id = {}

    # 计算游戏对象的象限(如果子弹象限与游戏对象象限相同才检测碰撞)
    if gameobject_coordinate[0] > player_coordinate[0] and gameobject_coordinate[1] <= player_coordinate[1]: # 第一象限(包含x正半轴)
        gameobject_quadrant = 1 
    elif gameobject_coordinate[0] <= player_coordinate[0] and gameobject_coordinate[1] < player_coordinate[1]: # 第二象限(包含y正半轴)
        gameobject_quadrant = 2
    elif gameobject_coordinate[0] < player_coordinate[0] and gameobject_coordinate[1] >= player_coordinate[1]: # 第三象限(包含x负半轴)
        gameobject_quadrant = 3
    elif gameobject_coordinate[0] >= player_coordinate[0] and gameobject_coordinate[1] > player_coordinate[1]: # 第四象限(包含y负半轴)
        gameobject_quadrant = 4

    # 遍历子弹字典并检测碰撞
    for i, Parameter in Bullets.items():
        # 获取每一颗字典的相关参数
        bullets_rect = Parameter['bullets_rect'] # 子弹的矩形信息
        coordinate = Parameter['coordinate'] # 子弹的坐标(头坐标)
        quadrant = Parameter['quadrant'] # 象限

        # 如果子弹与游戏对象在同一个象限或者相邻象限, 检测
        if gameobject_quadrant == 1: # 游戏对象在第一象限, 允许检测的子弹象限为1, 2, 4
            if quadrant == 1 or quadrant == 2 or quadrant == 4:
                if gameobject_rect.colliderect(bullets_rect) == True:
                    over_bullets_id[i] = coordinate
        elif gameobject_quadrant == 2: # 游戏对象在第二象限, 允许检测的子弹象限为1, 2, 3
            if quadrant == 1 or quadrant == 2 or quadrant == 3:
                if gameobject_rect.colliderect(bullets_rect) == True:
                    over_bullets_id[i] = coordinate
        elif gameobject_quadrant == 3: # 游戏对象在第三象限, 允许检测的子弹象限为2, 3, 4
            if quadrant == 2 or quadrant == 3 or quadrant == 4:
                if gameobject_rect.colliderect(bullets_rect) == True:
                    over_bullets_id[i] = coordinate
        elif gameobject_quadrant == 4: # 游戏对象在第四象限, 允许检测的子弹象限为1, 3, 4
            if quadrant == 1 or quadrant == 3 or quadrant == 4:
                if gameobject_rect.colliderect(bullets_rect) == True:
                    over_bullets_id[i] = coordinate

    # 删除无效子弹
    for over_i, bullets_coordinate in over_bullets_id.items():
        del Bullets[over_i]
        collision_textsound(screen, bullets_coordinate) # 显示文字化的碰撞声音

        if zombies_health != None:
            zombies_health = zombies_health - settings('bullets_damage')

            if zombies_health == 0:
                break
    
    if zombies_health == None:
        return Bullets, player_coordinate, gameobject_coordinate, gameobject_rect
    else:
        return Bullets, player_coordinate, gameobject_coordinate, gameobject_rect, zombies_health