# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3] --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input("Введите N:"))
numbers = []
for i in range(-n, n+1):
    numbers.append(i)
print(numbers)
a, b, c, = (input()).split()
print(a, b, c)
i = 0 
mult = 1

if i == a:
    print(numbers[i])
    mult *= numbers[i]
else:
    i +=1
if b == i:
    mult *= numbers[i]
else:
    i +=1
if c == i:
   mult *= numbers[i]
else:
    i +=1
print(mult)

