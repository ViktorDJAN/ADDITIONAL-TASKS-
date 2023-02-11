# Палиндром
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение
# True если указанный текст является палиндромом и False в противном случае.
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

# объявление функции
def is_palindrome(text):
    a = txt
    s = a
    b =''
    for i in a:
        if i.isalpha():
            b += i.lower()
            c = b[::-1]
    if b == c:
        return True
    else:
        return False
    pass
# считываем данные
txt = input()
# вызываем функцию
print(is_palindrome(txt))