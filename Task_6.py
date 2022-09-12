# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример: Для "abababb" и "aba" -> 2

string = input('Введите первую строку: ')
substring = input('Введите вторую строку: ')

def counting_occurrences(a, b):
    count = 0
    i = -1
    while True:
        i = a.find(b, i+1)
        if i == -1:
            return count
        count += 1
print(counting_occurrences(string, substring))