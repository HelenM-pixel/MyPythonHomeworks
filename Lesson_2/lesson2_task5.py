def month_to_season(month_num):

    if not (1 <= month_num <= 12):
        return "Ошибка: Неверный номер месяца. Введите число от 1 до 12."

    if month_num in [12, 1, 2]:
        return "Зима"
    elif month_num in [3, 4, 5]:
        return "Весна"
    elif month_num in [6, 7, 8]:
        return "Лето"
    elif month_num in [9, 10, 11]:
        return "Осень"


print("Введите номер месяца:")
m = int(input())
season = month_to_season(m)
print(f"Название сезона: {season}")
