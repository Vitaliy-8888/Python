# Задача 11_1. 
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# 1. Определить корни

# 2. Найти интервалы, на которых функция возрастает

# 3. Найти интервалы, на которых функция убывает

# 4. Построить график

# 5. Вычислить вершину

# 6. Определить промежутки, на котором f > 0

# 7. Определить промежутки, на котором f < 0


from sympy import symbols, sin, cos       # из sympy взяли sin и cos
from sympy.plotting import plot
from scipy.optimize import fsolve         # рисует графики, так же как и matplotlib  
import matplotlib.pyplot as plt         # вместо pyplot использием псевдоним plt 
import numpy                            # создает список с тем количеством, которое мы укажем


# 4.1. График функции при помощи библиотеки matplotlib:
x = [x for x in range(-30, 30)]     # для функции через list comprehension создали список Иксов, (количество значений, которые мы передаем)
y = [(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for       # список Игреков создали на основании наших Иксов
     x in range(-30, 30)]           # взяли диапазон -30, 30
# y = [y for y in range(-30, 30)]
plt.plot(x, y)      # передали списки х и y в matplotlib  
plt.grid()          # добавляет сетку значений на график
plt.show()          # добавляет график из библиотеки matplotlib


# 4.2. График функции при помощи библиотеки sympy:
# в диапазоне -300...300
x = symbols('x')            # х будет равняться symbols('x') в формуле: 
plot(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30,    # передаем нашу функцию
     (x, -300, 300))            # передаем диапазон для х от -300 до 300

# 4.3. в диапазоне -10...10
x = symbols('x')
plot(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30,
     (x, -10, 10))          # взяли другой диапазон


# 1. Определить корни   
# (Определить корни – то есть, там где х = 0)
def f(x):       # с помощью scipy создаем функцию 
    # математическую функцию поместили в Питоновскую функцию и будем использовать в дальнейших расчетах
    return -12 * x ** 4 * numpy.sin(        
        numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


# Это тригонометрическая функция, имеющая бесконечное количество корней.
# Можно определить корни только на заданном интервале.
# Запросим их у пользователя:
# funcrange = list(
#     map(int, input('Задайте интервал функции через пробел: ').split()))
funcrange = [-10, 10]       # диапазон в котром будем находить наши значения
leftnum = min(funcrange)
rightnum = max(funcrange)


# Задайте интервал функции через пробел: -5 5


def solution():
    global leftnum, rightnum
    temp = leftnum
    rightnum = rightnum
    roots = []
    interval = []

    while temp < rightnum:
        if f(temp) >= 0 and f(temp + 1) <= 0:     # используем нашу функцию f и передаем в fsolve функцию f и значение temp 
            w = fsolve(f, temp)                 # fsolve относится к: from scipy.optimize import fsolve (см.вверху import)
            roots.append(*w)                # с помощью fsolve считаем корни в диапазоне [-10, 10] и добавляем их в список
        if f(temp) <= 0 and f(temp + 1) >= 0:
            w = fsolve(f, temp)
            roots.append(*w)
        if f(temp) > f(temp + 1) < f(temp + 2):
            interval.append(temp + 1)
        temp += 1
    roots = [round(i, 2) for i in roots]
    print(f'Корни уравнения для заданного интервала: {roots}')
    return roots


# 6 и 7. Определить промежутки, на которых f>0 и f<0:
def func_interval(left, right):
    array = []
    temp = left
    while left < right:
        array.append([f(left), left])
        left += 0.1
    if array[0][0] > 0:
        print(f'f > 0 в промежутке {temp, right}')
        return max(array)
    else:
        print(f'f < 0 в промежутке {temp, right}')
        return min(array)


# 5. Вычисляем координаты вершины функции на заданном интервале (т.е. находим min и max на интевале)
# 2 и 3. Найти интервалы, на которых функция возрастает и убывает
def maxima_and_minima():
    roots = solution()

    if len(roots) < 2:
        print('На заданном интервале нет вершин')
    else:
        top = []
        for i in range(len(roots) - 1):
            top.append(func_interval(roots[i], roots[i + 1]))
        for j in top:
            j = [round(i, 2) for i in j]
            print(f'Координаты вершин функции: [{j[1]}, {j[0]}]')
        if len(top) < 2:
            print('error')
        else:
            for i in range(len(top) - 1):           
                if top[i][0] > top[i + 1][0]:       #  определяем где функция возрастает и убывает:
                    print('Функция убывает')
                else:
                    print('Функция возрастает')


maxima_and_minima()
