""" 包含退出游戏函数 """
import pygame

from sys import exit # 退出

pygame.init()


# 退出游戏
def exit_game(ifget_esc = None, ifget_enter = None):
    get_esc, get_enter = False, False
    # 响应键盘
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
        elif event.type == pygame.KEYDOWN: # 如果玩家按esc键, 则退出游戏
            if event.key == pygame.K_ESCAPE and ifget_esc == True:
                get_esc, get_enter = True, False
            elif event.key == pygame.K_RETURN and ifget_enter == True: # 如果玩家按确定键, 则跳过当前场景
                get_esc, get_enter = False, True
        else:
            get_esc, get_enter = False, False
    return get_esc, get_enter