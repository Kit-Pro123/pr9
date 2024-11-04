def squares_between(a, b):
    squares = [i**2 for i in range(int(a)+1, int(b))]
    return squares

def user_input():
    while True:
        try:
            a = float(input("Введите значение a: "))
            b = float(input("Введите значение b: "))
            return a, b
        except ValueError:
            print("Пожалуйста, введите числа.")

a, b = user_input()

if a > b:
    a, b = b, a
if a == b:
    print('Введенные числа равны, тут нечего сравнивать')
else:
    squares = squares_between(a, b)
    print(f"Квадраты целых чисел между {a} и {b}: {squares}")