# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# 5
# 15
# [1, 9, 13, 14, 19]

# Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

a = list(map(int, input('Введите массив: ').split()))

mini = int(input('Min: '))
maxi = int(input('Max: '))
print(*[i for i in range(len(a)) if mini <= a[i] <= maxi])
