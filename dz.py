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
number=int(input('Введите число: '))
array_numbers=[]
for i in range(1,number+1):
     array_numbers.append((1 + 1/i)**i)
sum=0
for i in array_numbers:
    sum+=i
print(f'Для N ={number}:->', end='')
print(array_numbers)
print(f'Сумма', end=' ')
print(round(sum,2))
