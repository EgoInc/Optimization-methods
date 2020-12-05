import math as m



def golden_section(f, a=0.001, b=5, delta=0.001):

    a0 = a
    b0 = b

    k1 = (3 - m.sqrt(5)) / 2
    k2 = (m.sqrt(5) - 1) / 2

    # единственная итерация, на которой высчитываются значения функции в двух точках
    c = k1 * (b - a) + a
    d = k2 * (b - a) + a
    f_c = f(c)
    f_d = f(d)

    while delta < (b - a) / 2:

        if f(c) <= f(d):
            b = d
            d = c
            c = k1 * (b - a) + a

            xmin = c
            fmin = f_c
            f_d = f_c

            # единственное вычисление функции на данной итерации
            f_c = f(c)
        else:
            a = c
            c = d
            d = k2 * (b - a) + a

            xmin = d
            fmin = f_d
            f_c = f_d

            # единственное вычисление функции на данной итерации
            f_d = f(d)


    xmin = (a + b) / 2
    fmin = f(xmin)

    print("Минимальное значение функция принимает в точке x = ", round(xmin, 4))
    print("Значение функции в этой точке: f(x) = ", round(f(xmin), 4))



f = lambda x: x + 1 / x ** 2
golden_section(f)