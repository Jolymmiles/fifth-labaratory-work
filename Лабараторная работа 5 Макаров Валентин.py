import math

number = int(input('Введите номер задания:'))
if number == 1:  # Task 1
    t = int(input('Введите температуру воздуха:'))
    if t > 10: print('Хорошая погода')
elif number == 2:  # Task 2
    P = int(input('Введите оценку:'))
    if P == 5:
        print('Молодец!')
    elif P == 4:
        print('Хорошо!')
    elif P <= 3:
        print('Лентяй!')
elif number == 3:  # Task 3
    digit = int(input('Введите число:'))
    if (digit % 4 == 0) and (digit % 2 == 0):
        print('Число кратно 4 и четное!')
    elif (digit % 5 == 0) and (digit % 2 != 0):
        print('Число кратно 5 и нечетное!')
elif number == 4:  # Task 4
    D = int(input('Введите диаметр поперечного сечения:'))
    A = int(input('Введите ширину бруска:'))
    a = A * math.sqrt(2)
    if a <= D:
        print('Можно.')
    else:
        print('Нельзя')
elif number == 5:  # Task 5
    seat = int(input('Введите место:'))
    if seat > 54:
        print('Таких мест нет!')
    elif seat <= 54:
        if seat >= 37:
            print('Бокове место')
        elif seat < 37:
            print('Купе')
        if seat % 2 == 0:
            print('Верхнее место')
        elif seat % 2 != 0:
            print('Нижнее место')
elif number == 6:  # Task 6
    summa = int(input('Введите сумму:'))
    if summa % 2 != 0:
        print('Невозможно разменять!')
    elif summa % 2 == 0:
        summa500 = summa // 500
        summa100 = (summa - summa500 * 500) // 100
        summa10 = (summa - summa500 * 500 - summa100 * 100) // 10
        summa2 = (summa - summa500 * 500 - summa100 * 100 - summa10 * 10) // 2
        print(str(summa500) + ' купюр по 500',
              str(summa100) + ' купюр по 100',
              str(summa10) + ' купюр по 10',
              str(summa2) + ' купюр по 2')
elif number == 7:  # Task 7
    A = int(input('Ребро куба:'))
    H = int(input('Высота цилиндра:'))
    R = int(input('Радиус основания цилиндра:'))
    M = int(input('Объем жидкости:'))
    Cylinder = math.pi * R ** 2 * H
    Cube = A ** 3
    if Cube >= M:
        print('Вода поместится в кубе')
    elif Cylinder >= M:
        print('Вода поместится в цилиндре')
    elif (Cube >= M) and (Cylinder >= M):
        print('Вода поместится и в кубе и в цилиндре')
    else:
        print('Вода нигде не поместится!')
elif number == 8:  # Task 8
    X = int(input('Введите X:'))
    Y = int(input('Введите Y:'))
    Z = int(input('Введите Z:'))
    if X > 0 and Y > 0 and Z > 0:
        if (X + Y > Z) and (X + Z > Y) and (Y + Z > X):
            print('Существует!')
            maxstorona = max(X, Y, Z)
            if (X ** 2 + Y ** 2 == maxstorona ** 2) or (Z ** 2 + X ** 2 == maxstorona ** 2) or (
                    Y ** 2 + Z ** 2 == maxstorona ** 2): print('Это прямоугольник!')
        else:
            print('Такого треугольника не существует!')
elif number == 9:  # Task 9
    X = int(input('Введите число Х:'))
    a = int(input('Введите начало промежутка a:'))
    b = int(input('Введите конец промежутка b:'))
    if X <= b and X >= a:
        print('Принадлежит')
    else:
        print('Не принадлежит')
elif number == 10:  # Task 10
    A = int(input('Введите A:'))
    B = int(input('Введите B:'))
    C = int(input('Введите C:'))
    if A < B < C:
        print('Выолняется неравенство A<B<C')
    elif A > B > C:
        print('Выолняется неравенство A>B>C')
    else:
        print('Ничего не выполняется')
elif number == 11:  # Task 11
    x1 = int(input('Введите координаты левого нижнего угла x1:'))
    y1 = int(input('Введите координаты левого нижнего угла y1:'))
    x2 = int(input('Введите координаты левого нижнего угла x2:'))
    y2 = int(input('Введите координаты левого нижнего угла y2:'))
    a1 = int(input('Введите длинну стороны a1 первого треугольника:'))
    b1 = int(input('Введите длинну стороны b1 первого треугольника:'))
    a2 = int(input('Введите длинну стороны a2 второго треугольника:'))
    b2 = int(input('Введите длинну стороны b1 второго треугольника:'))
    if x1 + a1 > x2 + a2:
        x3 = x1 + a1
    else:
        x3 = x2 + a2
    if y1 + b1 > y2 + b2:
        y3 = y1 + b1
    else:
        y3 = y2 + b2
    print('Координаты правого верхнего угла общего прямоугольника:', 'x=' + str(x3), 'y=' + str(y3))
elif number == 12:  # Task 12
    digit = int(input('Введите число:'))
    d1 = digit // 10
    d2 = digit % 10
    if 4 * (d1 * d1 * d1 + d2 * d2 * d2) == digit ** 2:
        print('Равен')
    else:
        print('Не равен')
elif number == 13:  # Task 13
    a = int(input('Введите сторону стола a:'))
    b = int(input('Введите сторону стола b:'))
    if a > b:
        c = int(input('Введите сторону коробки c:'))
        d = int(input('Введите сторону коробки d:'))
        n1 = (a // c) * (b // d)
        n2 = (a // d) * (b // c)
        if n1 > n2:
            print('Длинной стороной вдоль длинной больше')
        elif n2 > n1:
            print('Длинной стороной вдоль короткой больше')
        elif n1 == n2:
            print('Одинаково')
elif number == 14:  # Task 14
    t = int(input('Введите прошедшее время:'))
    if 1 <= t % 10 <= 3 or 5 < t % 10 <= 8:
        print('Зеленый')
    elif 3 < t % 10 <= 5 or 8 < t % 10 <= 10:
        print('Красный')
elif number == 15:  # Task 15
    a = int(input('Введите сторону коверта a:'))
    b = int(input('Введите сторону коверта b:'))
    c = int(input('Введите сторону открытки c:'))
    d = int(input('Введите сторону открытки d:'))
    if a >= c + 1 and b >= d + 1:
        print('Войдет')
    else:
        print('Не войдет!')
elif number == 16:  # Task 16
    number_of_mounth = int(input('Введите номер месяца:'))
    if number_of_mounth == 1:
        print('Январь')
    elif number_of_mounth == 2:
        print('Февраль')
    elif number_of_mounth == 3:
        print('Март')
    elif number_of_mounth == 4:
        print('Апрель')
    elif number_of_mounth == 5:
        print('Май')
    elif number_of_mounth == 6:
        print('Июнь')
    elif number_of_mounth == 7:
        print('Июль')
    elif number_of_mounth == 8:
        print('Август')
    elif number_of_mounth == 9:
        print('Сентябрь')
    elif number_of_mounth == 10:
        print('Октябрь')
    elif number_of_mounth == 11:
        print('Ноябрь')
    elif number_of_mounth == 12:
        print('Декабрь')
    else:
        print('Такого месяца не сущесвтует!')
#   name_of_mounth='0 Январь Февраль Март Апрель Май Июнь Июлю Август Сентябрь Октябрь Ноябрь Декабрь'.split(' ')
#   mounth=int(input('Введите номер месяца: '))
#   print(name_of_mounth[mounth])
elif number == 17:  # Task 17
    suit_number = int(input('Номер масти:'))
    card_number = int(input('Введите номер карты:'))
    if suit_number == 1:
        m = ' пики'
    elif suit_number == 2:
        m = ' трефы'
    elif suit_number == 3:
        m = ' бубны'
    elif suit_number == 4:
        m = ' червы'
    else:
        print('Такой масти нету!')
    if card_number == 6:
        n = 'Шестерка'
    elif card_number == 7:
        n = 'Семерка'
    elif card_number == 8:
        n = 'Восьмерка'
    elif card_number == 9:
        n = 'Девятка'
    elif card_number == 10:
        n = 'Десятка'
    elif card_number == 11:
        n = 'Валет'
    elif card_number == 12:
        n = 'Дама'
    elif card_number == 13:
        n = 'Король'
    elif card_number == 14:
        n = 'Туз'
    else:
        print('Такой карты нету')
    print(str(n) + str(m))
elif number == 18:  # Task 18
    animals = "Обезьяна Петух Собака Свинья Крыса Корова Тигр Заяц Дракон Змея Лошадь Овца".split(" ")
    colors = "белый черный зеленый красный желтый".split(" ")
    year = int(input('Введите год: '))
    print("{}, {}".format(animals[year % 12], colors[(year % 10) // 2]))
elif number == 19:  # Task 19
    suit_number = '0 Пики Трефы Бубны Червы'.split(' ')
    card_number = '0 1 2 3 4 5 Шестерка Семерка Восьмерка Девятка Десятка Валет Дама Король Туз'.split(' ')
    number_of_suit = int(input('Номер масти: '))
    number_of_card = int(input('Номер карты: '))
    print('{}, {}'.format(card_number[number_of_card], suit_number[number_of_suit]))
elif number == 20:  # Task 20
    year = int(input('Введите год:'))
    mounth = int(input('Введите месяц:'))
    day = int(input('Введите день:'))
    next_year = year
    last_year = year
    if (mounth == 1) or (mounth == 3) or (mounth == 5) or (mounth == 7) or (mounth == 8) or (mounth == 10) or (
            mounth == 12):
        if mounth == 1 and day == 1:
            next_yaer = year
            last_year = year - 1
            next_day = day + 1
            last_day = 31
            next_mounth = mounth
            last_mounth = 12
        elif mounth == 12 and day == 31:
            next_year = year + 1
            last_year = year
            next_day = 1
            last_day = day - 1
            next_mounth = 1
            last_mounth = 12
        elif day < 31:
            next_day = day + 1
            next_mounth = mounth
            last_mounth = mounth
            last_day = day - 1
            if day == 1:
                if (mounth - 1 == 4) or (mounth - 1 == 5) or (mounth - 1 == 9) or (mounth - 1 == 11):
                    last_day = 30
                    next_mounth = mounth
                    last_mounth = mounth - 1
                elif day == 1 and mounth == 3:
                    if (year % 10 == 4 or year % 10 == 8 or year % 10 == 6 or
                            year % 10 == 2 or year % 10 == 0):
                        next_day = day + 1
                        last_day = 29
                        next_mouth = mounth
                        last_mounth = mounth - 1
                    else:
                        next_day = day + 1
                        last_day = 28
                        next_mounth = mounth
                        last_mounth = mounth - 1
        elif day == 31:
            next_day = 1
            last_day = day - 1
            next_mounth = mounth + 1
            last_mounth = mounth
            next_year = year
            last_year = year
    elif (mounth == 4) or (mounth == 6) or (mounth == 9) or (mounth == 11):
        if day < 30:
            if day == 1:
                next_day = day + 1
                last_day = 31
                next_mounth = mounth
                last_mounth = mounth - 1
            else:
                next_day = day + 1
                last_day = day - 1
                next_mounth = mounth
                last_mounth = mounth
        elif day == 30:
            next_day = 1
            last_day = day - 1
            next_mounth = mounth + 1
            last_mounth = mounth
    elif mounth == 2:  # Високостный год
        if (year % 10 == 4 or year % 10 == 8 or year % 10 == 6 or
                year % 10 == 2 or year % 10 == 0):
            if day < 29:
                if day == 1:
                    next_day = day + 1
                    last_day = 31
                    next_mounth = mounth
                    last_mounth = mounth - 1
                else:
                    next_day = day + 1
                    last_day = day - 1
                    next_mounth = mounth
                    last_mounth = mounth
            elif day == 1:
                next_day = day + 1
                last_day = 31
                next_mounth = mounth
                last_mounth = mounth - 1
            elif day == 29:
                next_day = 31
                last_day = day - 1
                next_mounth = mounth + 1
                last_mounth = mounth
        else:  # Месяца на 28
            if day < 28:
                if day == 1:
                    next_day = day + 1
                    last_day = 31
                    next_mounth = mounth
                    last_mounth = mounth - 1
                else:
                    next_day = day + 1
                    last_day = day - 1
                    next_mounth = mounth
                    last_mounth = mounth
            elif day == 1:
                next_day = day + 1
                last_day = 31
                next_mounth = mounth
                last_mounth = mounth - 1
            elif day == 28:
                next_day = 31
                last_day = day - 1
                next_mounth = mounth + 1
                last_mounth = mounth
    else:  # Месяца на 30
        if day < 30:
            next_day = day + 1
            last_day = day - 1
            next_mounth = mounth
            last_mounth = mounth
        elif day == 1:
            last_day = 31
            next_day = day + 1
            next_mounth = mounth
            last_mounth = mounth - 1
        elif day == 30:
            next_day = 31
            last_day = day - 1
            next_mounth = mounth + 1
            last_mounth = mounth
    print('След. дата:', next_year, 'год', next_mounth, 'месяц', next_day, 'день')
    print('Прошлая дата:', last_year, 'год', last_mounth, 'месяц', last_day, 'день')
elif number == 21:  # Task 21
    k = int(input('Введите кол-во грибов:'))
    if k % 10 == 1:
        print('Мы нашли', k, 'гриб в лесу')
    elif k % 10 == 2:
        print('Мы нашли', k, 'гриба в лесу')
    elif k % 10 == 3:
        print('Мы нашли', k, 'гриба в лесу')
    elif k % 10 == 4:
        print('Мы нашли', k, 'гриба в лесу')
    elif k % 10 == 5:
        print('Мы нашли', k, 'грибов в лесу')
    elif k % 10 == 6:
        print('Мы нашли', k, 'грибов в лесу')
    elif k % 10 == 7:
        print('Мы нашли', k, 'грибов в лесу')
    elif k % 10 == 8:
        print('Мы нашли', k, 'грибов в лесу')
    elif k % 10 == 9:
        print('Мы нашли', k, 'грибов в лесу')
    elif k % 10 == 10:
        print('Мы нашли', k, 'грибов в лесу')
elif number == 22:  # Task 22
    n = int(input('Введите число n:'))
    y = (n // 100) % 100
    t = n % 100
    if 1 <= n <= 99999:
        rubl = n // 100
        coins = n % 100
        if (y == 11) or (y == 12) or (y == 13) or (y == 14) or (y == 15) or (y == 16) or (y == 17) or (y == 18) or (
                y == 19):
            q = 'рублей'
        elif (n // 100) % 10 == 1:
            q = 'рубль'
        elif ((n // 100) % 10 == 2) or ((n // 100) % 10 == 4):
            q = 'рубля'
        else:
            q = 'рублей'
        if (t == 11) or (t == 12) or (t == 13) or (t == 14) or (t == 15) or (t == 16) or (t == 17) or (t == 18) or (
                t == 19):
            k = 'копейку'
        elif n % 10 == 1:
            k = 'копейку'
        elif (n % 10 == 2) or (n % 10 == 4):
            k = 'копейки'
        else:
            k = 'копеек'
        print(rubl, q, coins, 'копеек')
elif number == 23:  # Task 23
    number_of_mounth = int(input('Сколько месяцев вы прожили:'))
    years = number_of_mounth // 12
    mounth = number_of_mounth - years * 12
    if (years // 100) % 100 == (11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
        q = 'лет'
    elif (years // 100) % 10 == 1:
        q = 'год'
    elif (years // 100) % 10 == 2 or 4:
        q = 'года'
    else:
        q = 'лет'
    if mounth == 1:
        w = 'месяц'
    elif mounth == 2:
        w = 'месяца'
    elif mounth == 3:
        w = 'месяца'
    elif mounth == 4:
        w = 'месяца'
    else:
        w = 'месяцев'
    print(years, q, mounth, w)
elif number == 24:  # Task 24
    year = int(input('Введите год вашего рождения:'))
    mounth = int(input('Введите месяц вашего рождения:'))
    day = int(input('Введите день вашего рождения:'))
    this_year = int(input('Введите нынешний год:'))
    this_mounth = int(input('Введите нынешний месяц:'))
    this_day = int(input('Введите нынешний день:'))
    allo = 12 - mounth + this_mounth
    if allo <= 12:
        o = 1
    elif allo > 12:
        o = 2
    golo = this_year - year - o
    years_old = (golo * 12 + allo) // 12
    if this_day >= day and this_mounth == mounth:
        years_old = years_old + 1
    elif this_mounth > mounth:
        years_old = years_old + 1
    print(years_old)
elif number == 25:  # Task 25
    year_a = int(input('Введите год рождения первого человека'))
    mounth_a = int(input('Введите месяц рождения первого человека'))
    day_a = int(input('Введите день рождения первого человека'))
    year_b = int(input('Введите год рождения второго человека'))
    mounth_b = int(input('Введите месяц рождения второго человека'))
    day_b = int(input('Введите день рождения первого человека'))
    if mounth_a == mounth_b and year_a == year_b and day_a == day_b:
        print('Они одинакового возраста')
    elif mounth_a == mounth_b and year_a == year_b and day_a < day_b:
        print('Первый человек старше')
    elif mounth_a == mounth_b and year_a == year_b and day_a > day_b:
        print('Второй человек старше')
    elif mounth_a < mounth_b and year_a == year_b:
        print('Первый человек старше')
    elif mounth_a > mounth_b and year_a == year_b:
        print('Второй человек старше')
    elif year_a < year_b:
        print('Первый человек старше')
    elif year_a > year_b:
        print('Второй человек страше')
