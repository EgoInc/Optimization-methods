import sympy
import numpy as np

f = lambda x1,x2,x3: x1**4+x2**2+x3**2+x1*x2+x2*x3
x0 = [0,1,0]
a, b, eps = 0.0001, 0.9999,  0.02

def f(x):
    return x[0]**4+x[1]**2+x[2]**2+x[0]*x[1]+x[1]*x[2]


def passive_search(x, v, a = a, b = b, eps = eps):
    n = round((b-a)/eps)+1
    x_s = [a+i*eps for i in range(n)]
    y_s = [f(x-i*v) for i in x_s]
    res = y_s.index(min(y_s))
    print(x_s[res])
    return x_s[res]

def coord_descent(x = np.array([0,1, 0]), num_var = 3, alpha = 0.001, eps = 0.02):
    x_prev = x + np.array([-1,-1, -1]) #делаем норму разности больше eps, чтобы выполнялось условие цикла
    n = 0
    check = 0
    while (np.linalg.norm(x-x_prev) > eps) or (check < 3):
        for i in range(num_var):
            x_prev = x
            d = np.zeros(num_var)
            d[i] = 1
            alp = passive_search(x, d)
            x = x - alp*d
            n+=1
            if (np.linalg.norm(x-x_prev) <= eps): check +=1 #проверили критерий остановки
    print("Метод покоординатного спуска выполнил {} шагов".format(n))
    print("Точка с координатами х1 = {}, x2 = {}, x3={}".format(x[0], x[1],x[2]))
    return x

coord_descent()