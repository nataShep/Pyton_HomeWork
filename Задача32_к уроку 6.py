'''Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]'''

from random import randint
list_1 = [randint(-100,101)]
for n in range(int(input("Задайте кол-воэлементов списка = "))):
    list_1.append(n)
print(list_1)
list_2 = []
max = int(input("Задайте максимум = "))
min = int(input("Задайте минимум = "))
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)
