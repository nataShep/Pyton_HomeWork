'''Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
n = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15'''

num, step = int(input("Введите первый элемент арифметической прогрессии = ")), int(input("Введите шаг арифметической прогрессии = "))
for i in range(int(input("Введите количество элементов = "))):
    print(num + i*step, end=' ')

