# _____дано условию
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


def tangent():
    global a, b, e

    f_a = f(a)
    f_b = f(b)
    d1_a = df(a)
    d1_b = df(b)

    while (b - a) > e:

        # найдем точку пересечения касательных, пользуясь формулой касательной к функции в точке y=f(a)+f'(a)(x-a)
        c = ((f_b - d1_b * b) - (f_a - d1_a * a)) / (d1_a - d1_b)

        d1_c = df(c)

        if d1_c > 0:
            b = c
            xmin = c
            d1_b = d1_c
            f_b = fmin = f(b)

        else:
            a = c
            xmin = c
            d1_a = d1_c
            f_a = fmin = f(a)

    print("Минимальное значение функция принимает в точке x = ", xmin)
    print("Значение функции в этой точке: f(x) = ", fmin)

tangent()