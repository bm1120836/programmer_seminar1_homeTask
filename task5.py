# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math
print('Введите координату X первой точки')
x1 = int(input())
print('Введите координату Y первой точки')
y1 = int(input())
print('Введите координату X второй точки')
x2 = int(input())
print('Введите координату Y второй точки')
y2 = int(input())
x = x1 - x2
y = y1 - y2
number = x*x + y*y
l = math.sqrt(number)
print('Расстояние между точками равно: ')
print(l)