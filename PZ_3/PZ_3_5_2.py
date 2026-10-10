'''2. Мастям игральных карт присвоены порядковые номера: 1– пики, 2 – трефы, 3 –
бубны, 4 – червы.
Достоинству карт, старших десятки, присвоены номера:
11 – валет, 12 – дама, 13 – король, 14 – туз.
Дано трехзначное число, в котором первая цифра указывает на масть,
 а вторые две на достоинство карты.
 Вывести соответствующее название карты вида «дама червей», «туз треф» и т.п.'''

while True:
    try:
        num = int(input("Введите трехзначное число "))
        if num < 100 or num > 999:
            print("Число должно быть трехзначным")
        break
    except ValueError:
        print("Вводите число!")
hundreds, tens = divmod(num, 100)
if hundreds > 4 or tens < 10 or tens > 14:
    print("Не найдено таких мастей")

elif hundreds == 1:
    hundreds = 'пики'

elif hundreds == 2:
    hundreds = 'трефы'

elif hundreds == 3:
    hundreds = 'бубны'

elif hundreds == 4:
    hundreds = 'черви'

elif tens == 11:
    tens = 'валет'

elif tens == 12:
    tens = 'дама'

elif tens == 13:
    tens = 'король'

elif tens == 14:
    tens = 'туз'

print(tens, hundreds)