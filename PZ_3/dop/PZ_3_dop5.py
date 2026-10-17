# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

a = int(input())
b = int(input())
c = a + b
if c == 5:
    print(c + 1)
else:
    print(c - 2)
