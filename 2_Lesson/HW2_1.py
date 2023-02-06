# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# Пример:

# 5 -> 1 0 1 1 0
# 2

n = int(input())
count_1 = 0
count_2 = 0
for i in range(n):
    coin = int(input())
    if coin == 1:
        count_1 += 1
    else:
        count_2 += 1
if count_1 > count_2:
    print(count_2)
else:
    print(count_1)