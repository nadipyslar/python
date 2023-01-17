#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
def create_eq():
    equation={}
    n=int(input("Введите число n: "))
    for i in range (n, -1, -1):
        if i == n:
            while True:
                koef = random.randint(0,100)
                if koef!=0:
                    break
                else:
                    print ("contains zero") 
            equation [i]=koef
        else:
            equation[i]=random.randint(0,100)
    return equation
my_dict= (create_eq())
print (my_dict)
def reserve (d):
    return {v: k for k, v in d.items()}
my_dict_reversed= reserve(my_dict)
print(my_dict_reversed)

#{5: 43, 4: 67, 3: 34, 2: 34, 1: 36, 0: 6}
#43X**5
string = ', '.join(f'{k} {v}' for k,v in my_dict_reversed.items())
print (string)
polymonial = string.replace(', ', '+').replace(' ','*x**')
print (polymonial)

