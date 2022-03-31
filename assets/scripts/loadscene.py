""" 包含打开加载界面, 显示加载界面和关闭加载界面函数 """
import pygame

from random import randint, uniform # 随机数
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.settings import settings # 设置
from assets.scripts.scene_objects.loadscene_base_gameobject import loadscene_base_gameobject # 加载界面基础元素内容

pygame.init()


# 打开加载界面
def open_loadscene(screen, open_loadscene_bool, show_loadscene_bool, max_i, chapter_id, if_get_randint, message_id):
    # 加载屏幕大小和获取信息id
    screen_size = settings('screen_size')
    if if_get_randint == True:
        message_id = randint(1, 10)
        if_get_randint = False # 停止获取随机数

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    loadscene_base_gameobject(screen, screen_size, chapter_id, message_id = message_id)
    
    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        if_get_randint = True # 重新初始化是否获取随机数
        open_loadscene_bool, show_loadscene_bool = False, True
    else:
        max_i = max_i - settings('animation_speed') # 帧数为120
        open_loadscene_bool, show_loadscene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    return open_loadscene_bool, show_loadscene_bool, max_i, chapter_id, if_get_randint, message_id


# 显示加载界面
def show_loadscene(screen, show_loadscene_bool, close_loadscene_bool, i, chapter_id, time, loadscene_get_time, open_homescene_bool, message_id):
    # 加载屏幕大小和显示时间, 单位秒
    screen_size = settings('screen_size')
    if loadscene_get_time == True:
        time = round(uniform(1, 2), 1) # 帧数为120, 精确度为1
        loadscene_get_time = False # 停止获取时间

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 绘制关于界面基本元素内容
    loadscene_base_gameobject(screen, screen_size, chapter_id, i, time, message_id = message_id)

    # 更新计数器
    if i >= settings('fps') * time:
        i = 0
        loadscene_get_time = True # 重新初始化加载界面是否应该获取时间
        show_loadscene_bool, close_loadscene_bool, open_homescene_bool = False, True, False
    else:
        i = i + 1 # 帧数为120
        show_loadscene_bool, close_loadscene_bool, open_homescene_bool = True, False, False

    # 响应键盘和鼠标事件, 允许玩家中途退出加载界面, 返回主页
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # 返回主页
                i = 0
                loadscene_get_time = True # 重新初始化加载界面是否应该获取时间
                show_loadscene_bool, close_loadscene_bool, open_homescene_bool = False, False, True
            else:
                show_loadscene_bool, close_loadscene_bool, open_homescene_bool = True, False, False

    return show_loadscene_bool, close_loadscene_bool, i, chapter_id, time, loadscene_get_time, open_homescene_bool, message_id


# 关闭加载界面
def close_loadscene(screen, close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool, min_i, chapter_id, time, message_id):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    loadscene_base_gameobject(screen, screen_size, chapter_id, settings('fps') * time, time, message_id = message_id)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        if chapter_id == 1:
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = False, True, False, False, False, False, False, False
        elif chapter_id == 2:
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = False, False, True, False, False, False, False, False
        elif chapter_id == 3:
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = False, False, False, True, False, False, False, False
        elif chapter_id == 4:
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = False, False, False, False, True, False, False, False
        elif chapter_id == 5:
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = False, False, False, False, False, True, False, False
        elif chapter_id == 6:
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = False, False, False, False, False, False, True, False
        elif chapter_id == 7:
            close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = False, False, False, False, False, False, False, True
    else:
        min_i = min_i + settings('animation_speed') # 帧数为120
        close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool = True, False, False, False, False, False, False, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_loadscene_bool, scene_1_village_bool, scene_2_highway_bool, scene_3_town_bool, scene_4_suburb_bool, scene_5_city_bool, scene_6_trainstation_bool, scene_7_refuge_bool, min_i, chapter_id, message_id