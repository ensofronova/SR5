# def isint(x):
#     try:
#         int(x)
#         return 1
#     except ValueError:
#         return 0
    
a=[]
b=[]
Na=input("Введите количество элементов в первом массиве: ")
# if isint(Na)==0:
#     while isint(Na)!=1:
#         print('Ошибка! Введите число!')
#         Na=input("Введите количество элементов в первом массиве: ")
Na=int(Na)
from random import randint
for i in range(Na):
    a.append(randint(1,10))
print('Первый массив:',*a)

Nb=input("Введите количество элементов во втором массиве: ")
# if isint(Nb)==0:
#     while isint(Nb)!=1:
#         print('Ошибка! Введите число!')
#         Nb=input("Введите количество элементов во втором массиве: ")
Nb=int(Nb)
for i in range(Nb):
    b.append(randint(1,10))
print('Второй массив:',*b)
c=[]
for i in range(Na):
    for j in range(Nb):
        if a[i]==b[j] and not(a[i] in c):
            c.append(a[i])
            break
if len(c)!=0:
    print('Общие элементы двух массивов:',*c)
else:
    print('Данные два массива общих элементов не имеют')