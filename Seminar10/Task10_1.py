# Задача 10_1. Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
#
# seq(3)
# seq(8)
# seq(100)
# seq(8)
# seq(3)
# seq(100)


import datetime
import time


 # журнал записи
def log_func(log_lvl=0):       
    def logger2(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'  # дата и время
            if log_lvl >= 1:
                log_msg += f'функция: {func.__name__}\t'    # имя функции
                if log_lvl == 2:
                    log_msg += f"параметры: {', '.join(map(str, args))}\t"
            res = func(*args, **kwargs)
            log_msg += f'результат: {res}\n'
            with open('log_file.log', 'a', encoding='utf-8') as fp:
                fp.write(log_msg)
            return res

        return wrapper

    return logger2


# замеряем время выполнения функции
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()              # время начала (в наносекундах)
        res = func(*args, **kwargs)
        finish = time.time_ns()             # время окончания (в наносекундах)
        print(finish - start)               # время выполнения функции
        return res
    return wrapper


def cacher(func):
    cache = {}                  # сохраняем занчения в словарь (cach)


    def wrapper(*args):
        key = args
        if key not in cache:              # если ключа (который пришел) нет словаре (cach)
            cache[key] = func(*args)       # тогда выполняется функция
        return cache[key]               # если ключа (который пришел) уже есть в словаре, то берем его из словаря

    return wrapper


@log_func(1)            # навесили декораторы
@timer                      
@cacher
def seq(n):
    spisok = []
    for i in range(1, n + 1):
        result = (1 + i) ** i
        spisok.append(result)
    return spisok


print(seq(3))
print(seq(8))
print(seq(10))
print(seq(8))
print(seq(3))
print(seq(10))




