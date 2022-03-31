""" 包含开始界面基本元素内容函数 """
import pygame

from assets.scripts.support.settings import settings # 设置

pygame.init()


# 绘制开始界面基本元素内容(应用于打开开始界面, 显示开始界面和关闭开始界面)
def startscene_base_gameobject(screen, screen_size):
    # 绘制我的logo
    mine_logo_image = pygame.image.load(settings('mine_logo'))
    screen.blit(mine_logo_image, (screen_size[0]/2-150, screen_size[1]/2-150))