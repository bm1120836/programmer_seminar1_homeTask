# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

range = [0, 1]
flag = True
for x in range:
    for y in range:
        for z in range:
            f1 = not(x or y or z)
            f2 = not(x) and not(y) and not(z)
            print(x, y, z, f1==f2)
            if f1 != f2:
                flag = False
if flag == True:
    print ('Теорема доказана')
else:
    print('Утверждение ложно')