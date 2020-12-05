import numpy as np
import sympy


def f(x):
    return x[0]**4+x[1]**2+x[2]**2+x[0]*x[1]+x[1]*x[2]
def df(x):
    return [4*x[0]**3+x[1], 2*x[1]+x[0]+x[2], 2*x[2]+x[1]]
e= 0.0001
def MPF(fun):
    eps = 0.001
    a=0.0001
    b=5
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



def fast_grad_k(x0=np.array([0,1,0])):
    y0 = np.array( [-0.4445696, 0.31691606, -0.16865596])
    y0_x0 = y0-x0
    print('y0_x0', y0_x0)
    alpha = sympy.symbols('alpha')
    print('Our func',f(x0 + alpha * y0_x0))
    a = MPF(f(x0 + alpha * y0_x0))
    print('Найденное альфа', a)
    new_x=x0+a*y0_x0
    print('new_x', new_x)
    if (np.linalg.norm(df(new_x))>e) and a!=0:
        fast_grad_k(np.array(new_x))
    else:
        print('Ответ')
        print(np.round(new_x,4))
fast_grad_k()