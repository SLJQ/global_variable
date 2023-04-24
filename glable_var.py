def _init():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    # 定义一个全局变量
    _global_dict[key] = value


def get_value(key):
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _global_dict[key]
    except KeyError:
        print('读取' + key + '失败\r\n')


def delete_value(key):
    _global_dict.pop(key)
    return _global_dict


def value_exist(key):
    return key in _global_dict.keys()


def read_values():
    for key in _global_dict.keys():
        print('{}\t{}'.format(key,_global_dict[key]))
        
        
def read_value(key):
    try:
        print('{}\t{}'.format(key,_global_dict[key]))
    except KeyError:
        print('读取' + key + '失败\r\n')
    
