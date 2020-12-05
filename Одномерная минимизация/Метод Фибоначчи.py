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


def Fib(n):
    """Определим функцию, возвращающую массив чисел Фибоначчи"""

    Fib_n_1=1
    Fib_n_2 =1
    Fib_n=[Fib_n_1, Fib_n_2]

    while Fib_n_2 < n:
        v = Fib_n_2
        Fib_n_2 += Fib_n_1
        Fib_n_1 = v
        Fib_n.append(Fib_n_2)

    return Fib_n


def fibonacci():
    """Определим функцию, осуществляющую метод Фибоначчи по поиску точки минимума функции:"""
    global a, b


    # определяем, сколько чисел Фибоначчи нам необходимо
    n0 = (b - a) / e
    Fib_n = Fib(n0)

    n = len(Fib_n) - 1

    # на первой итерации определяем значения функции в двух точках
    c = a + (b - a) * (Fib_n[n - 2] / Fib_n[n])
    d = a + (b - a) * (Fib_n[n - 1] / Fib_n[n])

    f_c = f(c)
    f_d = f(d)

    # на всех последующих итерациях вычисляется лишь одно значение функции в новой точке
    for i in range(1, n - 2):

        if f_c <= f_d:
            fmin = f_c
            xmin = c
            b = d
            d = c
            c = a + (b - a) * (Fib_n[n - 1 - i] / Fib_n[n + 1 - i])

            f_d = f_c
            f_c = f(c)
        else:
            fmin = f_d
            xmin = d
            a = c
            c = d
            d = a + (b - a) * (Fib_n[n - i] / Fib_n[n + 1 - i])

            f_c = f_d
            f_d = f(d)


    print("Минимальное значение функция принимает в точке x = ", xmin)
    print("Значение функции в этой точке: f(x) = ", f(xmin))

fibonacci()