# Задача из ДЗ 2/3. Задать список из n чисел последовательности (1 + 1/n)^n    
# и вывести на экран их сумму.
# Пример - Для n = 6:
# [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
# Сумма чисел = 14.0717


def num_sequence(n):
    # n = 6
    res_list = []   # - задаем новый список 
    sum_res = 0
    for i in range(1, n + 1) :      # - перебираем все элементы списка
        # - высчитываем формулу:
        res = round((1 + 1 / i) ** i, 2)     # round - функция округления; 2 - два знака после запятой
        sum_res += res
        # sum_res = sum_res * res
        res_list.append(res)        # append - функция добавляет в конец списка
    sum_res = round(sum_res, 2)
    # print(res_list)
    # print(sum_res)
    return sum_res
    
   

# print(num_sequence(5))    # сумма чисел последовательности из n = 5 элементов = 11.55
# print(num_sequence('2')) 
# x = num_sequence(5)
