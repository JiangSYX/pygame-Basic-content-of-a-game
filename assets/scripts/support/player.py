""" 包含玩家角色函数 """
import pygame

from sys import exit # 退出
from random import randint, uniform # 随机数
from math import sqrt, asin, pi # 开方, 反正弦, 圆周率
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置
from assets.scripts.support.shooting import text_sound_shoot, draw_bullets, shoot # 开枪射击的文字化声音, 开枪射击

pygame.init()


# 玩家角色
def player(screen, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_coordinate, player_health, bullets_number, x, y, if_open_agnifying, if_shoot, draw_menuscene, draw_chapter_name, i, min_i, max_i, gamescene_bool, open_homescene_bool, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, enter_key, died_i, zombies_action, anti_aliasing, draw_blood_strip):
    # 获取屏幕大小
    screen_size = settings('screen_size')

    # 创建角色
    player_text = '我'
    player_size = settings('text_size')

    # 绘制角色
    player_rect = game_object(screen, size = player_size, text = player_text, coordinate = player_coordinate, ifreturn = True, antialiased = anti_aliasing)

    # 根据生命值设置玩家速度(生命值大于100或者生命值小于0, 速度设置为0)(当前最高帧数120)
    if player_health <= 100 and player_health >= 40:
        player_speed = settings('max_player_speed')
    elif player_health < 40 and player_health >= 20:
        player_speed = settings('middel_player_speed')
    elif player_health < 20 and player_health >= 0:
        player_speed = settings('min_player_speed')
    else:
        player_speed = 0

    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and draw_menuscene == False: # 射击(不允许绘制按钮)
                if len(Bullets) < settings('bullets_max_number'): # 限制子弹数量
                    if_shoot = True # 允许射击

                    # 计算鼠标到角色的距离
                    distance = sqrt(pow(x - player_coordinate[0], 2) + pow(y - player_coordinate[1], 2))

                    # 判断鼠标在角色坐标系的象限和特殊位置
                    if x > player_coordinate[0] and y <= player_coordinate[1]: # 第一象限(包含x正半轴)
                        quadrant = 1 
                    elif x <= player_coordinate[0] and y < player_coordinate[1]: # 第二象限(包含y正半轴)
                        quadrant = 2
                    elif x < player_coordinate[0] and y >= player_coordinate[1]: # 第三象限(包含x负半轴)
                        quadrant = 3
                    elif x >= player_coordinate[0] and y > player_coordinate[1]: # 第四象限(包含y负半轴)
                        quadrant = 4
                    elif x == player_coordinate[0] and y == player_coordinate[1]: # 原点
                        quadrant = 0

                    # 创建存储子弹参数的空字典
                    Parameter = {}

                    # 向参数字典增加子弹坐标
                    Parameter['coordinate'] = bullets_coordinate

                    # 向参数字典增加子弹的矩形信息
                    Parameter['bullets_rect'] = None

                    # 向参数字典增加sin值
                    if quadrant == 0: # 如果鼠标在角色中心位置(原点)点击, sin值则为45度的sin值
                        Parameter['sin'] = sqrt(2)/2
                    else:
                        Parameter['sin'] = abs(y - player_coordinate[1])/distance

                    # 向参数字典增加cos值
                    if quadrant == 0: # 如果鼠标在角色中心位置(原点)点击, cos值则为45度的cos值
                        Parameter['cos'] = sqrt(2)/2
                    else:
                        Parameter['cos'] = abs(x - player_coordinate[0])/distance

                    # 向参数字典增加所在象限
                    if quadrant == 0: # 如果鼠标在角色中心位置(原点)点击, 则给该子弹一个随机象限
                        Parameter['quadrant'] = randint(1, 4)
                    else:
                        Parameter['quadrant'] = quadrant

                    # 通过增加子弹id值来增加子弹数量
                    bullets_id = bullets_id + 1

                    # 向子弹字典中增加id和参数字典
                    Bullets[bullets_id] = Parameter

                    # 添加一颗子弹, 绘制一次文字化声音
                    if player_health > 0:
                        text_sound_shoot(screen, player_coordinate, player_rect, x, y)

            
            elif event.button == 3 and draw_menuscene == False: # 打开倍镜(不允许绘制按钮)
                if_open_agnifying = True

            if event.button == 1 and draw_menuscene == True and menuexit_button_bool == True: # 允许绘制菜单, 按退出按钮退出游戏
                exit()
            
            elif event.button == 1 and draw_menuscene == True and backgame_button_bool == True: # 允许绘制菜单, 按返回游戏按钮返回游戏
                draw_menuscene = not draw_menuscene
            
            elif event.button == 1 and draw_menuscene == True and home_button_bool == True: # 允许绘制菜单, 按主页按钮返回主页
                draw_chapter_name, i, min_i, max_i = False, 0, 0, 255 # 如果玩家提前退出场景, 则重新初始化标志和计数器(用于所有时间段)
                gamescene_bool, open_homescene_bool = False, True
                draw_menuscene = False # 重新初始化是否绘制菜单

                # 重新初始化移动标志
                up_bool, down_bool, left_bool, right_bool = False, False, False, False

                # 重新初始化键盘按下标志
                enter_key['enter_w'], enter_key['enter_s'], enter_key['enter_a'], enter_key['enter_d'] = False, False, False, False

                # 重新初始化射击标志
                if_shoot, if_open_agnifying = False, False

                # 重新初始化子弹参数
                Bullets, bullets_id, if_draw_bullets = {}, 0, False

                # 重新初始化死亡id
                died_i = 0

                # 重新初始化丧尸动作计数器
                zombies_action = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and draw_menuscene == False: # 取消射击(不允许绘制按钮)
                if_shoot = False
            
            elif event.button == 3 and draw_menuscene == False: # 关闭倍镜(不允许绘制按钮)
                if_open_agnifying = False

        elif event.type == pygame.KEYDOWN:
            # 实时记录方向键的按下情况
            if event.key == pygame.K_w:
                enter_key['enter_w'] = True
            elif event.key == pygame.K_s:
                enter_key['enter_s'] = True
            elif event.key == pygame.K_a:
                enter_key['enter_a'] = True
            elif event.key == pygame.K_d:
                enter_key['enter_d'] = True

            # 响应移动标志
            if event.key == pygame.K_w and if_down == True: # 游戏对象向下移动(w)
                down_bool = True
                if_up = True

            elif event.key == pygame.K_s and if_up == True: # 游戏对象向上移动(s)
                up_bool = True
                if_down = True

            elif event.key == pygame.K_a and if_right == True: # 游戏对象向右移动(a)
                right_bool = True
                if_left = True

            elif event.key == pygame.K_d and if_left == True: # 游戏对象向左移动(d)
                left_bool = True
                if_right = True

            # 附加操作
            elif event.key == pygame.K_ESCAPE: # 是否绘制菜单界面(是否返回游戏)
                draw_menuscene = not draw_menuscene

            elif event.key == pygame.K_1 and draw_menuscene == True: # 允许绘制菜单, 按1退出游戏
                exit()

            elif event.key == pygame.K_2 and draw_menuscene == True: # 允许绘制菜单, 按2返回游戏
                draw_menuscene = not draw_menuscene

            elif event.key == pygame.K_3 and draw_menuscene == True: # 允许绘制菜单, 按3返回主页
                draw_chapter_name, i, min_i, max_i = False, 0, 0, 255 # 如果玩家提前退出场景, 则重新初始化标志和计数器(用于所有时间段)
                gamescene_bool, open_homescene_bool = False, True
                draw_menuscene = False # 重新初始化是否绘制菜单

                # 重新初始化移动标志
                up_bool, down_bool, left_bool, right_bool = False, False, False, False

                # 重新初始化键盘按下标志
                enter_key['enter_w'], enter_key['enter_s'], enter_key['enter_a'], enter_key['enter_d'] = False, False, False, False

                # 重新初始化射击标志
                if_shoot, if_open_agnifying = False, False

                # 重新初始化子弹参数
                Bullets, bullets_id, if_draw_bullets = {}, 0, False

                # 重新初始化死亡id
                died_i = 0

                # 重新初始化丧尸动作计数器
                zombies_action = 0

            elif event.key == pygame.K_RETURN and draw_menuscene == True: # 允许绘制菜单, 按确定键返回主页
                draw_chapter_name, i, min_i, max_i = False, 0, 0, 255 # 如果玩家提前退出场景, 则重新初始化标志和计数器(用于所有时间段)
                gamescene_bool, open_homescene_bool = False, True
                draw_menuscene = False # 重新初始化是否绘制菜单

                # 重新初始化移动标志
                up_bool, down_bool, left_bool, right_bool = False, False, False, False

                # 重新初始化键盘按下标志
                enter_key['enter_w'], enter_key['enter_s'], enter_key['enter_a'], enter_key['enter_d'] = False, False, False, False

                # 重新初始化射击标志
                if_shoot, if_open_agnifying = False, False

                # 重新初始化子弹参数
                Bullets, bullets_id, if_draw_bullets = {}, 0, False

                # 重新初始化死亡id
                died_i = 0

                # 重新初始化丧尸动作计数器
                zombies_action = 0

            elif event.key == pygame.K_TAB and draw_menuscene == False: # 是否显示或者隐藏血条(前提是不允许或者菜单)
                draw_blood_strip = not draw_blood_strip

        elif event.type == pygame.KEYUP:
            # 实时记录方向键的按下情况
            if event.key == pygame.K_w:
                enter_key['enter_w'] = False
            elif event.key == pygame.K_s:
                enter_key['enter_s'] = False
            elif event.key == pygame.K_a:
                enter_key['enter_a'] = False
            elif event.key == pygame.K_d:
                enter_key['enter_d'] = False

            # 响应移动标志
            if event.key == pygame.K_w and if_down == True: # 停止移动游戏对象(w)
                down_bool = False
                if_up = True

            elif event.key == pygame.K_s and if_up == True: # 停止移动游戏对象(s)
                up_bool = False
                if_down = True

            elif event.key == pygame.K_a and if_right == True: # 停止移动游戏对象(a)
                right_bool = False
                if_left = True

            elif event.key == pygame.K_d and if_left == True: # 停止移动游戏对象(d)
                left_bool = False
                if_right = True
                

    # 游戏对象移动, 玩家按1个键
    if player_health > 0 and up_bool == True and left_bool != True and right_bool != True and down_bool != True and draw_menuscene == False: # 角色向上移动, 前提是不允许绘制菜单
        x_dvalue, y_dvalue = x_dvalue, y_dvalue - player_speed
    
    if player_health > 0 and down_bool == True and left_bool != True and right_bool != True and up_bool != True and draw_menuscene == False: # 角色向下移动, 前提是不允许绘制菜单
        x_dvalue, y_dvalue = x_dvalue, y_dvalue + player_speed
    
    if player_health > 0 and left_bool == True and up_bool != True and down_bool != True and right_bool != True and draw_menuscene == False: # 角色向左移动, 前提是不允许绘制菜单
        x_dvalue, y_dvalue = x_dvalue - player_speed, y_dvalue
    
    if player_health > 0 and right_bool == True and up_bool != True and down_bool != True and left_bool != True and draw_menuscene == False: # 角色向右移动, 前提是不允许绘制菜单
        x_dvalue, y_dvalue = x_dvalue + player_speed, y_dvalue


    # 游戏对象移动, 玩家按2个键
    if player_health > 0 and up_bool == True and left_bool == True and right_bool != True and down_bool != True and draw_menuscene == False: # 角色向左上移动
        x_dvalue, y_dvalue = x_dvalue - player_speed * round(sqrt(2)/2, 1), y_dvalue - player_speed * round(sqrt(2)/2, 1) 

    if player_health > 0 and up_bool == True and right_bool == True and left_bool != True and down_bool != True and draw_menuscene == False: # 角色向右上移动
        x_dvalue, y_dvalue = x_dvalue + player_speed * round(sqrt(2)/2, 1), y_dvalue - player_speed * round(sqrt(2)/2, 1)

    if player_health > 0 and down_bool == True and left_bool == True and right_bool != True and up_bool != True and draw_menuscene == False: # 角色向左下移动
        x_dvalue, y_dvalue = x_dvalue - player_speed * round(sqrt(2)/2, 1), y_dvalue + player_speed * round(sqrt(2)/2, 1)

    if player_health > 0 and down_bool == True and right_bool == True and left_bool != True and up_bool != True and draw_menuscene == False: # 角色向右下移动
        x_dvalue, y_dvalue = x_dvalue + player_speed * round(sqrt(2)/2, 1), y_dvalue + player_speed * round(sqrt(2)/2, 1)


    # 游戏对象移动, 玩家按3个键
    if player_health > 0 and up_bool == True and left_bool == True and right_bool == True and down_bool != True and draw_menuscene == False: # 角色向上移动
        x_dvalue, y_dvalue = x_dvalue, y_dvalue - player_speed

    if player_health > 0 and down_bool == True and left_bool == True and right_bool == True and up_bool != True and draw_menuscene == False: # 角色向下移动
        x_dvalue, y_dvalue = x_dvalue, y_dvalue + player_speed

    if player_health > 0 and left_bool == True and up_bool == True and down_bool == True and right_bool != True and draw_menuscene == False: # 角色向左移动
        x_dvalue, y_dvalue = x_dvalue - player_speed, y_dvalue

    if player_health > 0 and right_bool == True and up_bool == True and down_bool == True and left_bool != True and draw_menuscene == False: # 角色向右移动
        x_dvalue, y_dvalue = x_dvalue + player_speed, y_dvalue


    # 游戏对象移动, 玩家按4个键
    if player_health > 0 and up_bool == True and down_bool == True and left_bool == True and right_bool == True and draw_menuscene == False: # 游戏对象不动
        x_dvalue, y_dvalue = x_dvalue, y_dvalue


    # 开枪射击, 前提是不允许绘制菜单(玩家按下确定退出键后, 因为已经重新初始化了draw_menuscene, 此时应该继续不允许开枪)
    if player_health > 0 and draw_menuscene == False and gamescene_bool == True and open_homescene_bool == False:
        x, y, if_open_agnifying, if_shoot, bullets_number, if_draw_bullets, bullets_coordinate, bullets_id, Bullets = shoot(screen, x, y, player_coordinate, player_rect, if_open_agnifying, if_shoot, bullets_number, if_draw_bullets, bullets_coordinate, bullets_id, Bullets)


    # 返回移动标志和主坐标, 生命值等参数
    return up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, x_dvalue, y_dvalue, player_health, bullets_number, player_rect, x, y, if_open_agnifying, if_shoot, draw_menuscene, draw_chapter_name, i, min_i, max_i, gamescene_bool, open_homescene_bool, home_button_bool, backgame_button_bool, menuexit_button_bool, if_draw_bullets, bullets_coordinate, bullets_id, Bullets, enter_key, died_i, zombies_action, anti_aliasing, draw_blood_strip