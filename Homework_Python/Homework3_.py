# 1. **Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# **Пример:[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def new_random_list_create():
    my_list = []
    for i in range(0, 5):
        import random
        after_comma = random.randint(0, 99)
        if after_comma <10:
            after_comma = (str(after_comma)).rjust(2, '0')
        else:
            after_comma = (str(after_comma))
        my_list.append(float(str(random.randint(0, 99))+'.'+ after_comma))
    print(my_list)
    return my_list
# def find_sum_in_list(any_list):
#     sum=0
#     for i in range(1, len(any_list), 2):
#         sum += any_list[i]
#     return sum
# random_list = new_random_list_create()
# print(find_sum_in_list(random_list))
# print(find_sum_in_list([2, 3, 5, 9, 3]))

# 2. **Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# **Пример:[2, 3, 4, 5, 6] => [12, 15, 16];[2, 3, 5, 6] => [12, 15]

# def find_mult_in_list(any_list):
#     new_list = []
#     for i in range(0, (len(any_list)+1)//2):
#         sum = any_list[i] * any_list[len(any_list)-1-i]
#         new_list.append(sum)
#     return new_list
# print(find_mult_in_list([2, 3, 4, 5, 6]))
# print(find_mult_in_list([2, 3, 5, 6]))

# 3. **Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# **Пример:[1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def find_def_min_max(list_of_floats):
#     min_in_list = max_in_list = round(list_of_floats[0] - int(list_of_floats[0]), 2)
#     for i in range(len(list_of_floats)):
#         after_comma = round(list_of_floats[i] - int(list_of_floats[i]), 2)
#         if after_comma != 0.0:
#             if min_in_list > after_comma:
#                 min_in_list = after_comma
#             if max_in_list < after_comma:
#                 max_in_list = after_comma
#     print(f'max {max_in_list} - min {min_in_list}')
#     return round(max_in_list-min_in_list, 2)
# print(f' => {find_def_min_max(new_random_list_create())}')
# print(find_def_min_max([1.1, 1.2, 3.1, 5, 10.01]))

# 4. **Напишите программу, которая будет преобразовывать десятичное число в двоичное.**
# Пример:45 -> 101101
# # 3 -> 11
# # 2 -> 10
# number = int(input('Please, enter a number: '))
# print(f'{number} -> {bin(number)}')

# def decimal_in_bin(num):
#     srting_bin =''
#     for i in range(0, 100):
#         pos = num % 2
#         num = num//2
#         srting_bin = str(pos) + srting_bin
#         if num == 0:
#             break
#     return str(number) + ' -> ' + '0b' + srting_bin
# print(decimal_in_bin(number))
# print(decimal_in_bin(45))
# print(decimal_in_bin(3))
# print(decimal_in_bin(2))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
number = int(input('Please, enter a number: '))
def Fib(num):
    num_list = []
    for i in range(0, num+1):
        if i == 0 or i == 1:
            num_list.append(i)
        else:
            num_list.append(int(num_list[i-1]+num_list[i-2]))
    nega_num_list = []
    for i in range(-num, num+1):
        if i<0:
            nega_num_list.append(int(((-1)**(i+1)) * num_list[-i]))
        if i >= 0:
            nega_num_list.append(num_list[i])
    return nega_num_list

print(Fib(number))

