""" 包含碰撞检测和是否打开碰撞检测函数 """
import pygame

from assets.scripts.support.settings import settings # 设置

pygame.init()


# 碰撞检测
def collision_detection(player_coordinate, gameobject_coordinate, player_rect, gameobject_rect, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, enter_key):
    # 检测角色是否碰撞游戏对象上面
    if player_coordinate[0] + player_rect.width/2 >= gameobject_coordinate[0] - gameobject_rect.width/2 and \
        player_coordinate[0] - player_rect.width/2 <= gameobject_coordinate[0] + gameobject_rect.width/2 and \
        player_coordinate[1] - player_rect.height/2 <= gameobject_coordinate[1] + gameobject_rect.height/2 + settings('max_player_speed') and \
        player_coordinate[1] - player_rect.height/2 >= gameobject_coordinate[1] + gameobject_rect.height/2:
        if down_bool == True:
            down_bool, if_down, if_up, if_left, if_right = False, False, True, True, True # 当前移动标志关, 除反方向的检测移动标志的标志开外, 其他的都关闭
        if up_bool == True:
            up_bool, if_up, if_down, if_left, if_right = True, True, True, True, True
        if left_bool == True or right_bool == True:
            down_bool, if_down = False, False
    
    elif player_coordinate[0] + player_rect.width/2 < gameobject_coordinate[0] - gameobject_rect.width/2 - settings('max_player_speed') and \
        player_coordinate[1] - player_rect.height/2 <= gameobject_coordinate[1] + gameobject_rect.height/2 + settings('max_player_speed') and \
        player_coordinate[1] - player_rect.height/2 >= gameobject_coordinate[1] + gameobject_rect.height/2:
        if enter_key['enter_w'] == True:
            down_bool, if_down = True, True

    elif player_coordinate[0] - player_rect.width/2 > gameobject_coordinate[0] + gameobject_rect.width/2 + settings('max_player_speed') and \
        player_coordinate[1] - player_rect.height/2 <= gameobject_coordinate[1] + gameobject_rect.height/2 + settings('max_player_speed') and \
        player_coordinate[1] - player_rect.height/2 >= gameobject_coordinate[1] + gameobject_rect.height/2:
        if enter_key['enter_w'] == True:
            down_bool, if_down = True, True

    else:
        if_down = True
        if enter_key['enter_w'] == True:
            down_bool = True

    
    # 检测角色是否碰撞游戏对象下面
    if player_coordinate[0] + player_rect.width/2 >= gameobject_coordinate[0] - gameobject_rect.width/2 and \
        player_coordinate[0] - player_rect.width/2 <= gameobject_coordinate[0] + gameobject_rect.width/2 and \
        player_coordinate[1] + player_rect.height/2 >= gameobject_coordinate[1] - gameobject_rect.height/2 - settings('max_player_speed') and \
        player_coordinate[1] + player_rect.height/2 <= gameobject_coordinate[1] - gameobject_rect.height/2:
        if up_bool == True:
            up_bool, if_up, if_down, if_left, if_right = False, False, True, True, True # 当前移动标志关, 除反方向的检测移动标志的标志开外, 其他的都关闭
        if down_bool == True:
            down_bool, if_up, if_down, if_left, if_right = True, True, True, True, True
        if left_bool == True or right_bool == True:
            up_bool, if_up = False, False

    elif player_coordinate[0] + player_rect.width/2 < gameobject_coordinate[0] - gameobject_rect.width/2 - settings('max_player_speed') and \
        player_coordinate[1] + player_rect.height/2 >= gameobject_coordinate[1] - gameobject_rect.height/2 - settings('max_player_speed') and \
        player_coordinate[1] + player_rect.height/2 <= gameobject_coordinate[1] - gameobject_rect.height/2:
        if enter_key['enter_s'] == True:
            up_bool, if_up = True, True

    elif player_coordinate[0] - player_rect.width/2 > gameobject_coordinate[0] + gameobject_rect.width/2 + settings('max_player_speed') and \
        player_coordinate[1] + player_rect.height/2 >= gameobject_coordinate[1] - gameobject_rect.height/2 - settings('max_player_speed') and \
        player_coordinate[1] + player_rect.height/2 <= gameobject_coordinate[1] - gameobject_rect.height/2:
        if enter_key['enter_s'] == True:
            up_bool, if_up = True, True

    else:
        if_up = True
        if enter_key['enter_s'] == True:
            up_bool = True


    # 检测角色是否碰撞游戏对象左边
    if player_coordinate[1] + player_rect.height/2 >= gameobject_coordinate[1] - gameobject_rect.height/2 and \
        player_coordinate[1] - player_rect.height/2 <= gameobject_coordinate[1] + gameobject_rect.height/2 and \
        player_coordinate[0] - player_rect.width/2 <= gameobject_coordinate[0] + gameobject_rect.width/2 + settings('max_player_speed') and \
        player_coordinate[0] - player_rect.width/2 >= gameobject_coordinate[0] + gameobject_rect.width/2:
        if right_bool == True:
            right_bool, if_right, if_up, if_down, if_left = False, False, True, True, True # 当前移动标志关, 除反方向的检测移动标志的标志开外, 其他的都关闭
        if left_bool == True:
            left_bool, if_up, if_down, if_left, if_right = True, True, True, True, True
        if up_bool == True or down_bool == True:
            right_bool, if_right = False, False

    elif player_coordinate[1] + player_rect.height/2 < gameobject_coordinate[1] - gameobject_rect.height/2 - settings('max_player_speed') and \
        player_coordinate[0] - player_rect.width/2 <= gameobject_coordinate[0] + gameobject_rect.width/2 + settings('max_player_speed') and \
        player_coordinate[0] - player_rect.width/2 >= gameobject_coordinate[0] + gameobject_rect.width/2:
        if enter_key['enter_a'] == True:
            right_bool, if_right = True, True

    elif player_coordinate[1] - player_rect.height/2 > gameobject_coordinate[1] + gameobject_rect.height/2 + settings('max_player_speed') and \
        player_coordinate[0] - player_rect.width/2 <= gameobject_coordinate[0] + gameobject_rect.width/2 + settings('max_player_speed') and \
        player_coordinate[0] - player_rect.width/2 >= gameobject_coordinate[0] + gameobject_rect.width/2:
        if enter_key['enter_a'] == True:
            right_bool, if_right = True, True

    else:
        if_right = True
        if enter_key['enter_a'] == True:
            right_bool = True
    

    # 检测角色是否碰撞游戏对象右边
    if player_coordinate[1] + player_rect.height/2 >= gameobject_coordinate[1] - gameobject_rect.height/2 and \
        player_coordinate[1] - player_rect.height/2 <= gameobject_coordinate[1] + gameobject_rect.height/2 and \
        player_coordinate[0] + player_rect.width/2 >= gameobject_coordinate[0] - gameobject_rect.width/2 - settings('max_player_speed') and \
        player_coordinate[0] + player_rect.width/2 <= gameobject_coordinate[0] - gameobject_rect.width/2:
        if left_bool == True:
            left_bool, if_left, if_up, if_down, if_right = False, False, True, True, True # 当前移动标志关, 除反方向的检测移动标志的标志开外, 其他的都关闭
        if right_bool == True:
            right_bool, if_up, if_down, if_left, if_right = True, True, True, True, True
        if up_bool == True or down_bool == True:
            left_bool, if_left = False, False

    elif player_coordinate[1] + player_rect.height/2 < gameobject_coordinate[1] - gameobject_rect.height/2 - settings('max_player_speed') and \
        player_coordinate[0] + player_rect.width/2 >= gameobject_coordinate[0] - gameobject_rect.width/2 - settings('max_player_speed') and \
        player_coordinate[0] + player_rect.width/2 <= gameobject_coordinate[0] - gameobject_rect.width/2:
        if enter_key['enter_d'] == True:
            left_bool, if_left = True, True

    elif player_coordinate[1] - player_rect.height/2 > gameobject_coordinate[1] + gameobject_rect.height/2 + settings('max_player_speed') and \
        player_coordinate[0] + player_rect.width/2 >= gameobject_coordinate[0] - gameobject_rect.width/2 - settings('max_player_speed') and \
        player_coordinate[0] + player_rect.width/2 <= gameobject_coordinate[0] - gameobject_rect.width/2:
        if enter_key['enter_d'] == True:
            left_bool, if_left = True, True

    else:
        if_left = True
        if enter_key['enter_d'] == True:
            left_bool = True

    return up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, enter_key


# 检测是否开始碰撞检测
def ifopen_collision_detection(gameobject_coordinate):
    screen_size = settings('screen_size')

    # 如果游戏对象的中心坐标在屏幕里面, 就开启碰撞检测
    if gameobject_coordinate[0] >= 0 and gameobject_coordinate[0] <= screen_size[0] and \
       gameobject_coordinate[1] >= 0 and gameobject_coordinate[1] <= screen_size[1]:
        bools = True
    else:
        bools = False

    return bools