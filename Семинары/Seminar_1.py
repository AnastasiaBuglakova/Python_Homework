# Урок 1. Знакомство с Python
# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# number_of_weekday = int(input('Please, enter number of day in a week (number from 1 to 7): '))
# if number_of_weekday >0 and number_of_weekday < 6:
#     print('It is not weekend(.')
# elif number_of_weekday >5 and number_of_weekday < 8:
#     print('It is weekend!')
# else:
#     print('It is not number from 1 to 7')

# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = None
y = None
z = None

for i in range(0, 2):
    if i == 0: x = False
    else: x= True
    for j in  range(0, 2):
        if j == 0: y = False
        else: y= True
        for k in  range(0, 2):
            if k == 0: z = False
            else: z= True
            a = not(x or y or z)
            b = (not (x)) and (not (y)) and (not (z))
            if a == b:
                print('Доказано!')
            else:
                print('Не вышло!')

# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# x = int(input('Please, enter the X coordinate of the point to define the quarter: '))
# y = int(input('Please, enter the X coordinate of the point to define the quarter: '))
# if x > 0 and y > 0:
#     print('Your quarter is #1')
# if x < 0 and y > 0:
#     print('Your quarter is #2')
# if x < 0 and y < 0:
#     print('Your quarter is #3')
# if x > 0 and y < 0:
#     print('Your quarter is #4')

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).
# chetvert = input('Please, enter number of querter in format "1, 2, 3 or 4": ')
# if chetvert == '1':
#     print('range of coordinate values: x: (0, ∞), y:(0, ∞)')
# elif chetvert == '2':
#     print('range of coordinate values: x: (0, - ∞), y:(0, ∞)')
# elif chetvert == '3':
#     print('range of coordinate values: x: (0, - ∞), y:(0, - ∞)')
# elif chetvert == '4':
#     print('range of coordinate values: x: (0, ∞), y:(0, - ∞)')
# else:
#     print('Please, enter number of quarter in right format and range')

# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# # - A (7,-5); B (1,-1) -> 7,21
# x1 = float(input('Please, enter coordinats for first point, x: '))
# y1 = float(input('y: '))
# x2 = float(input('Please, enter coordinats for second point, x: '))
# y2 = float(input('y: '))
# distance = round(((x1-x2)**2 + (y1- y2)**2)**0.5, 2)
# print(f'Distanse between these poins is {distance}')