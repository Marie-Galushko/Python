# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input())
pow_of_two = 1

while pow_of_two <= n:
    print(pow_of_two)
    pow_of_two = pow_of_two * 2
