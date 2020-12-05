import numpy as np
import sympy


# def f(x):
#     return 9*x[0]**2+x[1]**2
# def df(x):
#     return [18*x[0], 2*x[1]]
# a, b, eps = 0.0001, 0.9999,  0.0005

def f(x):
    return x[0]**4+x[1]**2+x[2]**2+x[0]*x[1]+x[1]*x[2]
def df(x):
    return [4*x[0]**3+x[1], 2*x[1]+x[0]+x[2], 2*x[2]+x[1]]
a, b, eps = 0.0001, 0.9999,  0.02
count=0

def MPF(fun):
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
    return dic[min_fx]

def MGD(x0):
    global count
    count +=1
    print('________________КРУГ НОМЕР', count, "_____________________")
    alpha = sympy.symbols('alpha')
    df_x0 = np.array(df(x0))
    print('Значение производной в точке', df_x0)
    x = x0-alpha*df_x0
    # print("Начинаем минимизировать f(alpha) от параметром:", x)
    fun = f(x)
    # print('Our func', fun)
    a = MPF(fun)
    print('Найденное alpha = ', a, 'проверяем критерий остановки')
    new_x = x0 - a*df_x0
    # new_x[0] = round(new_x[0], 4)
    print('Новый х', new_x)
    print('df(new_x)', df(new_x))
    print(np.linalg.norm(df(new_x)))
    if (np.linalg.norm(df(new_x))>eps) and a!=0:
        MGD(np.array(new_x))
    else:
        print('Ответ')
        print(x0[0], x0[1],x0[2])
        # print()
MGD(np.array([0,1,0]))