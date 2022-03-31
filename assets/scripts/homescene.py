""" 包含打开主页和显示主页的函数 """
import pygame

from sys import exit # 退出
from assets.scripts.support.exit_game import exit_game # 退出游戏
from assets.scripts.support.settings import settings # 设置
from assets.scripts.scene_objects.homescene_base_gameobject import homescene_base_gameobject # 主页基本元素内容

pygame.init()


# 打开主页
def open_homescene(screen, x, y, open_homescene_bool, show_homescene_bool, max_i, language, runs_number):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制主页基本元素内容
    homescene_base_gameobject(screen, x, y, screen_size, language, runs_number, ifopen_click = False)
    
    # 绘制逐渐隐藏的界面, 逐渐显示界面
    surface = pygame.Surface(screen_size)
    surface.set_alpha(max_i)

    if max_i <= 0:
        max_i = 255
        open_homescene_bool, show_homescene_bool = False, True
    else:
        max_i = max_i - settings('animation_speed') # 帧数为120
        open_homescene_bool, show_homescene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    return open_homescene_bool, show_homescene_bool, max_i, language, runs_number


# 显示主页
def show_homescene(screen, x, y, show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool, language, runs_number, chapter_id):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 绘制主页基本元素内容
    start_button_bool, level_button_bool, options_button_bool, about_button_bool, exit_button_bool, new_button_bool = homescene_base_gameobject(screen, x, y, screen_size, language, runs_number, ifopen_click = True)
    
    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # 打开退出游戏界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, False, True, False, False
            
            elif event.key == pygame.K_1: # 打开选项界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, False, False, True, False
            
            elif event.key == pygame.K_2: # 打开关于界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, True, False, False, False, False
            
            elif event.key == pygame.K_3: # 开始游戏
                if chapter_id == 1:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, True, False, False, False, False, False, False, False, False, False, False, False
                elif chapter_id == 2:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, True, False, False, False, False, False, False, False, False, False, False
                elif chapter_id == 3:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, True, False, False, False, False, False, False, False, False, False
                elif chapter_id == 4:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, True, False, False, False, False, False, False, False, False
                elif chapter_id == 5:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, True, False, False, False, False, False, False, False
                elif chapter_id == 6:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, True, False, False, False, False, False, False
                elif chapter_id == 7:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, True, False, False, False, False, False

            elif event.key == pygame.K_4: # 打开退出游戏界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, False, True, False, False
            
            elif event.key == pygame.K_5: # 打开章节界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, True, False, False, False
            
            elif event.key == pygame.K_6 and runs_number != 0: # 打开新旅途界面(响应条件为运行次数不等于0)
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, False, False, False, True


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and start_button_bool == True: # 开始游戏
                if chapter_id == 1:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, True, False, False, False, False, False, False, False, False, False, False, False
                elif chapter_id == 2:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, True, False, False, False, False, False, False, False, False, False, False
                elif chapter_id == 3:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, True, False, False, False, False, False, False, False, False, False
                elif chapter_id == 4:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, True, False, False, False, False, False, False, False, False
                elif chapter_id == 5:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, True, False, False, False, False, False, False, False
                elif chapter_id == 6:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, True, False, False, False, False, False, False
                elif chapter_id == 7:
                    show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, True, False, False, False, False, False
            
            elif event.button == 1 and options_button_bool == True: # 打开选项界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, False, False, True, False
            
            elif event.button == 1 and level_button_bool == True: # 打开章节界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, True, False, False, False
            
            elif event.button == 1 and about_button_bool == True: # 打开关于界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, True, False, False, False, False
            
            elif event.button == 1 and exit_button_bool == True: # 退出游戏
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, False, True, False, False
            
            elif event.button == 1 and new_button_bool == True: # 新旅途界面
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = False, False, False, False, False, False, False, False, False, False, False, False, True
            
            else:
                show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool = True, False, False, False, False, False, False, False, False, False, False, False, False

    
    return show_homescene_bool, close_homescene_to_scene1_village_bool, close_homescene_to_scene2_highway_bool, close_homescene_to_scene3_town_bool, close_homescene_to_scene4_suburb_bool, close_homescene_to_scene5_city_bool, close_homescene_to_scene6_trainstation_bool, close_homescene_to_scene7_refuge_bool, close_homescene_to_aboutscene_bool, close_homescene_to_levelscene_bool, close_homescene_to_exitscene_bool, close_homescene_to_optionscene_bool, close_homescene_to_newscene_bool, language, runs_number, chapter_id


# 关闭主页
def close_homescene(screen, x, y, close_homescene_to_otherscene_bool, open_otherscene_bool, min_i, language, runs_number):
    # 加载屏幕大小
    screen_size = settings('screen_size')

    # 绘制背景颜色
    screen.fill(settings('background_color'))

    # 退出游戏
    exit_game()

    # 绘制关于界面基本元素内容
    homescene_base_gameobject(screen, x, y, screen_size, language, runs_number, ifopen_click = False)

    # 绘制逐渐显示的界面, 逐渐将界面隐藏
    surface = pygame.Surface(screen_size)
    surface.set_alpha(min_i)

    if min_i >= 255:
        min_i = 0
        close_homescene_to_otherscene_bool, open_otherscene_bool = False, True
    else:
        min_i = min_i + settings('animation_speed') # 帧数为120
        close_homescene_to_otherscene_bool, open_otherscene_bool = True, False

    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    
    return close_homescene_to_otherscene_bool, open_otherscene_bool, min_i, language, runs_number