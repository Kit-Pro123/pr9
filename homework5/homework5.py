import random

def more_high(l):
    if len(l) < 2:
        print("Список должен содержать хотя бы два элемента.")
        return
    try:
        print("Элементы, которые больше предыдущего элемента:")
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                print(l[i])
    except TypeError:
        print("Некоторые элементы списка не поддерживают сравнение.")
        return

numbers=list()

for i in range(10):
    number = random.randint(1, 10)
    numbers.append(number)

print("Исходный список:", numbers)
more_high(numbers)