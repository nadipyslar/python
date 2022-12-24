#Напишите программу, которая принимает на вход вещественное число и показывает сумму
#my_number = (input('Введите число '))
#sum=0
#array_numbers =[]
#for symbol in my_number:
#    if '1234567890'.find(symbol) != -1:
#        array_numbers.append(int(symbol))
#for i in (array_numbers):
#    sum=sum+i
#print (sum)

#Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
#number=int(input('Введите число: '))
#array_numbers=[]
#for i in range(1,number+1):
#     array_numbers.append((1 + 1/i)**i)
#sum=0
#for i in array_numbers:
#    sum+=i
#print(f'Для N ={number}:->', end='')
#print(array_numbers)
#print(f'Сумма', end=' ')
#print(round(sum,2))

#Реализуйте алгоритм перемешивания списка. 
#НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

#import random
#my_list=[]
#for i in range(10):
#    my_list.append(random.randint(0,100))
#print (my_list)
#temporary=0
#for i in range(9):
#    temporary=my_list[i]
#    my_list[i]=my_list[i+1]
#    my_list[i+1]=temporary
#print(my_list)

#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом

#import random
#my_list=[]
#for i in range(int(input('Введите количество элементов списка: '))):
#    my_list.append(random.randint(0,100))
#print(my_list)
#sum=0
#for i in range(len(my_list)):
#    if i%2:
#        sum+=my_list[i]
#print(f'Сумма элементов списка с нечетными индексами равна {sum}')

#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#import random
#my_list=[]
#for i in range(int(input('Введите количество элементов списка: '))):
#    my_list.append(random.randint(0,100))
#print(my_list)
#dlina = len(my_list)
#if dlina%2:
#    middle=dlina//2+1
#else:
#    middle=dlina//2
#my_mult=[]
#for i in range (middle):
#    my_mult.append(my_list[i]*my_list[-1-i])
#print(my_mult)
#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
import random
my_list=[]
for i in range(int(input('Введите количество элементов списка: '))):
    my_list.append(random.uniform(0,100))
print(my_list)
my_int_list=[int(x) for x in my_list]
print(my_int_list)
float_part=[]
temp=0
while len(my_list)!=temp:
    z=my_list[temp]-my_int_list[temp]
    temp=temp+1
    float_part.append(z)
print(float_part)
for i in range(len(float_part)):
    if float_part[i]==0:
        float_part.remove(a[i])
print(float_part)
diff=max(float_part)-min(float_part)
print(f'Разница между максимальной и минимальной дробной частью составляет {diff}')