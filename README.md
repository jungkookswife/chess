# Шахматы
Выполнила: Бурганова Дарья, ФТ-220008.

Задание: Поле шахматной доски определяется парой натуральных чисел, каждое из которых не превосходит восьми:
первое число — номер вертикали (при счете слева направо),
второе число — номер горизонтали (при счете снизу вверх).
Даны натуральные числа k, l, m, n, каждое из которых не превосходит восьми.

Требуется:

а) Выяснить, являются ли поля (k, I) и (m, n) полями одного цвета.

б) На поле (к, I) расположен ферзь, ладья, слон или конь (должен ввести пользователь). Угрожает ли он полю (m, n)?

в) Выяснить, можно ли с поля (k, I) одним ходом ладьи, ферзя или слона (должен ввести пользователь) попасть на поле (m, n). Если нет, то выяснить, как это можно сделать за два хода (указать поле, на которое приводит первый ход).

***Проект можно открыть в:***

- Visual Studio 

- Atom

Чтобы увидеть программу, Вам следует открыть файл **Untitled-1.py**. Затем нужно ввести четыре натуральных числа с клавиатуры:
```python
k = int(input('Введите k: '))
l = int(input('Введите l: '))
m = int(input('Введите m: '))
n = int(input('Введите n: '))
```
После того, как Вы введете числа, программа проверит, удовлетворяют ли они условию задачи:
```python
if not(1 <= k <= 8) or not(1 <= l <= 8) or not(1 <= m <= 8) or not(1 <= n <= 8):
    print("Координаты должны быть натуральными числами от 1 до 8")
```

Следом программа определит, являются ли поля (k, I) и (m, n) полями одного цвета:
```python
elif (k+l) % 2 == (m+n) % 2:
    print('Поля одного цвета')
else:
    print('Поля разных цветов')
```

Далее Вы должны ввести название фигуры. Программа проверит, угрожает ли она полю (m, n):
```python
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
```

После этого Вы вновь должны ввести название фигуры, чтобы программа выяснила, можно ли с поля (k, I) одним ходом попасть на поле (m, n). Если нет, то выяснит, как это можно сделать за два хода (укажет поле, на которое приводит первый ход):
```python
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
```

Тесты:

![test1](https://sun9-21.userapi.com/impg/wweKcsYKht0qZgLAvyIYu9FfZQ-b1IKh2xqEZg/FX8v8vmc2BM.jpg?size=611x250&quality=96&sign=c8b8c264722c0898bf3481e329463f5a&type=album)
![test2](https://sun9-6.userapi.com/impg/XTg_1OdZtdbbkVtAGYjRBIHo5qup61a0a8UKvw/hbmQLjeHanA.jpg?size=827x253&quality=96&sign=3fa692d5ae892859dfd1e707db2922bf&type=album)
![test2](https://sun9-59.userapi.com/impg/tFMaR-bHBRSqtgSc71jA1A8SPQzrAHWOiVtrMg/IqmR9Z2LRuI.jpg?size=489x255&quality=96&sign=8fe97d957caab3e1ce355930c10f6208&type=album)
