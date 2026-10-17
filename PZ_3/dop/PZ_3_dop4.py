'''
Дано целое число. Если оно является положительным,
то прибавить к нему 20, в противном случае вычесть из него 5.
'''

while True:
    user_input = input("Введите целое число: ")

    try:
        number = int(user_input)

        print(f"Отлично! Вы ввели целое число: {number}")
        break

    except ValueError:
        print("Ошибка: нужно писать только целые числа! Попробуйте еще раз.")

if number < 0:
    print(number + 20)
else:
    print(number - 5)