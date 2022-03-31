""" 包含文字化射击声音和射击函数 """
import pygame

from math import sqrt, asin, pi # 开方, 反正弦, 圆周率
from assets.scripts.support.detection_position import detection_position # 检测位置
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 开枪射击的文字化声音
def text_sound_shoot(screen, player_coordinate, player_rect, x, y):
    # 创建文字声音
    shoot_sound_text = '砰'
    shoot_sound_size = settings('text_sound_size')

    # 计算鼠标相对与坐标系的角度值(当鼠标不在角色正中间时计算)
    if x != player_coordinate[0] and y != player_coordinate[1]:
        angle = asin(abs(player_coordinate[1] - y)/sqrt(pow(x - player_coordinate[0], 2) + pow(y - player_coordinate[1], 2))) * 180 / pi
    else:
        angle = 360 # 鼠标在角色中间, 角度为360度

    # 初始化文字声音的坐标(根据鼠标相对于角色方向设置坐标)
    # 鼠标在角色正中间
    if x == player_coordinate[0] and y == player_coordinate[1]:
        sound_coordinate_type = 'center'
        shoot_sound_coordinate = player_coordinate

    # 鼠标在角色的右边(鼠标在角色右边而且鼠标在45度的扇形区域中(x上面小于或等于24.5度, x下面大于或等于24.5度))
    elif x >= player_coordinate[0] and angle <= 45/2:
        sound_coordinate_type = 'left_centery'
        shoot_sound_coordinate = (player_coordinate[0] + player_rect.width/2, player_coordinate[1])

    # 鼠标在角色右上方(鼠标在角色右边和上面而且鼠标在45度的扇形区域中(大于24.5度, 小于45+24.5度))
    elif x >= player_coordinate[0] and y <= player_coordinate[1] and angle > 45/2 and angle < 45 + 45/2:
        sound_coordinate_type = 'left_centery'
        shoot_sound_coordinate = (player_coordinate[0] + player_rect.width/2, player_coordinate[1] - player_rect.height/2)
    
    # 鼠标在角色右下方(鼠标在角色右边和下面而且鼠标在45度的扇形区域中(大于24.5度, 小于45+24.5度))
    elif x >= player_coordinate[0] and y >= player_coordinate[1] and angle > 45/2 and angle < 45 + 45/2:
        sound_coordinate_type = 'left_centery'
        shoot_sound_coordinate = (player_coordinate[0] + player_rect.width/2, player_coordinate[1] + player_rect.height/2)

    # 鼠标在角色上面(鼠标在角色上面而且鼠标在45度扇形区域中(y左边24.5度, y右边24.5度, 包括等于))
    elif y < player_coordinate[1] and angle >= 45 + 45/2:
        sound_coordinate_type = 'centerx_bottom'
        shoot_sound_coordinate = (player_coordinate[0], player_coordinate[1] - player_rect.height/2)

    # 鼠标在角色下面(鼠标在角色下面而且鼠标在45度扇形区域中(y左边24.5度, y右边24.5度, 包括等于))
    elif y > player_coordinate[1] and angle >= 45 + 45/2:
        sound_coordinate_type = 'centerx_top'
        shoot_sound_coordinate = (player_coordinate[0], player_coordinate[1] + player_rect.height/2)

    # 附属检测(消除上下与左右的冲突)(当前检测鼠标在角色右边)
    elif y == player_coordinate[1] and x >= player_coordinate[0] and angle >= 45 + 45/2:
        sound_coordinate_type = 'left_centery'
        shoot_sound_coordinate = (player_coordinate[0] + player_rect.width/2, player_coordinate[1])

    # 附属检测(消除上下与左右的冲突)(当前检测鼠标在角色左边)
    elif y == player_coordinate[1] and x <= player_coordinate[0] and angle >= 45 + 45/2:
        sound_coordinate_type = 'right_centery'
        shoot_sound_coordinate = (player_coordinate[0] - player_rect.width/2, player_coordinate[1])

    # 鼠标在角色左边(鼠标在角色左边而且鼠标在45度扇形区域中(x上面小于或等于24.5度, x下面大于或等于24.5度))
    elif x <= player_coordinate[0] and angle <= 45/2:
        sound_coordinate_type = 'right_centery'
        shoot_sound_coordinate = (player_coordinate[0] - player_rect.width/2, player_coordinate[1])

    # 鼠标在角色左上方(鼠标在角色左边和上面而且鼠标在45度扇形区域中(大于24.5度, 小于45+24.5度))
    elif x <= player_coordinate[0] and y <= player_coordinate[1] and angle > 45/2 and angle < 45 + 45/2:
        sound_coordinate_type = 'right_centery'
        shoot_sound_coordinate = (player_coordinate[0] - player_rect.width/2, player_coordinate[1] - player_rect.height/2)
    
    # 鼠标在角色左下方(鼠标在角色左边和下面而且鼠标在45度扇形区域中(大于24.5度, 小于45+25.5度))
    elif x <= player_coordinate[0] and y >= player_coordinate[1] and angle > 45/2 and angle < 45 + 45/2:
        sound_coordinate_type = 'right_centery'
        shoot_sound_coordinate = (player_coordinate[0] - player_rect.width/2, player_coordinate[1] + player_rect.height/2)

    # 绘制文字声音
    game_object(screen, size = shoot_sound_size, text = shoot_sound_text, coordinate = shoot_sound_coordinate, coordinate_type = sound_coordinate_type)


# 绘制子弹并让子弹移动
def draw_bullets(screen, Bullets):
    # 初始化子弹到屏幕绘制范围外的id列表
    over_bullets_id = []

    # 遍历字典, 根据每个子弹的参数绘制子弹
    for i, Parameter in Bullets.items():
        # 从参数字典获取子弹参数(first_coordinate = coordinate)
        first_coordinate = Parameter['coordinate'] # 子弹的头坐标
        sin = Parameter['sin'] # 水平夹角的sin值
        cos = Parameter['cos'] # 水平夹角的cos值
        quadrant = Parameter['quadrant'] # 象限

        # 根据象限计算子弹的头坐标和尾坐标(原点使用随机象限代替)
        if quadrant == 1: # 第一象限
            first_coordinate = (first_coordinate[0] + (settings('bullets_speed') * cos), first_coordinate[1] - (settings('bullets_speed') * sin))
            last_coordinate = (first_coordinate[0] + ((settings('bullets_speed') + settings('bullets_length')) * cos), first_coordinate[1] - ((settings('bullets_speed') + settings('bullets_length')) * sin))
        elif quadrant == 2: # 第二象限
            first_coordinate = (first_coordinate[0] - (settings('bullets_speed') * cos), first_coordinate[1] - (settings('bullets_speed') * sin))
            last_coordinate = (first_coordinate[0] - ((settings('bullets_speed') + settings('bullets_length')) * cos), first_coordinate[1] - ((settings('bullets_speed') + settings('bullets_length')) * sin))
        elif quadrant == 3: # 第三象限
            first_coordinate = (first_coordinate[0] - (settings('bullets_speed') * cos), first_coordinate[1] + (settings('bullets_speed') * sin))
            last_coordinate = (first_coordinate[0] - ((settings('bullets_speed') + settings('bullets_length')) * cos), first_coordinate[1] + ((settings('bullets_speed') + settings('bullets_length')) * sin))
        elif quadrant == 4: # 第四象限
            first_coordinate = (first_coordinate[0] + (settings('bullets_speed') * cos), first_coordinate[1] + (settings('bullets_speed') * sin))
            last_coordinate = (first_coordinate[0] + ((settings('bullets_speed') + settings('bullets_length')) * cos), first_coordinate[1] + ((settings('bullets_speed') + settings('bullets_length')) * sin))

        # 绘制子弹
        bullets_rect = pygame.draw.aaline(screen, settings('text_color'), first_coordinate, last_coordinate, settings('bullets_width'))
    
        # 更新子弹参数和字典
        coordinate = first_coordinate # 更新子弹坐标

        Parameter['coordinate'] = coordinate # 更新参数字典的坐标
        Parameter['bullets_rect'] = bullets_rect # 更新参数字典的子弹矩形信息

        Bullets[i] = Parameter # 更新子弹字典

        # 检测子弹是否在屏幕绘制范围外面
        if detection_position(coordinate) == False:
            over_bullets_id.append(i)

    # 删除无效子弹
    for over_i in over_bullets_id:
        del Bullets[over_i]

    # 返回子弹字典
    return Bullets


# 开枪射击
def shoot(screen, x, y, player_coordinate, player_rect, if_open_agnifying, if_shoot, bullets_number, if_draw_bullets, bullets_coordinate, bullets_id, Bullets):
    # 限制瞄准点的范围
    if if_open_agnifying == True: # 打开倍镜
        radius = 300
    elif if_open_agnifying == False: # 关闭倍镜(普通状态)
        radius = 150

    # 当前鼠标的坐标到角色的距离
    distance_mouse_to_player = (sqrt(pow(x - player_coordinate[0], 2) + pow(y - player_coordinate[1], 2)))

    # 开始检测鼠标是否超出范围
    if distance_mouse_to_player > radius: # 鼠标超出范围
        # 获取新的鼠标坐标
        if x > player_coordinate[0] and y <= player_coordinate[1]: # 鼠标在以角色坐标为原点的坐标系的第一象限(包括正x)
            x = int(player_coordinate[0] + ((x - player_coordinate[0]) * radius) / distance_mouse_to_player)
            y = int(player_coordinate[1] - ((player_coordinate[1] - y) * radius) / distance_mouse_to_player)

        elif x <= player_coordinate[0] and y < player_coordinate[1]: # 鼠标在以角色坐标为原点的坐标系的第二象限(包括正y)
            x = int(player_coordinate[0] - ((player_coordinate[0] - x) * radius) / distance_mouse_to_player)
            y = int(player_coordinate[1] - ((player_coordinate[1] - y) * radius) / distance_mouse_to_player)
        
        elif x < player_coordinate[0] and y >= player_coordinate[1]: # 鼠标在以角色坐标为原点的坐标系的第三象限(包括负x)
            x = int(player_coordinate[0] - ((player_coordinate[0] - x) * radius) / distance_mouse_to_player)
            y = int(player_coordinate[1] + ((y - player_coordinate[1]) * radius) / distance_mouse_to_player)
        
        elif x >= player_coordinate[0] and y > player_coordinate[1]: # 鼠标在以角色坐标为原点的坐标系的第四象限(包括负y)
            x = int(player_coordinate[0] + ((x - player_coordinate[0]) * radius) / distance_mouse_to_player)
            y = int(player_coordinate[1] + ((y - player_coordinate[1]) * radius) / distance_mouse_to_player)
        
        # 设置鼠标位置
        pygame.mouse.set_pos((x, y))
    
    else: # 鼠标没有超出范围, 跳过计算(不需要设置坐标)
        pass

    # 绘制瞄准点
    pygame.draw.line(screen, settings('text_color'), (x + 4, y), (x + 12, y), 2)
    pygame.draw.line(screen, settings('text_color'), (x, y - 4), (x, y - 12), 2)
    pygame.draw.line(screen, settings('text_color'), (x - 4, y), (x - 12, y), 2)
    pygame.draw.line(screen, settings('text_color'), (x, y + 4), (x, y + 12), 2)

    # 射击
    if if_shoot == True:
        # 允许绘制子弹
        if_draw_bullets = True

    # 绘制子弹
    if if_draw_bullets == True:
        Bullets = draw_bullets(screen, Bullets)

    return x, y, if_open_agnifying, if_shoot, bullets_number, if_draw_bullets, bullets_coordinate, bullets_id, Bullets