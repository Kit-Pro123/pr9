def counter(numbers):
    chet_count = 0
    nechet_count = 0
    for number in numbers:
        if number % 2 == 0:
            chet_count += 1
        else:
            nechet_count += 1
    return chet_count, nechet_count

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
        print("Пожалуйста, введите корректное целое число или 'end' для завершения.")
chet_count, nechet_count = counter(user_numbers)
print(f"Вы ввели {len(user_numbers)} чисел.")
print(f"Четные числа: {chet_count}")
print(f"Нечетные числа: {nechet_count}")