import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def get_user_numbers():
    user_numbers = []
    print("Выберите по одному числу из каждой строки:")
    for i in range(len(ticket)):
        while True:
            try:
                number = int(input(f"Строка {i + 1} (выберите число из {ticket[i]}): "))
                if number in ticket[i]:
                    user_numbers.append(number)
                    break
                else:
                    print("Некорректное число. Пожалуйста, выберите число из строки.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")
    return user_numbers

def random_numbers():
    r_numbers = []
    for r in ticket:
        r_number = random.choice(r)
        r_numbers.append(r_number)
    return r_numbers

def count_matches(user_numbers, random_numbers):
    return len(set(user_numbers) & set(random_numbers))

def lottery():
    user_numbers = get_user_numbers()
    random_numbers = random_numbers()
    print("Ваши числа: ", user_numbers)
    print("Числа компьютера: ", random_numbers)

lottery()