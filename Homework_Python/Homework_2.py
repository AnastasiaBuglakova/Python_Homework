# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму 
# его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
num = input('Please, enter any number: ')
if ',' in num:
    num = num.replace(',', '.')
def sum_of_numbers(num):
    num_int= int(float(num))
    sum=0
    for i in range(1, 10):
        sum+=num_int%10
        num_int//=10
    if "." in num:
        integer, separate = num.split('.')
        separate = int(separate)
        for i in range(1, 10):
            sum+=separate%10
            separate//=10
    return sum
print(sum_of_numbers(num))


# 2 Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Please, enter any number: '))
# list_of_numbers = []
# sum=0
# for i in range(1, n+1):
#     num=round ((1 + 1/i)**i, 2)
#     list_of_numbers.append(num)
#     sum +=num
# print(f'Для n = {n} -> {list_of_numbers}\n Сумма {sum}')



# 3 Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

my_list = []
for i in range(0, 10):
    import random
    my_list.append(str(random.randint(0,99))+'.'+str(random.randint(0,99)))
print(my_list)
for j in range (0, len(my_list)*5):
    for i in range(0, len(my_list)-1):
        shake = my_list[i]
        k = random.randint(0, len(my_list)-1)
        my_list[i] = my_list[k]
        my_list[k]=shake
print(my_list)