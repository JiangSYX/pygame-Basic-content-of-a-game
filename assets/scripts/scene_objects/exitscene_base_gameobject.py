""" 包含退出界面基本元素内容函数 """
from assets.scripts.support.button import button # 按钮
from assets.scripts.support.game_object import game_object # 游戏对象


# 绘制退出界面的基本元素内容(应用于打开退出界面, 显示退出界面, 关闭退出界面)
def exitscene_base_gameobject(screen, x, y, screen_size, language, ifopen_click = False):
    # 初始化返回主页按钮
    if language == 'chinese':
        back_button_text = '取消'
    elif language == 'english':
        back_button_text = 'NO'
    back_button_text_size = 20
    back_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2+100)
    back_button_diamond_side_length = 100

    # 初始化退出游戏按钮
    if language == 'chinese':
        exit_button_text = '确定'
    elif language == 'english':
        exit_button_text = 'YES'
    exit_button_text_size = 20
    exit_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2)
    exit_button_diamond_side_length = 100

    # 绘制消息
    if language == 'chinese':
        game_object(screen, size = 50, text = '是否退出游戏', coordinate = (screen_size[0]/2, screen_size[1]/2-125))
    elif language == 'english':
        game_object(screen, size = 50, text = 'Exit the Game', coordinate = (screen_size[0]/2, screen_size[1]/2-125), language = 'english')

    # 绘制按钮
    if language == 'chinese':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click)
        exit_button_bool = button(screen, x, y, exit_button_text, back_button_text_size, exit_button_center_coordinate, exit_button_diamond_side_length, ifopen_click = ifopen_click)
    elif language == 'english':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')
        exit_button_bool = button(screen, x, y, exit_button_text, back_button_text_size, exit_button_center_coordinate, exit_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')

    # 根据是否打开点击处理而返回按钮点击标志
    if ifopen_click == True:
        return back_button_bool, exit_button_bool