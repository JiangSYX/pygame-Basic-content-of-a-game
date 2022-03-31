""" 包含绘制菜单界面基础元素内容函数 """
import pygame

from assets.scripts.support.button import button # 按钮
from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 绘制菜单
def draw_menu(screen, x, y, home_button_bool, backgame_button_bool, menuexit_button_bool):
    # 初始化屏幕大小
    screen_size = settings('screen_size')

    # 绘制半透明膜
    surface = pygame.Surface(screen_size)
    surface.set_alpha(128)
    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))

    # 初始化返回主页按钮
    home_button_text = '主页'
    home_button_text_size = 20
    home_button_center_coordinate = (screen_size[0]/2+150, screen_size[1]/2)
    home_button_diamond_side_length = 100

    # 初始化返回游戏按钮
    backgame_button_text = '返回旅途'
    backgame_button_text_size = 25
    backgame_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2)
    backgame_button_diamond_side_length = 200

    # 初始化退出游戏按钮
    exit_button_text = '退出'
    exit_button_text_size = 20
    exit_button_center_coordinate = (screen_size[0]/2-150, screen_size[1]/2)
    exit_button_diamond_side_length = 100

    # 绘制返回主页按钮
    home_button_bool = button(screen, x, y, home_button_text, home_button_text_size, home_button_center_coordinate, home_button_diamond_side_length, ifopen_click = True)
    backgame_button_bool = button(screen, x, y, backgame_button_text, backgame_button_text_size, backgame_button_center_coordinate, backgame_button_diamond_side_length, ifopen_click = True)
    menuexit_button_bool = button(screen, x, y, exit_button_text, exit_button_text_size, exit_button_center_coordinate, exit_button_diamond_side_length, ifopen_click = True)

    # 返回鼠标在按钮上面的标志
    return home_button_bool, backgame_button_bool, menuexit_button_bool