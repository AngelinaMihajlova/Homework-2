# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

from random import randint

n = int(input('Введите размер списка: '))
numbers = [randint(-10, 10) for i in range(n)]
print(numbers)

a = int(input('Введите позицию первого элемента: '))
b = int(input('Введите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[a]*numbers[b]
print(f'Произведение элементов: {numbers[a]} * {numbers[b]} =', mult)




