# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

def FillRandomArray(number, left, right):
    number_array = list()
    for _ in range(number):
        number_array.append(random.randint(left, right))
    return number_array

def CountNumberInArray(array, find_number):
    count = 0
    for _ in array:
        if _ == find_number:
            count += 1
        else:
            continue
    return count

number = int(input("Введите длину массива: "))
array = FillRandomArray(number, 0, 10)
print(array)
find_number = int(input("Введите искомое число: "))
print(f"Искомое число в массиве встречается: {CountNumberInArray(array, find_number)} раз(-а)")