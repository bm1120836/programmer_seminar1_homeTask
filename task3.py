# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = None
y = None
print('Введите координату X')
x = int(input())
print('Введите координату Y')
y = int(input())
if x > 0 and y > 0:
    print('Точка находится в первой четверти.')
elif x < 0 and y > 0:
    print('Точка находится во второй четверти.')
elif x < 0 and y < 0:
    print('Точка находится в третьей четверти.')
elif x > 0 and y < 0:
    print('Точка находится в четвертой четверти.')
elif x == 0 and y == 0:
    print('Точка находится в центре системы координат.')
