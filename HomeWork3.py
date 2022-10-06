#1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
numb_spis = int(input('Введите количество элементов списка\n'))
print('Введите элементы списка через клавишу Enter')
spis =[]
sum_spis = 0
for i in range(numb_spis):
    spis.append(int(input()))
    if i % 2 != 0:
        sum_spis += spis[i]
print(f'Исходный список: {spis}')
print(f'Сумма элементов, стоящих на нечетных позициях, равна {sum_spis}')


#2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];
#         - [2, 3, 5, 6] => [12, 15]
numb_spisok = int(input('Введите количество элементов списка\n'))
print('Введите элементы списка через клавишу Enter')
spisok =[]
spisok_pr = []
for i in range(numb_spisok):
    spisok.append(int(input()))
print(f'Исходный список: {spisok}')
if numb_spisok % 2 == 0:
    k = numb_spisok // 2
else:
    k = numb_spisok // 2 + 1
for i in range(k):
    spisok_pr.append(spisok[i] * spisok[numb_spisok - i - 1])
print(f'Список произведений пар чисел: {spisok_pr}')


#3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
numb_spisok_real = int(input('Введите количество элементов списка\n'))
print('Введите элементы списка через клавишу Enter')
spisok_real =[]
spisok_dr = []
if numb_spisok_real != 0:
    for i in range(numb_spisok_real):
        spisok_real.append(float(input()))
        dr = round(spisok_real[i] - int(spisok_real[i]), 5)
        if dr != 0:
            spisok_dr.append(dr)
    if spisok_dr != []:
        max_dr = max(spisok_dr)
        min_dr = min(spisok_dr)
    else:
        max_dr = 0
        min_dr = 0
    print(f'Исходный список: {spisok_real}\n')
    print(f'Разница между максимальным и минимальным значением дробной части элементов равна {max_dr - min_dr}')
else:
    print('Список пустой!')


#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101
#         - 3 -> 11
#         - 2 -> 10
number_dec = int(input('Введите число\n'))
number_bin = ''
if number_dec == 0:
    number_bin = '0'
while number_dec > 0:
    number_bin = str(number_dec % 2) + number_bin
    number_dec = number_dec // 2
print(f'Число в двоичном представлении равно {number_bin}')


#5. Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
numb_Fibonach = int(input('Введите число\n'))
if numb_Fibonach == 0:
    print('Список чисел Фибоначчи: [0]')
else:
    spisok_Fibonach_pol = [0, 1]
    spisok_Fibonach_all = []
    for i in range(2, numb_Fibonach + 1):
        spisok_Fibonach_pol.append(spisok_Fibonach_pol[i-2]+spisok_Fibonach_pol[i-1])
    k = -1
    for i in range(numb_Fibonach,1,-1):
        spisok_Fibonach_all.append(k * spisok_Fibonach_pol[i])
        k = -k
    spisok_Fibonach_all.extend(spisok_Fibonach_pol)
    print(f'Список чисел Фибоначчи: {spisok_Fibonach_all}')


#6. Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных
# холодильников. Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными,
# состоящая из строчных букв и цифр, и если в ней присутствует слово "anton"
# (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число n – количество холодильников.
# В последующих n строках вводятся строки, содержащие латинские строчные
# буквы и цифры, в каждой строке от 5 до 100 символов.
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
numb_refr = int(input('Введите количество холодильников\n'))
anton = ['a', 'n', 't', 'o', 'n']
str_refr = []
refr = []
k = 0
for i in range(numb_refr):
    str_refr.append(input(f'Введите строку номер {i+1}\n'))
    k = 0
    for symb in str_refr[i]:
        if symb == anton[k] and k < len(anton):
            k += 1
    if k == len(anton):
        refr.append(i + 1)
if refr != []:
    print(f'Номера зараженных холодильников: {refr}')
else:
    print('Зараженных холодильников нет')