import random

def cicle_sdvig(l):
    if len(l) == 0:
        return l
    last_element = l[-1]
    for i in range(len(l)-1,0,-1):
        l[i] = l[i-1]
    l[0] = last_element
    return l

numbers=list()

for i in range(10):
    number = random.randint(1, 10)
    numbers.append(number)

print("Исходный список:", numbers)
print("Список после сдвига вправо:", cicle_sdvig(numbers))