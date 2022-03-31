""" 包含关于界面基本元素内容函数 """
from assets.scripts.support.button import button # 按钮
from assets.scripts.support.game_object import game_object # 游戏对象


# 绘制关于界面基本元素内容(应用于打开关于界面, 显示关于界面和关闭关于界面)
def aboutscene_base_gameobject(screen, x, y, screen_size, language, emoticon_id, ifopen_click = False):
    # 初始化返回主页按钮
    if language == 'chinese':
        back_button_text = '返回'
    elif language == 'english':
        back_button_text = 'BACK'
    back_button_text_size = 20
    back_button_center_coordinate = (screen_size[0]/2, screen_size[1]/2+150)
    back_button_diamond_side_length = 100

    # 初始化表情包
    if emoticon_id == 1 or emoticon_id == 11 or emoticon_id == 21 or emoticon_id == 31 or emoticon_id == 41:
        emoticon = "ε(*'ω')_/`:^☆"
    elif emoticon_id == 2 or emoticon_id == 12 or emoticon_id == 22 or emoticon_id == 32 or emoticon_id == 42:
        emoticon = '(*^ω^*)'
    elif emoticon_id == 3 or emoticon_id == 13 or emoticon_id == 23 or emoticon_id == 33 or emoticon_id == 43:
        emoticon = 'ヾ(@^▽^@)ノ '
    elif emoticon_id == 4 or emoticon_id == 14 or emoticon_id == 24 or emoticon_id == 34 or emoticon_id == 44:
        emoticon = '(˙ε .)？'
    elif emoticon_id == 5 or emoticon_id == 15 or emoticon_id == 25 or emoticon_id == 35 or emoticon_id == 45:
        emoticon = '～(^з^)-☆'
    elif emoticon_id == 6 or emoticon_id == 16 or emoticon_id == 26 or emoticon_id == 36 or emoticon_id == 46:
        emoticon = '╭(°A°`)╮'
    elif emoticon_id == 7 or emoticon_id == 17 or emoticon_id == 27 or emoticon_id == 37 or emoticon_id == 47:
        emoticon = "(;｀O')o"
    elif emoticon_id == 8 or emoticon_id == 18 or emoticon_id == 28 or emoticon_id == 38 or emoticon_id == 48:
        emoticon = '╮(*‘ω’*)╭'
    elif emoticon_id == 9 or emoticon_id == 19 or emoticon_id == 29 or emoticon_id == 39 or emoticon_id == 49:
        emoticon = '(*＾3＾)/～☆'
    elif emoticon_id == 10 or emoticon_id == 20 or emoticon_id == 30 or emoticon_id == 40 or emoticon_id == 50:
        emoticon = 'ㄟ( ▔, ▔ )ㄏ'

    # 初始化左边的消息
    if language == 'chinese':
        message_left_text_1 = '这个游戏是我们的第一个项目.'
        message_left_text_2 = '希望你喜欢 :>'
    elif language == 'english':
        message_left_text_1 = 'This game is our first project.'
        message_left_text_2 = 'Wish you like it :>'

    # 初始化右边的消息
    if language == 'chinese':
        message_right_text_1 = '如果你有什么问题或者建议, 你可以给我发电子邮件.'
        message_right_text_2 = '电子邮件地址: 3124372698@qq.com'
    elif language == 'english':
        message_right_text_1 = 'If you have any questions or suggestions, you can email me.'
        message_right_text_2 = 'E-mail address: 3124372698@qq.com'

    # 绘制按钮
    if language == 'chinese':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click)
    elif language == 'english':
        back_button_bool = button(screen, x, y, back_button_text, back_button_text_size, back_button_center_coordinate, back_button_diamond_side_length, ifopen_click = ifopen_click, language = 'english')

    # 绘制表情包
    game_object(screen, size = 22, text = emoticon, coordinate = (screen_size[0]/2, screen_size[1]/2-200))

    if language == 'chinese':
        # 绘制左边的消息
        game_object(screen, size = 22, text = message_left_text_1, coordinate = (screen_size[0]/2, screen_size[1]/2-130), coordinate_type = 'center')
        game_object(screen, size = 22, text = message_left_text_2, coordinate = (screen_size[0]/2, screen_size[1]/2-100), coordinate_type = 'center')
        # 绘制右边的消息
        game_object(screen, size = 22, text = message_right_text_1, coordinate = (screen_size[0]/2, screen_size[1]/2-15), coordinate_type = 'center')
        game_object(screen, size = 22, text = message_right_text_2, coordinate = (screen_size[0]/2, screen_size[1]/2+15), coordinate_type = 'center')
    elif language == 'english':
        # 绘制左边的消息
        game_object(screen, size = 22, text = message_left_text_1, coordinate = (screen_size[0]/2, screen_size[1]/2-130), coordinate_type = 'center', language = 'english')
        game_object(screen, size = 22, text = message_left_text_2, coordinate = (screen_size[0]/2, screen_size[1]/2-100), coordinate_type = 'center', language = 'english')
        # 绘制右边的消息
        game_object(screen, size = 22, text = message_right_text_1, coordinate = (screen_size[0]/2, screen_size[1]/2-15), coordinate_type = 'center', language = 'english')
        game_object(screen, size = 22, text = message_right_text_2, coordinate = (screen_size[0]/2, screen_size[1]/2+15), coordinate_type = 'center', language = 'english')

    # 根据是否打开点击处理而返回按钮点击标志
    if ifopen_click == True:
        return back_button_bool