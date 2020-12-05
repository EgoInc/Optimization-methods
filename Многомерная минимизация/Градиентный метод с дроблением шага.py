import numpy as np

def f(x):
    return x[0]**4+x[1]**2+x[2]**2+x[0]*x[1]+x[1]*x[2]
def df(x):
    return [4*x[0]**3+x[1], 2*x[1]+x[0]+x[2], 2*x[2]+x[1]]
e = 0.02

def grad_split_step(x0=np.array([0,1,0]), alpha = 0.5):
    count = 0
    lam = 0.1
    alpha = 0.5
    delta = 0.5
    df_x0 = np.array(df(x0))
    while True:
        count +=1
        x_new = x0 - alpha*df_x0
        if (f(x_new)-f(x0)) <= (-1*alpha*delta*(np.linalg.norm(df_x0))**2):
            x0 = x0 - alpha*df_x0
            df_x0 = np.array(df(x0))
            alpha = 0.5
        else:
            alpha = lam*alpha
        if (np.linalg.norm(df_x0)) < e:
            break
    print('Количество циклов', count)
    print('Искомая точка', x0)

    return x0

grad_split_step()

