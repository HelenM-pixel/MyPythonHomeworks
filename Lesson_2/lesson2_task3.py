# модуль математики не поставился
def square(a):
    return a * a


side = float(input("Введите сторону квадрата: "))
if side != int(side):
    side = int(side) + 1
answer = square(side)
print(f"Площадь квадрата со стороной {side} равна {answer}")
