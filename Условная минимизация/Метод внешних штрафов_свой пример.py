import numpy as np
import sympy


def max1(func, x):
    return (func(x) + abs(func(x)))/2

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
    # print('Пассивный поиск возвращает', round(dic[min_fx], 6))
    return round(dic[min_fx], 6)





def external_penalty_method():
    def coord_descent(x0, r0=1):
        alpha = sympy.symbols('alpha')
        x10 = x0
        while True:
            x11 = x10 - alpha * d_phi(x10, r0)

            a = MPF(phi(x11, r0))
            # print('a',a)
            x11 = x10 - a * d_phi(x10, r0)
            if np.linalg.norm(d_phi(x11, r0)) <= 0.001 or a==0:
                return (x11)
            else:
                x10 = x11
                # print('new x in coord.des.=', x10)

    #_____Задаем необходимые функции________
    f = lambda x: x[1] ** 2 + 2 * x[0] * x[2] - x[2]
    df = lambda x: np.array([2 * x[0], 2 * x[1], 2 * x[0] - 1])
    g = lambda x: -x
    h1 = lambda x: x[0] + x[1] - 4
    h2 = lambda x: x[1] + x[2] - 8
    H = lambda x: max1(g, x[0]) ** 2 + max1(g, x[1]) ** 2 + max1(g, x[2]) ** 2 + h1(x) ** 2 + h2(x) ** 2
    d_H = lambda x: -2 * max1(g, x[0]) - 2 * max1(g, x[1]) - 2 * max1(g, x[1]) + 2 * h1(x) * np.array(
        [1, 1, 0]) + 2 * h2(x) * np.array([0, 1, 1])
    phi = lambda x, r: f(x) + r * H(x)
    d_phi = lambda x, r: df(x) + r * d_H(x)
    #_______________________________________


    x0 = [1,1,1]
    r0 = 1
    while True:
        print('ШАГ МЕТОДА ВНЕШНИХ ШТРАФОВ')
        x_new = coord_descent(x0, r0)
        print('new x', x_new)
        print(H(x_new)**2)
        if H(x_new) ** 2 > 0.01:
            x0 = x_new
            r0 = 10 * r0

        else:
            print('Точка минимума', x_new)
            print('Значение функции в точке минимума', f(x_new))
            break
external_penalty_method()