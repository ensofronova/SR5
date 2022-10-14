# def isint(x):
#     try:
#         int(x)
#         return 1
#     except ValueError:
#         return 0
#     
# def isfloat(x):
#     try:
#         float(x)
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
x=input("Введите элемент массива: ")
# if isfloat(x)==0:
#     while isfloat(x)!=1:
#         print('Ошибка! Введите число!')
#         x=input("Введите элемент массива: ")
x=float(x)
a.append(x)
m=x
k=-1
for i in range(N-1):
    x=input("Введите элемент массива: ")
#     if isfloat(x)==0:
#         while isfloat(x)!=1:
#             print('Ошибка! Введите число!')
#             x=input("Введите элемент массива: ")
    x=float(x)
    if m<x:
        m=x
        k=i
    a.append(x)
    
print('Данный массив:',*a)
print('Максимальный эллемент:',m)
for i in range(k+2,N):
    a[i]=0
print("Полученный массив:", *a)