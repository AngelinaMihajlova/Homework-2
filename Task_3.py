# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки. 
# Пример: Для n = 6 -> 14.072

n = int(input('Введите число: ')) 

def set_sequence(n):
    return [round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]

nums = set_sequence(n)
print(nums)
print(round(sum(nums), 3))
