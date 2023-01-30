# Задание на списки
# Создать список, на четных местах в котором стоят единицы, а на нечетных местах - числа,
# равные остатку от деления своего номера на 5.
# list_1 = []
# for i in range(10):
#     if i %2 == 0: list_1.append(i % 5)
#     else: list_1.append(1)
# print(list_1)

# Создать список, который одинаково читается как слева направоБ так и справа налево

# import random
# # n = random.randint(1, 10)
# n = 9
# l_n = []
# for i in range(n):
#     l_n.append(random.randint(5, 10))
# print(l_n)
# for i in range(n//2):
#     l_n[n-i-1] = l_n[i]
#     print(i, '->', l_n[n-i-1])
# print(n, '->', l_n)

# заполните список случайным образом нулями и единицами так, чтобы кол-во единиц было больше кол-ва нулей
# import random
# # n = random.randint(1, 10)
# n = 9
# l_n = []
# for i in range(n):
#     l_n.append(random.randint(0, 1))
# print(l_n, sum(l_n))
# count_0= 0
# count_1 = 0
# for i in range(n):
#     if l_n[i] == 0: count_0 += 1
#     else: count_1 += 1
# print('0 - >', count_0, '1 - >', count_1)
# if count_0 > count_1:
#     for i in range(n):
#         if l_n[i] == 0: l_n[i] =1
#         if count_0>count_1: break
# print(l_n)

# найти кол-во чисел в строке, которые делятся на 3, но не делятся на 7

# Дан массивб Найдите три последовательных элемента в массиве, сумма которых мах
# our_list = [2, 5, 11, 0, 5, 10, 1, 3, 2, 4, 6, 7, 8]
# sum_3 = 0
# max = 0
# for i in range(len(our_list)-2):
#     sum = our_list[i] + our_list[i+1] + our_list[i+2]
#     if sum > max: max = sum
# print(max)



# Проверьте, содржт ли данный массив из n чисел все числа от 1 до n.
# import random
# n = random.randint(6, 10)
# list_n = [random.randint(0, 10) for i in range(n)]
# list_x = [i for i in range(11)]
# print(n, list_n, list_x)
# there_are = False
# for i in range(11):
#     for j in range(n):
#         if list_x[i] == list_n[j]: there_are = True
#     print(f'Число {list_x[i]} в списке? {there_are}')
#     there_are = False

#
# Напишите программу, которая вводит с клавиатуры непустой список целых чисел, и выводит число локальных максимумов
# (элемент является локальным максимумом, если он не имеет соседей, больших, чем он сам).

# import random
# # n = random.randint(6, 10)
# list_n = [random.randint(0, 10) for i in range(15)]
# loc_max = []
# for i in range(1, len(list_n)-1):
#     if list_n[i]> list_n[i-1] and list_n[i] > list_n[i+1]:
#         loc_max.append(list_n[i])
# print(list_n)
# print(loc_max)

# Даны два списка. Определите, существуют ли в первом списке такие два элемента, что их сумма равна сумме
# # каких-либо трех элементов второго списка.
# import random
# # n = random.randint(6, 10)
# list_1 = [random.randint(0, 10) for i in range(5)]
# list_pare_1 =[]
# list_2 = [random.randint(0, 10) for i in range(5)]
# list_three_2 =[]
# dict_1 = {}
# dict_2 ={}
# for i in range(len(list_1)):
#     for j in range(i+1, len(list_1)):
#         list_pare_1. append(list_1[i] + list_1[j])
#         dict_1[f'{i} + {j}'] = list_1[i] + list_1[j]
# print(f'{list_1}\n{list_pare_1}')
# print(dict_1)
# for i in range(len(list_2)):
#     for j in range(i+1, len(list_2)):
#         for k in range(j+1, len(list_2)):
#             list_three_2. append(list_2[i] + list_2[j] + list_2[k])
#             dict_2[f'{i} + {j} +{k}'] = list_2[i] + list_2[j] + list_2[k]
# print(f'{list_2}\n{list_three_2}')
# print(dict_2)
# for kyes_1 in dict_1.keys():
#     for kyes_2 in dict_2.keys():
#         if dict_1[kyes_1] == dict_2[kyes_2]:
#             print(f'Значения первого листа:{kyes_1} : {dict_1[kyes_1]}, значения второго листа {kyes_2} : {dict_2[kyes_2]}')

# Задание на списки
# Дана упорядоченная последовательность an чисел от 1 до N. Из копии данной 
# последовательности bn удалили одно число, а оставшиеся перемешали. 
# Найти удаленное число.
# start_list = [11,0,9,1,2,4,8,12,3,5,8,6,10]
# def find_max(list_1:list):
#     max_0 = 0
#     for i in range(len(list_1)):
#         if list_1[i] > max_0: max_0 = list_1[i]
#     return max_0
# def find_min(list_1:list):
#     min_0 = 0
#     for i in range(len(list_1)):
#         if list_1[i] < min_0: min_0 = list_1[i]
#     return min_0
# max_max = find_max(start_list)

# min_min = find_min(start_list)
# print(max_max, '->', min_min)
# new_list = [i for i in range(min_min, max_max+1)]
# print(new_list)
# for i in range(min_min, max_max+1):
#     for j in range(len(start_list)): 
#         if i == start_list[j]: 
#             print('i=',i, 'j=', j, '=?', start_list[j])
#             new_list[i] = 'found'
# print(new_list)

# Дан список, в котором количество отрицательных элементов равно количеству
# положительным. Поменяйте местами первый отрицательный и первый положительный, 
# второй отрицательный и второй положительный и так далее.