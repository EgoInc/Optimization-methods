def f(x):
    """Исследуемая функция"""
    return x + 1 / x ** 2

# _____дано условию
a = 1
b = 2
e = 0.02
delta=0.015
# __________________


def dichotomy():
    global b, a
    """Реализация метода Дихотомии"""

    while True:
        x = (a + b) / 2.0
        c = x - delta
        d = x + delta

        print("Проверяем критерий остановки", ((b - a) / 2))
        if ((b - a) / 2) < e:
            x_min = x
            fx_min = f(x_min)
            print('')
            print("_______________________ОТВЕТ_____________________")
            print('Наименьшее значение равное', fx_min, "функция принимает в точке", x_min)
            break

        if f(c) > f(d):
            a = c
            print("Новые границы", a, b)
        elif f(c) <= f(d):
            b = d
            print("Новые границы", a, b)





dichotomy()
