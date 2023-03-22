# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

def FillRandomArray(number, left, right):
    number_array = list()
    for _ in range(number):
        number_array.append(random.randint(left, right))
    return number_array

def FindNumberInArray(array, find_number):
    array.sort()
    if find_number <= array[0]:
        return array[0]
    elif find_number >= array[-1]:
        return array[-1]
    for i in range(1, len(array)):
        if array[i] == find_number:
            return array[i]
        elif array[i] < find_number:
            continue
        
        if abs(array[i - 1] - find_number) < abs(array[i] - find_number):
            return array[i - 1]
        elif abs(array[i - 1] - find_number) == abs(array[i] - find_number):
            return array[i - 1], array[i]
        else:
            return array[i]

array = FillRandomArray(int(input("Введите длину массива: ")), 0, 10)
print(array)
result = FindNumberInArray(array, int(input("Введите искомое число: ")))
print(f"Ближайшее число массива к искомому будет число {result}")
