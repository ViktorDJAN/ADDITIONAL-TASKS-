Звездный треугольник
Дано нечетное натуральное число
n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным
n в соответствии с примером:

*
**
***
****
***
**
*
Формат входных данных
На вход программе подается одно нечетное натуральное число.

n = int(input())
a = n// 2 + 1
counter = 0
for i in range(1, n + 1):
    if i <= a :
        counter += 1
        print('*' * counter)
    else:
        counter -= 1
        print('*'* counter)