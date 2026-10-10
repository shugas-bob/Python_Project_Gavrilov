try:
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
except ValueError:
    print("Число должно быть!!")

c = (a < 0) or (b < -2)
print(f"Высказывание «A > 0 или B < -2»: {c}")