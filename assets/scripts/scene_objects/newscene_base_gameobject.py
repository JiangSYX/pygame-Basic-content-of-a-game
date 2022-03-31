""" 包含新游戏界面基本元素内容函数 """
from assets.scripts.support.button import button # 按钮
from assets.scripts.support.game_object import game_object # 游戏对象


# 绘制新游戏界面基本元素内容(应用于打开新游戏界面, 显示新游戏界面和关闭新游戏界面)
def newscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = False):
    # 初始化返回主页按钮
    if language == 'chinese':
        back_button_text = '取消'
    elif language == 'english':
        back_button_text = 'NO'
    back_button_text_size = 20
    back_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2+100)
    back_button_diamond_side_length = 100

    # 初始化确定按钮
    if language == 'chinese':
        yes_button_text = '确定'
    elif language == 'english':
        yes_button_text = 'YES'
    yes_button_text_size = 20
    yes_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2)
    yes_button_diamond_side_length = 100

    # 绘制消息
    if language == 'chinese':
        game_object(screen, size = 50, text = '是否创建新旅途', coordinate = (screen_size[0]/2, screen_size[1]/2-125))
    elif language == 'english':
        game_object(screen, size = 50, text = 'Build a New Journey', coordinate = (screen_size[0]/2, screen_size[1]/2-125), language = 'english')

    # 绘制按钮
    if language == 'chinese':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click)
        yes_button_bool = button(screen, x, y, yes_button_text, yes_button_text_size, yes_button_center_coordinate, yes_button_diamond_side_length, ifopen_click = ifopen_click)
    elif language == 'english':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        yes_button_bool = button(screen, x, y, yes_button_text, yes_button_text_size, yes_button_center_coordinate, yes_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')

    # 根据是否打开点击处理而返回按钮点击标志
    if ifopen_click == True:
        return back_button_bool, yes_button_bool