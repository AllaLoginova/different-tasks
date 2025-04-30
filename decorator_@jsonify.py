''' Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON. 

@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}
    
print(make_user(4, False, None))
=> {"id": 4, "live": false, "options": null}

'''

import functools, json

def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        res = json.dumps(val)
        return res
    return wrapper
