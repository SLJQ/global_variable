def _init():
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    _global_dict[key] = value


def get_value(key):
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
    
