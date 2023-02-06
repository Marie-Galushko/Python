# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

print(len(set(list_nums)))

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

list_nums = [1, 2, 3, 4, 5]
k = 7
print(list_nums)
result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
print(result)

# 2 Вариант
# list_nums = [1, 2, 3, 4, 5]
# k = 7

# print(list_nums)

# for i in range(k - 1):
#     list_nums.insert(0, list_nums.pop(- 1))

# print(k, list_nums)


# 3 задача

list_dict = [{"V": "S001"}, {"V": "S002"},
             {"VI": "S001"}, {"VI": "S005"},
             {"VII": " S005 "}, {"V": " S009 "},
             {"VIII": " S007 "}]



print(set(list(i.values())[0].strip() for i in list_dict))

# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)


list_nums = [0, -1, 5, 2, 3]

print(sum([1 for i in range(1, len(list_nums)) if list_nums[i] > list_nums[i - 1]]))
