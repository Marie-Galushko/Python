# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# 5
# 1 2 3 4 5 3
# -> 1

n = int(input("Введите количество элементов в массиве: "))
list = [int(input()) for i in range(n)]
number = int(input("Выберите число: "))
print(f"Сколько раз встречается число {number} в массиве: {list.count(number)}")