""" 包含加载界面基础元素内容函数 """
import pygame

from assets.scripts.support.game_object import game_object # 游戏对象
from assets.scripts.support.settings import settings # 设置

pygame.init()


# 加载界面基础元素内容
def loadscene_base_gameobject(screen, screen_size, chapter_id, i = 0, time = 1, message_id = None):
	# 初始化数据
    if chapter_id == 1:
        chapter_name = '乡村'
        background_text = 'I'
    elif chapter_id == 2:
        chapter_name = '公路'
        background_text = 'II'
    elif chapter_id == 3:
        chapter_name = '小镇'
        background_text = 'III'
    elif chapter_id == 4:
        chapter_name = '郊区'
        background_text = 'IV'
    elif chapter_id == 5:
        chapter_name = '城市'
        background_text = 'V'
    elif chapter_id == 6:
        chapter_name = '火车站'
        background_text = 'VI'
    elif chapter_id == 7:
        chapter_name = '避难所'
        background_text = 'VII'

    # 绘制信息
    if message_id == 1:
        message_1 = '一直扫射很累的, 尝试一下精准射击吧.'
        message_2 = '持续射击时射击系统会微调角色系统的鼠标灵敏度'
    elif message_id == 2:
        message_1 = '累了可以直接睡觉, 从菜单界面退出游戏吧.'
        message_2 = '每次循环主程序都会调用一次存储系统保存数据'
    elif message_id == 3:
        message_1 = '目标太远了? 你可以打开倍镜.'
        message_2 = '按住鼠标右键时准星的移动范围将变大'
    elif message_id == 4:
        message_1 = '丧尸会进化的, 所以快点跑!'
        message_2 = '丧尸通过神经网络算法来寻找角色的位置'
    elif message_id == 5:
        message_1 = '边听音乐边玩可以不会感觉太单调.'
        message_2 = '抱歉没有背景音乐, 因为实在没有合适的'
    elif message_id == 6:
        message_1 = '丧尸来咯, TNN的, 为什么不杀?'
        message_2 = '接触角色的丧尸越多, 血量损失的越多, 低血量玩家速度将变慢'
    elif message_id == 7:
        message_1 = '鼠标坏了, 键盘来凑, 干净又卫生.'
        message_2 = '每一个场景的按钮从左到右都对应着一个数字按键'
    elif message_id == 8:
        message_1 = '这些丧尸超逊的啦, 比binbin还逊.'
        message_2 = '丧尸的数量和每只丧尸的参数是不变的, 参数镶嵌于程序中'
    elif message_id == 9:
        message_1 = '个人觉得绘制UI有点丑, 所以我把决定权给你'
        message_2 = '按[tab]键可以显示或者隐藏血条, 默认为显示血条'
    elif message_id == 10:
        message_1 = '你这子弹多少钱一斤啊? —— 20块钱一斤'
        message_2 = '子弹的数量是无限的, 但是屏幕上最多只能存在20颗子弹'
    game_object(screen, size = 23, text = message_1, coordinate = (screen_size[0]/2, screen_size[1]/2+245), coordinate_type = 'center')
    game_object(screen, size = 20, text = message_2, coordinate = (screen_size[0]/2, screen_size[1]/2+275), coordinate_type = 'center')

    # 绘制文字背景
    """
    game_object(screen, size = 500, text = background_text, coordinate = (screen_size[0]/2, screen_size[1]/2), language = 'english', change_color = True, new_color = settings('button_above_color'))
    surface = pygame.Surface(screen_size)
    surface.set_alpha(128)
    surface.fill(settings('background_color'))
    screen.blit(surface, (0, 0))
    """

    # 绘制当前章节名字
    game_object(screen, size = 100, text = chapter_name, coordinate = (screen_size[0]/2, screen_size[1]/2-50))

    # 绘制进度条
    pygame.draw.rect(screen, settings('text_color'), (screen_size[0]/2-201, screen_size[1]/2+140, 402, 10), 1)
    pygame.draw.rect(screen, settings('button_above_color'), (screen_size[0]/2-200, screen_size[1]/2+141, i*(400/settings('fps'))/time, 8), 0)