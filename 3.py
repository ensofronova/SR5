# def isint(x):
#     try:
#         int(x)
#         return 1
#     except ValueError:
#         return 0
    
a=[]
N=input("Введите количество элементов в массиве: ")
# if isint(N)==0:
#     while isint(N)!=1:
#         print('Ошибка! Введите число!')
#         N=input("Введите количество элементов в массиве: ")
N=int(N)
d=input('Введите дельта: ')
# if isint(d)==0:
#     while isint(d)!=1:
#         print('Ошибка! Введите число!')
#         d=input('Введите дельта: ')
d=int(d)
from random import randint
for i in range(N):
    a.append(randint(1,10))
print('Исходный массив:',*a)
k=0
for i in range(N):
    if (a[i]-d==min(a)) or (a[i]+d==min(a)):
        k+=1
print('Количество элементов, отличающихся от минимального на дельта равно',k)