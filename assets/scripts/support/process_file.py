""" 包含读取和写入文件的函数 """
import json


# 读取文件
def read_file(file, base_data):
    try:
        with open(file) as objects:
            output = json.load(objects)
    except FileNotFoundError:
        output = base_data
        with open(file, 'w') as file:
            json.dump(output, file)
    except json.decoder.JSONDecodeError:
        output = base_data
        with open(file, 'w') as file:
            json.dump(output, file)
    return output


# 写入文件
def write_file(file, data):
    with open(file, 'w') as objects:
        json.dump(data, objects)