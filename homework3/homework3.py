def nechet_numbers():
    user_numbers = []
    print("Введите числа (введите 'end' для завершения ввода):")
    while True:
        user_input = input()
        if user_input == 'end':
            break
        try:
            number = int(user_input)
            user_numbers.append(number)
        except ValueError:
            print("Пожалуйста, введите целое число или 'end' для завершения.")
    odd_numbers = [num for num in user_numbers if num % 2 != 0]
    print("Нечетные элементы списка:", odd_numbers)

nechet_numbers()