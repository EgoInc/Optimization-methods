import sympy
import numpy as np
count = 0

# def f(x):
#     return 9*x[0]**2+x[1]**2
# def df(x):
#     return [18*x[0], 2*x[1]]
def f(x):
    return x[0] ** 4 + x[1] ** 2 + x[2] ** 2 + x[0] * x[1] + x[1] * x[2]


def df(x):
    return [4 * x[0] ** 3 + x[1], 2 * x[1] + x[0] + x[2], 2 * x[2] + x[1]]


def MPF(fun):
    eps = 0.001
    a = -10
    b = 10
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
    return round(dic[min_fx], 3)


def MGD(x0):
    alpha = sympy.symbols('alpha')
    df_x0 = np.array(df(x0))
    x = x0 - alpha * df_x0
    fun = f(x)
    a = MPF(fun)
    new_x = x0 - a * df_x0
    # new_x[0] = round(new_x[0], 4)
    # return np.round(new_x,3)
    return new_x


def gully_minimization(x0=np.array([0, 1, 0])):
    global count
    count +=1
    print('_________ШАГ {}_______________'.format(count))
    alpha = alpha = sympy.symbols('alpha')
    about_x0 = x0 + 0.1
    y0 = MGD(x0)
    about_y0 = MGD(about_x0)
    print('x0=', x0, '     x0* = ', about_x0)
    print('y0=', y0, '     y0* = ', about_y0)
    y_difference = np.round(about_y0 - y0, 3)

    a = MPF(f(y0 + alpha * y_difference))
    new_x = y0 + a * y_difference
    print('Новый x', new_x)
    if (np.linalg.norm(df(new_x)) > 0.05) and a != 0:
        gully_minimization(np.array(new_x))
    else:
        print('__________Ответ__________')
        print(new_x)
        # print(np.round(new_x, 3))
        return (new_x)


gully_minimization()
