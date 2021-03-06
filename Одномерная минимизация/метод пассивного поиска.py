def f(x):
    """Исследуемая функция"""
    return x + 1 / x ** 2

# _____дано условию
a = 1
b = 2
e = 0.02
# __________________


def MPF():
    """Реализация метода пассивного поиска"""

    k = int((b - a) / e)
    print('Делим интервал на', k, "отрезков")

    # Ставим в соответствие каждому х значение функции
    dic = {}
    for i in range(k + 1):
        x_i = a + e * i
        print("Значение функции в точке", x_i, "равно", f(x_i))
        dic[x_i] = f(x_i)

    # Находим минимальное значение среди значений
    keys = dic.values()
    min_fx = min(keys)

    # Находим чему равен соответствующий х
    dic = {value: key for key, value in dic.items()}  # Меняем ключи и значения местами

    print('')

    print("_______________________ОТВЕТ_____________________")
    print('Наименьшее значение равное',  min_fx, "функция принимает в точке", dic[min_fx])


MPF()
