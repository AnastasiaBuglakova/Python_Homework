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

# Проверьте, содржт ли данный массив из n чисел все числа от 1 до n.