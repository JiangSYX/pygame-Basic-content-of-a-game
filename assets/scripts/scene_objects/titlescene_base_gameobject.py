""" 包含标题界面基本元素内容函数 """
import pygame

from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 绘制标题界面基本元素内容(应用于打开标题界面, 显示标题界面和关闭标题界面)
def titlescene_base_gameobject(screen, screen_size):
    # 绘制主标题和副标题
    game_object(screen, size = 75, text = '文字游戏', coordinate = (screen_size[0]/2, screen_size[1]/2-50))
    game_object(screen, size = 35, text = '基因突变', coordinate = (screen_size[0]/2, screen_size[1]/2+75))