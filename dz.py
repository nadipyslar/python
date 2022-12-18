# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

# x_coordinate = int(input('Введите координату Х, неравную 0 '))
# y_coordinate = int(input('Введите координату Y, неравную 0 '))
# if x_coordinate>0 and y_coordinate>0:
#     print('Это первая четверть')
# elif x_coordinate<0 and y_coordinate>0:
#     print('Это вторая четверть')
# elif x_coordinate>0 and y_coordinate<0:
#     print('Это четвертая четверть')
# elif x_coordinate<0 and y_coordinate<0:
#     print('Это третья четверть')
# else:
#     print('координаты не равны нулю по условию')
#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# nomer_chetverti = int(input('Введите номер четверти от 1 до 4 '))
# if nomer_chetverti == 1:
#     print('Х и Y координаты положительные числа')
# elif nomer_chetverti == 2:
#     print('Х координата отрицательное, Y координата положительное числа')
# elif nomer_chetverti == 3:
#     print('Х и Y координаты отрицательные числа')
# elif nomer_chetverti == 4:
#     print('Х координата положительное, Y координата отрицательное число')
# else:
#     print('Вы ввели некорректные данные')

#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# import math
# x1_coordinate = int(input('Введите координату Х первой точки '))
# y1_coordinate = int(input('Введите координату Y первой точки '))
# x2_coordinate = int(input('Введите координату Х второй точки '))
# y2_coordinate = int(input('Введите координату Y второй точки '))
# distance = math.sqrt(((x2_coordinate-x1_coordinate)**2)+((y2_coordinate-y1_coordinate)**2))
# print (round(distance,3))

#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
my_number = (input('Введите число '))
sum=0
array_numbers =[]
for symbol in my_number:
    if '1234567890'.find(symbol) != -1:
        array_numbers.append(int(symbol))
for i in (array_numbers):
    sum=sum+i
print (sum)
