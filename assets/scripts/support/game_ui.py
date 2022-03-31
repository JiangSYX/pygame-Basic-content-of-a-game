""" 包含游戏ui函数 """
import pygame

from math import sqrt # 开方
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 游戏UI
def game_UI(screen, player_health, bullets_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, draw_blood_strip, scene_name):
    # 初始化UI参数
    screen_size = settings('screen_size') # 获取屏幕大小
    uitext_size = 23 # 普通UI文字字体大小
    chapter_name_size = 35 # 场景名字字体大小

    wait_time = 0 # 绘制场景名字的等待时间
    show_time = 3 # 绘制时间
    speed = 3 # 显示与隐藏速度
    end_speed = 5 # 结尾透明化文字背景速度

    chapter_name_coordinate = (45, screen_size[1] - 250) # 章节名字坐标
    player_health_coordinate = (55, 55) # 生命值菱形的中心坐标

    diamond_side_length = 70 # 背景菱形的边长
    icon_size = 25 # 回血药图标, 子弹图标大小
    icon_angle = 3 # 回血药图标, 子弹图标角度
    blood_strip_length, blood_strip_height = 450, 10 # 血条的长度和高度

    zero_health = 0.5 # 生命值等于0时血条需要绘制的生命值

    diamond_half_height = (int(sqrt(2))/2)*diamond_side_length # 菱形背景框的半高


    # 初始化菱形背景的坐标
    diamond_coordinate_left = (player_health_coordinate[0] - diamond_half_height, player_health_coordinate[1]) 
    diamond_coordinate_up = (player_health_coordinate[0], player_health_coordinate[1] - diamond_half_height)
    diamond_coordinate_right = (player_health_coordinate[0] + diamond_half_height, player_health_coordinate[1])
    diamond_coordinate_down = (player_health_coordinate[0], player_health_coordinate[1] + diamond_half_height)

    # 初始化血条背景的坐标
    blood_strip_coordinate = (screen_size[0]/2 - blood_strip_length/2, 40 - blood_strip_height/2)


    if draw_blood_strip == True:
        # 绘制血条背景
        pygame.draw.rect(screen, settings('background_color'), (blood_strip_coordinate[0], blood_strip_coordinate[1], blood_strip_length, blood_strip_height), 0)
        pygame.draw.rect(screen, settings('text_color'), (blood_strip_coordinate[0], blood_strip_coordinate[1], blood_strip_length, blood_strip_height), 1)
    
        # 根据生命值绘制血条
        if player_health == 0: # 处理生命值等于0的时候
            pygame.draw.rect(screen, settings('button_above_color'), (blood_strip_coordinate[0] + 1, blood_strip_coordinate[1] + 1, (blood_strip_length - (100 - zero_health)*(blood_strip_length/100)) - 2, blood_strip_height - 2), 0)
        else:
            pygame.draw.rect(screen, settings('button_above_color'), (blood_strip_coordinate[0] + 1, blood_strip_coordinate[1] + 1, (blood_strip_length - (100 - player_health)*(blood_strip_length/100)) - 2, blood_strip_height - 2), 0)

    """
    # 绘制生命值菱形背景
    pygame.draw.polygon(screen, settings('background_color'), [diamond_coordinate_left, diamond_coordinate_up, diamond_coordinate_right, diamond_coordinate_down], 0)
    pygame.draw.polygon(screen, settings('text_color'), [diamond_coordinate_left, diamond_coordinate_up, diamond_coordinate_right, diamond_coordinate_down], 2)

    # 绘制生命值
    game_object(screen, size = uitext_size, text = str(player_health), coordinate = player_health_coordinate, coordinate_type = 'center')
    """

    # 等待绘制章节时间
    if draw_chapter_name == False:
        if i == int(settings('fps') * wait_time):
            draw_chapter_name = True # 时间到后开始绘制章节名字
        else:
            if draw_menuscene == False: # 如果不允许绘制菜单, 则计数器继续工作
                i = i + 1

    # 开始绘制章节名字
    if draw_chapter_name == True:
        # 根据章节绘制章节名字(有背景颜色)
        chapter_name_rect = game_object(screen, size = chapter_name_size, text = scene_name, coordinate = chapter_name_coordinate, coordinate_type = 'topleft', ifreturn = True, language = 'chinese', bgcolor = settings('background_color'))

        # 绘制逐渐隐藏的界面, 逐渐显示章节标题
        if i <= int(settings('fps') * wait_time) + int(255/speed): # 计算绘制条件
            surface = pygame.Surface((chapter_name_rect.width, chapter_name_rect.height))
            surface.set_alpha(max_i)

            # 更新计数器
            if max_i <= 0:
                max_i = 0 # 保持数据
            else:
                if draw_menuscene == False: # 如果不允许绘制菜单, 则计数器继续工作
                    max_i = max_i - speed

            surface.fill(settings('background_color'))
            screen.blit(surface, (chapter_name_coordinate[0], chapter_name_coordinate[1]))

        # 绘制逐渐显示的界面, 逐渐隐藏章节标题
        if i >= int(settings('fps') * (wait_time + show_time)) - int(255/speed): # 计算绘制条件
            surface = pygame.Surface((chapter_name_rect.width, chapter_name_rect.height))
            surface.set_alpha(min_i)

            # 更新计数器
            if min_i >= 255:
                min_i = 255 # 保持数据
            else:
                if draw_menuscene == False: # 如果不允许绘制菜单, 则计数器继续工作
                    min_i = min_i + speed
            
            surface.fill(settings('background_color'))
            screen.blit(surface, (chapter_name_coordinate[0], chapter_name_coordinate[1]))
        
        # 限制章节名字显示时间
        if i == int(settings('fps') * (wait_time + show_time)):
            i, min_i, max_i = 0, 0, 255 # 重新初始化计数器
            draw_chapter_name = 'END' # 时间到后进入结尾状态
        else:
            if draw_menuscene == False: # 如果不允许绘制菜单, 则计数器继续工作
                i = i + 1

    # 结尾工作, 让文字背景逐渐透明
    if draw_chapter_name == 'END':
        # 根据章节获取章节名字的rect(不绘制文字)
        chapter_name_rect = game_object(screen, size = chapter_name_size, text = scene_name, coordinate = chapter_name_coordinate, coordinate_type = 'topleft', ifreturn = True, if_draw = False)
        
        surface = pygame.Surface((chapter_name_rect.width, chapter_name_rect.height))
        surface.set_alpha(max_i)

        # 更新计数器
        if max_i <= 0:
            i, min_i, max_i = 0, 0, 255 # 重新初始化计数器
            draw_chapter_name = None # 时间到后结束绘制
        else:
            if draw_menuscene == False: # 如果不允许绘制菜单, 则计数器继续工作
                max_i = max_i - end_speed

        surface.fill(settings('background_color'))
        screen.blit(surface, (chapter_name_coordinate[0], chapter_name_coordinate[1]))

    # 返回玩家生命值, 子弹数量
    return player_health, bullets_number, draw_chapter_name, i, min_i, max_i, draw_menuscene, draw_blood_strip