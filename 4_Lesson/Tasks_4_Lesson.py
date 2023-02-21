# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.

string = input().split()

for i in range(len(string)):
    count = 1
    for j in range(i + 1, len(string)):
        if string[i] == string[j]:
            string[j] += "_" + str(count)
            count += 1
    

print(string)


# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним
# или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.

She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
string = set(string.lower().split())
print(len(string))

# Вариант Дениса

print(len(set(input().lower().split())))

# set убирает повторы слов, len(set) считает число неповторяющихся слов,
# lower убирает значение регистра, split слова в строке 
# преобразует в элементы массива


# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности,
# которая завершается первым встретившимся
# нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде,
# тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

n = int(input())
max_number = 0
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)

n = int(input())
max_number = -1
while n > 0:    
    if max_number < n:
       max_number = n
    n = int(input())
print(max_number)