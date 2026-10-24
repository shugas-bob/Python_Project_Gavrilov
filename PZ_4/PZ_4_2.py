'''
2. Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
деления, найти количество и сумму его цифр.
'''

while True:
    try:
        n = int(input("Введите целое число N (> 0): "))
        if n > 0:
            break
        print("Ошибка: Число должно быть строго больше нуля.")
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите целое число.")

count = 0
total_sum = 0
temp_n = n

while temp_n > 0:
    digit = temp_n % 10
    total_sum += digit
    count += 1
    temp_n //= 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total_sum}")