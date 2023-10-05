k = int(input('Введите k: '))
l = int(input('Введите l: '))
m = int(input('Введите m: '))
n = int(input('Введите n: '))
if not(1 <= k <= 8) or not(1 <= l <= 8) or not(1 <= m <= 8) or not(1 <= n <= 8):
    print("Координаты должны быть натуральными числами от 1 до 8")
elif (k+l) % 2 == (m+n) % 2:
    print('Поля одного цвета')
else:
    print('Поля разных цветов')


figure = input('Введите фигуру: ')
if figure == "ферзь":
    if k == m or l == n or abs(k - m) == abs(l - n):
        print("Фигура угрожает полю (", m, ",", n, ")")
    else:
        print("Фигура не угрожает полю (", m, ",", n, ")")
elif figure == "ладья":
    if k == m or l == n:
        print("Фигура угрожает полю (", m, ",", n, ")")
    else:
        print("Фигура не угрожает полю (", m, ",", n, ")")
elif figure == "слон":
    if abs(k - m) == abs(l - n):
        print("Фигура угрожает полю (", m, ",", n, ")")
    else:
        print("Фигура не угрожает полю (", m, ",", n, ")")
elif figure == "конь":
    if (abs(k - m) == 2 and abs(l - n) == 1) or (abs(k - m) == 1 and abs(l - n) == 2):
        print("Фигура угрожает полю (", m, ",", n, ")")
    else:
        print("Фигура не угрожает полю (", m, ",", n, ")")
else:
    print("Некорректная фигура")



figure1 = input('Введите фигуру: ')
if figure1 == 'ладья':
    if k == m or l == n:
        print("Фигура может попасть на поле (", m, ",", n, ") за один ход")
    else:
        print("Фигура может попасть на поле (", k, ",", n, ") или (", m, ",", l, ") за первый ход")
elif figure1 == 'ферзь':
    if k == m or l == n or abs(k - m) == abs(l - n):
       print("Фигура может попасть на поле (", m, ",", n, ") за один ход")             
    else:
        print("Фигура может попасть на поле (", k, ",", n, ") или (", m, ",", l, ") или (", k + abs(k - m), ",",  l + abs(l - n), ") за первый ход")
elif figure1 == 'слон':
    if abs(k - m) == abs(l - n):
        print("Фигура может попасть на поле (", m, ",", n, ") за один ход")
    else:
        print("Фигура может попасть на поле (", k + abs(k - m), ",",  l + abs(l - n), ") за первый ход")
else:
    print("Некорректная фигура")