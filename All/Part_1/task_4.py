# Google search - 2 ️
# На вход программе подается натуральное число
# n, затем
# n строк, затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
#
# Формат входных данных
# На вход программе подаются натуральное число
# n — количество строк, затем сами строки в указанном количестве, затем число k, затем сами поисковые запросы.

n = int(input())
ss = []
sz = []
q = []
for i in range(1,n+1):
    st = input()
    ss.append(st)
z = int(input())
for k in range(1,z+1):
    g = input()
    sz.append(g)
for a in ss:
    counter = 0
    for b in sz:
        if b.lower() in a.lower():
            counter += 1
        if counter == len(sz):
            print(a)