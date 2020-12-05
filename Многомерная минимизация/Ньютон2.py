import numpy as np
import sympy


# def f(x):
#     return 9 * x[0] ** 2 + x[1] ** 2
#
# def df(x):
#     return np.array([[18*x[0]], [2*x[1]]])
#
# def d2f(x):
#     return np.array([[18, 0],[0, 2]])
def f(x):
    return x[0] ** 4 + x[1] ** 2 + x[2] ** 2 + x[0] * x[1] + x[1] * x[2]


def df(x):
    return np.array([[4 * x[0] + x[1]], [2 * x[1] + x[0] + x[2]], [2 * x[2] + x[1]]])


def d2f(x):
    return np.array([[4, 1, 0], [1, 2, 1], [0, 1, 2]])


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


def newton2(x0=[0, 1, 0]):
    alpha = sympy.symbols('alpha')
    df_x0 = df(x0)
    # print(df_x0)
    d2f_x0 = d2f(x0)
    # print(d2f_x0)
    d2f_inverse = np.linalg.inv(d2f_x0)
    # print(d2f_inverse)
    # print(d2f_inverse.dot(df_x0))
    x1 = [[0], [1], [0]]  - alpha * d2f_inverse.dot(df_x0)
    # print(x1)
    alpha = MPF(f([x1[0][0], x1[1][0],x1[2][0]]))
    print('alpha=', alpha)
    x1 = [[0], [1], [0]] - alpha * d2f_inverse.dot(df_x0)
    # print(x1)
    # print(np.linalg.norm(x1))
    if np.linalg.norm(x1) < 0.05:
        print(np.round(x1,5))
        # print('end')


newton2()
