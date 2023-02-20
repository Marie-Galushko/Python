# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и 
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Первый элемент: '))
d = int(input('Разность: '))
n = int(input('Количество элементов: '))

print(*[a1 + (i - 1) * d for i in range(1, n + 1)])