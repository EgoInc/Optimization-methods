# _____дано условию
import numpy

a = 1
b = 2
e = 0.02
delta=0.015
# __________________
def f(x):
    """Исследуемая функция"""
    return x + 1 / x ** 2

def df(x):
    """Производная функции 1ого порядка"""
    return 1 - 2/x**3

def d2f(x):
    """Производная функции 2ого порядка"""
    return 6/x**4

def secant():
    global a, b

    f_a = f(a)
    f_b = f(b)

    df_a = df(a)
    df_b = df(b)

    # Воспользуемся вместо второй производной ее приближением
    d2_f_b = (df_b - df_a) / (b - a)

    while abs(a - b) > e:

        a = b
        b -= df_b / d2_f_b

        f_a = f_b
        f_b = f(b)

        df_a = df_b
        df_b = df(b)

        d2_f_b = (df_b - df_a) / (b - a)

        if f_a > f_b:
            xmin = b
            fmin = f_b
        else:
            xmin = a
            fmin = f_a

    print("Минимальное значение функция принимает в точке x = ", xmin)
    print("Значение функции в этой точке: f(x) = ", fmin)

secant()