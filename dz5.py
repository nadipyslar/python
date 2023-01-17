#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c-> aaaaabbbcccc

#string = input("Введите строку для зашифровки: ")
#count=1
#for i in range (1,len(string)):
#        if string[i]==string[i-1]:
#            count+=1
#        else:
#            print(count,string[i-1])
#            count=1
#print(count,string[i])

#string1 = input("Введите строку для расшифровки: ")
#deshifrovanie = ''
#count = ''
#for char in string1:
#        if char.isdigit():
#            count += char
#        else :
#            deshifrovanie += int(count) * char
#           count = ''
#print (deshifrovanie)

#Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

#import random
#whos_turn=random.randint(1,2)
#sum = random.randint(50,200)
#print(f'На столе лежит {sum} конфет')
#while sum in range (28,200):
#    if whos_turn ==1:
#        first_player=int(input('Первый игрок, сколько конфет от 1 до 28 ты возьмешь?'))
#        whos_turn=whos_turn+1
#        sum=sum-first_player    
#    else:
#        second_player=int(input('Второй игрок, сколько конфет от 1 до 28 ты возьмешь?'))
#        whos_turn=whos_turn-1
#        sum=sum-second_player
#if whos_turn==1:
#    print('Победил первый герой')
#else:
#    print('Победил второй герой')


import random
whos_turn=random.randint(1,2)
sum = random.randint(50,100)
print(f'На столе лежит {sum} конфет')
while sum in range (28,100):
    if whos_turn ==1:
        first_player=int(input('Первый игрок, сколько конфет от 1 до 28 ты возьмешь?'))
        whos_turn=whos_turn+1
        sum=sum-first_player    
    else:
        bot=random.randint(1,28)
        print(f'Бот взял {bot} конфет')
        whos_turn=whos_turn-1
        sum=sum-bot
if whos_turn==1:
    print('Победил первый герой')
else:
    print('Победил бот')