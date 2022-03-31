""" 包含记录每一个游戏对象标志的函数 """


def record_sign(up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, Dictionaries, enter_key):
	# 初始化标志列表
    up_bool_list, down_bool_list, left_bool_list, right_bool_list = [], [], [], []
    if_up_list, if_down_list, if_left_list, if_right_list = [], [], [], []

    # 读取每一个游戏对象的标志并记录下来
    for dictionarie in Dictionaries:
        up_bool_list.append(dictionarie['up_bool'])
        down_bool_list.append(dictionarie['down_bool'])
        left_bool_list.append(dictionarie['left_bool'])
        right_bool_list.append(dictionarie['right_bool'])
        if_up_list.append(dictionarie['if_up'])
        if_down_list.append(dictionarie['if_down'])
        if_left_list.append(dictionarie['if_left'])
        if_right_list.append(dictionarie['if_right'])

    # 根据列表处理主标志. 如果全部为True, 则主标志为True. 如果其中一个为False, 则主标志为False
    # # up_bool
    if up_bool_list.count(True) == len(up_bool_list):
        up_bool = True
    elif False in up_bool_list:
        up_bool = False

    # # down_bool
    if down_bool_list.count(True) == len(down_bool_list):
    	down_bool = True
    elif False in down_bool_list:
    	down_bool = False

    # # left_bool
    if left_bool_list.count(True) == len(left_bool_list):
    	left_bool = True
    elif False in left_bool_list:
    	left_bool = False

    # # right_bool
    if right_bool_list.count(True) == len(right_bool_list):
    	right_bool = True
    elif False in right_bool_list:
    	right_bool = False

    # # if_up
    if if_up_list.count(True) == len(if_up_list):
        if_up = True
    elif False in if_up_list:
        if_up = False

    # # if_down
    if if_down_list.count(True) == len(if_down_list):
    	if_down = True
    elif False in if_down_list:
    	if_down = False

    # # if_left
    if if_left_list.count(True) == len(if_left_list):
    	if_left = True
    elif False in if_left_list:
    	if_left = False

    # # if_right
    if if_right_list.count(True) == len(if_right_list):
    	if_right = True
    elif False in if_right_list:
    	if_right = False

    # 根据enter_key来处理if_xxx为真时xxx_bool是否为真还是为假
    if if_up == True:
        if enter_key['enter_s'] == True:
            up_bool = True
    if if_down == True:
        if enter_key['enter_w'] == True:
            down_bool = True
    if if_left == True:
        if enter_key['enter_d'] == True:
            left_bool = True
    if if_right == True:
        if enter_key['enter_a'] == True:
            right_bool = True

    # 返回主标志
    return up_bool, down_bool, left_bool, right_bool, if_up, if_down, if_left, if_right, enter_key