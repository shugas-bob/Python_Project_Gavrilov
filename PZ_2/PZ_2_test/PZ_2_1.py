"""
Вариант 1. Известно, что X кг конфет стоит A рублей. Определить, сколько стоит
1 кг и Y кг этих же конфет.
"""

try:
    x_kg = float(input("Введите сколько кг конфет: "))
    a_rub = float(input("Введите стоимость (руб): "))

    if x_kg <= 0 or a_rub <= 0:
        raise ValueError("Вес и стоимость должны быть больше нуля!")

    kg = a_rub / x_kg

except ValueError as err:
    print(f"Ошибка ввода: {err}")

else:
    print(f"1 килограмм конфет стоит (руб): {kg:.2f}")

    try:
        y_kg = float(input("Введите второй кг конфет: "))
        if y_kg <= 0:
            raise ValueError("Второй вес должен быть больше нуля!")
            
        print(f"Второй вес стоит: {y_kg * kg:.2f}")
        
    except ValueError as err:
        print(f"Ошибка ввода второго веса: {err}")
