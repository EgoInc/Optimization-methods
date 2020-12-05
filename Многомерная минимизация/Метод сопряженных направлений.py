import sympy
import numpy as np

k = 0


def f(x):
    return x[0] ** 4 + x[1] ** 2 + x[2] ** 2 + x[0] * x[1] + x[1] * x[2]


def df(x):
    return np.array([4 * x[0] ** 3 + x[1], 2 * x[1] + x[0] + x[2], 2 * x[2] + x[1]])


def MPF(fun):
    eps = 0.001
    a = 0.0001
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
    return round(dic[min_fx], 3)


def Fletcher_Rivz(x0=np.array([0, 1, 0]), d0=np.array([-1, -2, -1])):
    global k
    print(x0, d0)
    k += 1
    alpha = sympy.symbols('alpha')
    a = MPF(f(x0 + alpha * d0))
    print('Найденное альфа', a)
    if k % 10 == 0:
        x1 = x0+a*d0
        print(x1)
        d1 = -1*df(x1)
    else:
        x1 = x0+a*d0
        print(x1)
        b = np.linalg.norm(df(x1))**2/np.linalg.norm(df(x0))**2
        print('b=', b)
        print(df(x1))
        print(b*d0)
        d1 = -1*df(x1)+b*d0

    if (np.linalg.norm(df(x1))>0.005) and a!=0:
        Fletcher_Rivz(x1,d1)
    else:
        print('Ответ')
        print(np.round(x1,4))

        


Fletcher_Rivz()
