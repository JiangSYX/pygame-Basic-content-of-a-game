""" 包含检测游戏对象是否在屏幕绘制范围中的函数 """
from assets.scripts.support.settings import settings # 设置


# 检测游戏对象是否在屏幕绘制范围里面
def detection_position(gameobject_coordinate):
    # 设置标志和检测范围
    if_inside = False
    ranges = 175

    # 开始检测
    if gameobject_coordinate[0] + ranges >= 0 and gameobject_coordinate[0] - ranges <= settings('screen_size')[0] and \
       gameobject_coordinate[1] + ranges >= 0 and gameobject_coordinate[1] - ranges <= settings('screen_size')[1]:
        if_inside = True
    else:
    	if_inside = False

    return if_inside