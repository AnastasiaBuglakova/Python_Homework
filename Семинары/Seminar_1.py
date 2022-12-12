# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# number1 = int(input('Enter first number: '))
# number2 = int(input('Enter second number: '))
# if number1 == number2**2 or number2 ==number1**2:
#     print('да')
# else:
#     print('неа')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

number1 = int(input('Enter #1 number: '))
number2 = int(input('Enter #2 number: '))
number3 = int(input('Enter #3 number: '))
number4 = int(input('Enter #4 number: '))
number5 = int(input('Enter #5 number: '))
max = number1

list = [number1, number2, number3, number4, number5]
for i in list:
    if list[i] > max: max = list[i]
print(max)
# if number2  > max: max = number2
# if number3  > max: max = number3
# if number4  > max: max = number4
# if number5  > max: max = number5
# print(max)