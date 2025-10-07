def fizz_buzz(num):
    for x in range(1, num + 1):
        if x % 5 == 0 and x % 3 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")

        else:
            print(x)


m = int(input("Введите число: "))  # для проверки лучше 15 и более
fizz_buzz(m)
