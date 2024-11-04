import random

def swap_min_max(l):
    if len(l) < 2:
        print("Список слишком мал для выполнения операции.")
        return l
    try:
        min_index = l.index(min(l))
        max_index = l.index(max(l))
        l[min_index], l[max_index] = l[max_index], l[min_index]
    except TypeError:
        print("Элементы списка не поддерживают сравнение чисел с буквами или другими элементами.")
        return
    return l

numbers=list()

for i in range(10):
    number = random.randint(1, 10)
    numbers.append(number)

print("Исходный список:", numbers)
s_numbers = swap_min_max(numbers)
if s_numbers!=None:
    print("Список после замены минимального и максимального элементов:", s_numbers)