import numpy as np

def f(x):
    return x[0]**4+x[1]**2+x[2]**2+x[0]*x[1]+x[1]*x[2]
def df(x):
    return [4*x[0]**3+x[1], 2*x[1]+x[0]+x[2], 2*x[2]+x[1]]
e = 0.01

def grad_const_step(x0=np.array([0,1,0])):
    count = 0
    alpha = 0.05
    while True:
        df_x0 = np.array(df(x0))
        x0 = x0 - alpha*df_x0
        if (np.linalg.norm(df_x0)) < e:
            break
    print('Количество итераций')
    print("Искомая точка", x0)
    return x0

grad_const_step()