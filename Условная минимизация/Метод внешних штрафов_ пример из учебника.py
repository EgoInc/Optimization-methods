import numpy as np
import sympy
import math
import numpy as np

def df(x):
    return np.array([2 * x[0], 2 * x[1]])

def max1(g, x):
    return (g(x) + abs(g(x))) / 2
def H(g,x):
    return max1(g,x)

def MPF(fun):
    eps = 0.0001
    a = -5
    b = 5
    """Реализация метода пассивного поиска"""
    alpha = sympy.symbols('alpha')
    func = sympy.lambdify(alpha, fun, 'numpy')
    k = int((b - a) / eps)
    # Ставим в соответствие каждому х значение функции
    dic = {}
    for i in range(k + 1):
        x_i = a + eps * i
        dic[x_i] = func(x_i)
    # Находим минимальное значение среди значений
    keys = dic.values()
    min_fx = min(keys)
    # Находим чему равен соответствующий х
    dic = {value: key for key, value in dic.items()}  # Меняем ключи и значения местами
    print('Пассивный поиск возвращает', round(dic[min_fx], 6))
    return round(dic[min_fx], 6)


def golden_serch(fun, a=-10, b=10, delta=0.0001):
    alpha = sympy.symbols('alpha')
    f = sympy.lambdify(alpha, fun, 'numpy')
    a0 = a
    b0 = b
    k1 = (3 - math.sqrt(5)) / 2
    k2 = (math.sqrt(5) - 1) / 2
    # единственная итерация, на которой высчитываются значения функции в двух точках
    c = k1 * (b - a) + a
    d = k2 * (b - a) + a
    f_c = f(c)
    f_d = f(d)
    while delta < (b - a) / 2:
        if f(c) <= f(d):
            b = d
            d = c
            c = k1 * (b - a) + a
            xmin = c
            fmin = f_c
            f_d = f_c
            # единственное вычисление функции на данной итерации
            f_c = f(c)
        else:
            a = c
            c = d
            d = k2 * (b - a) + a
            xmin = d
            fmin = f_d
            f_c = f_d
            # единственное вычисление функции на данной итерации
            f_d = f(d)
    xmin = (a + b) / 2
    print('Золотое сечение возвращает', round(xmin,6))
    return xmin


def external_penalty_method(x0=np.array([1, 1]), r0=1, e=0.01):
    def coord_descent(x0, r0):
        alpha = sympy.symbols('alpha')
        x10 = x0
        while True:
            x11 = x10 - alpha * d_phi(x10, r0)
            a = MPF(phi(x11, r0))
            x11 = x10 - a * d_phi(x10, r0)
            if np.linalg.norm(d_phi(x11, r0)) <= 0.001:
                return (x11)
            else:
                x10 = x11

    x1 = sympy.symbols('x1')
    x2 = sympy.symbols('x2')
    alpha = sympy.symbols('alpha')
    f = lambda x: x[0] ** 2 + x[1] ** 2
    g = lambda x: 2 * x[0] + x[1] + 4
    phi = lambda x0, r0: f(x0) + r0 * H(g,x0) ** 2
    d_phi = lambda x0, r0: df(x0) + 2 * r0 * H(g,x0) * np.array([2, 1])
    i=1

    while True:
        x_new = coord_descent(x0, r0)
        # if i == 1:
        #     x_new = np.array([-1.3333, -0.6666])
        # elif i==2:
        #     x_new = np.array([-1.568629, -0.784310])
        # elif i==3:
        #     print('Error')
        #     break

        if H(g,x_new)**2>0.01:
            x0 = x_new
            r0 = 10 * r0

        else:
            print('Точка минимума', x_new)
            break



external_penalty_method()
