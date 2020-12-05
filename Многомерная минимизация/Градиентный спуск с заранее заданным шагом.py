import numpy as np

count = 1


def f(x):
    return x[0] ** 4 + x[1] ** 2 + x[2] ** 2 + x[0] * x[1] + x[1] * x[2]


def df(x):
    return [4 * x[0] ** 3 + x[1], 2 * x[1] + x[0] + x[2], 2 * x[2] + x[1]]


e = 0.001


# _______________________________________________________-


def grad_preset_step(x0=np.array([0, 1, 0])):
    global count
    while True:
        count += 1
        # print(count)
        df_x0 = np.array(df(x0))
        koef = (1 / count)
        x0 = x0 - koef * df_x0
        if (np.linalg.norm(np.array(df(x0)))) < e:
            break
    print('Количество итераций')
    print("Искомая точка", x0)


grad_preset_step()
