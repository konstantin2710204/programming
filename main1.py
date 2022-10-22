import math
from random import randint

print("Разделить массив на массивы с четными и нечетными числами")
a = []
for i in range(0,10):
    x1 = randint(0,100)
    a.append(x1)
print(a)

# Четные и нечетные числа

chet = []
nechet = []
for i in range(1, len(a)):
    if i % 2 == 0:
        chet.append(a[i])
    else:
        nechet.append(a[i])
print("Массив с четными числами", chet, "Массив с нечетными числами", nechet, sep="\n")

# Минимальное число в массиве
print("Найти k наименьших элементов массива")
k = int(input("Введите число k: "))
minimum = []
min = a[0]
for i in range(0, k):
    for i in range(1, len(a)):
        if min > a[i]:
			min, a[i] = a[i], min
			minimum.append(min)
print("Минимальные числа в массиве", minimum, sep="\n")

# Максимальное число в массиве
maximum = []
max = a[9]
for i in range(0, k):
    for i in range(1, len(a)):
        if max < a[i]:
			max, a[i] = a[i], max
			maximum.append(max)
print("Наибольшие числа в массиве", maximum, sep="\n")

# Среднее значение

avg = sum(a) / len(a)
for i in range(1, len(a)):
    if a[i] > avg:
        print("Числа, превышающие среднее значение чисел в массиве", a[i], sep="\n")

# Вычисления

print("Вычисление значений")

print("(101 + 0) / 3 = ", (101 + 0) / 3)
print("3.0e-6 * 10000000.1 = ", 0.0000030 * 10000000.1)
print("true && true =", True + True)
print("false && true =", False + True)
print("(false && false) (true && true) =", ((False + False) * (True + True)))
print("(false false) && (true && true) =", ((False * False) + (True + True)))

# Сравнение чисел

print("Сравнение 4 чисел\n")

a = int(input("Введите целое число: "))
b = int(input("Введите целое число: "))
c = int(input("Введите целое число: "))
d = int(input("Введите целое число: "))

if a == b & b == c & a == d:
    print ("Числа равны")
else:
    print("Числа не равны")

# Умножение без операции умножения

print("Умножение без использования умножения")

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
result = 0
z = 0

while z != (abs(y)):
    result = result + (abs(x))
    z = z + 1

if (y or x) < 0:
    result = -result

print(x, "*", y, "=", result)

# Температура

print("Перевод температуры из градусов Фаренгейта в градусы Цельсия")

far = int(input("Введите температуру в Фаренгейтах: "))
cel = ((far - 32) * 5) / 9
print("Температура в Цельсиях:", cel)

# ИМТ

print("Рассчет индекса массы тела")

h = int(input("Введите рост: "))
w = int(input("Введите вес: "))
imt = (w / math.pow(h, 2)) * 10000
print("ИМТ: ", imt)

# Степени

print("Возведение числа в степень")

k = int(input("Введите число для рассчета его степеней"))
print(math.pow(k, 2), math.pow(k, 3), math.pow(k, 4))

# Треугольник

oneside = int(input("Введите сторону треугольника"))
twoside = int(input("Введите сторону треугольника"))
threeside = int(input("Введите сторону треугольника"))

if oneside <= 0 or twoside <= 0 or threeside <= 0:
    print("Стороны треугольника должны быть натуральными числами")
elif oneside >= twoside + threeside or twoside >= oneside + threeside or threeside >= oneside + twoside:
    print("Полученный треугольник не существует")
elif oneside != twoside and twoside != threeside and oneside != threeside:
    print("Полученный треугольник разносторонний")
elif oneside == threeside and oneside == twoside and twoside == threeside:
    print("Полученный треугольник равносторонний")
elif oneside == threeside or oneside == twoside or twoside == threeside:
    print("Полученный треугольник равнобедренный")
