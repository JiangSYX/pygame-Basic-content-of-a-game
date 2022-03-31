""" 包含绘制游戏对象的函数 """
from assets.scripts.support.bullets_collision import bullets_collision # 子弹碰撞检测
from assets.scripts.support.detection_position import detection_position # 检测位置
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.process_collision import collision_detection, ifopen_collision_detection # 碰撞检测, 是否打开碰撞检测


def draw_objects(screen, text, text_size, object_coordinate, player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_dictionaries, enter_key, vertical = False, antialiased = True, if_detection = True):
    if detection_position(object_coordinate) == True: # 检测游戏对象是否在屏幕绘制范围内
        # 加载移动标志
        up_bool, down_bool, left_bool, right_bool = object_dictionaries['up_bool'], object_dictionaries['down_bool'], object_dictionaries['left_bool'], object_dictionaries['right_bool']
        if_up, if_down, if_left, if_right = object_dictionaries['if_up'], object_dictionaries['if_down'], object_dictionaries['if_left'], object_dictionaries['if_right']

        # 绘制游戏对象
        object_rect = game_object(screen, size = text_size, text = text, coordinate = object_coordinate, ifreturn = True, vertical = vertical, antialiased = antialiased)
        
        # 角色与游戏对象的碰撞检测(开启条件: 在绘制范围以及在检测范围)
        if ifopen_collision_detection(object_coordinate) == True and if_detection == True: # 检测是否开启碰撞检测
            up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, enter_key = collision_detection(player_coordinate, object_coordinate, player_rect, object_rect, up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, enter_key)

        # 游戏对象与子弹的碰撞检测(开启条件: 在绘制范围)
        if draw_menuscene == False and player_health > 0:
            Bullets, player_coordinate, object_coordinate, object_rect = bullets_collision(screen, Bullets, player_coordinate, object_coordinate, object_rect)

        # 修改游戏对象字典
        object_dictionaries['up_bool'], object_dictionaries['down_bool'], object_dictionaries['left_bool'], object_dictionaries['right_bool'] = up_bool, down_bool, left_bool, right_bool
        object_dictionaries['if_up'], object_dictionaries['if_down'], object_dictionaries['if_left'], object_dictionaries['if_right'] = if_up, if_down, if_left, if_right

    return player_coordinate, player_rect, player_health, draw_menuscene, Bullets, object_dictionaries, enter_key