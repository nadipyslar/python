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
                koef = random.randit(0,100)
                if koef!=0:
                    break
                else:
                    print ("contains zero") 
            equation [i]=koef
        else:
            equation[i]=random.randint(0,100)
    return equation
    print(create_eq())



