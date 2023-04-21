# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5
# def multiplier_number(num):
#   count = 0
#   multiplier = 2
#   print(f'{num}->', end=" ")
#   while num>1:
#     if num%multiplier == 0:
#       num /= multiplier
#       print(multiplier, end=' ')
#       count+=1
#     else: multiplier+=1
#   return print(f'Колличество делителей: {count}')
# number = int(input("Введите число: "))
#multiplier_number(number)
#----------------------------------------
# Задача 2. В первом списке находится информация об ассортименте мороженного, во втором списке - информация о том, какое мороженное есть на складе. # Выведите названия того товара, который закончился.
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»
# tracking_product = {'Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка','Пломбир'}
# product_stock = {'Сливочное', 'Вафелька', 'Сладкоежка'}
# result = tracking_product.difference(product_stock)
# print(f'Закончилось: {result}')
#-----------------------------------------------------------------------
# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142
# import math
# places_pi = int(input("Введите колличество знаков после запятой: "))
# number = round(math.pi, places_pi)
# print(number)
# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8
# Запишем многочлены в файлы

def parse_polynomial(poly_str):
    terms = poly_str.split(' + ')
    parsed_poly = {}
    
    for term in terms:
        if 'x^' in term:
            coef, _, power = term.partition('x^')
            coef = int(coef) if coef else 1
            parsed_poly[int(power)] = int(coef)
        elif 'x' in term:
            coef, _, _ = term.partition('x')
            coef = int(coef) if coef else 1
            parsed_poly[1] = coef
        else:
            parsed_poly[0] = int(term)
    
    return parsed_poly

def add_polynomials(poly1, poly2):
    result = poly1.copy()
    
    for power, coef in poly2.items():
        if power in result:
            result[power] += coef
        else:
            result[power] = coef
            
    return result

def Task4():
    with open("polynomial_1.txt", "r") as file1:
        poly1_str = file1.read()
        poly1 = parse_polynomial(poly1_str)

    with open("polynomial_2.txt", "r") as file2:
        poly2_str = file2.read()
        poly2 = parse_polynomial(poly2_str)

    result_poly = add_polynomials(poly1, poly2)

    result_str = " + ".join(f"{coef}x^{power}" if power > 1 else (f"{coef}x" if power == 1 else str(coef)) for power, coef in sorted(result_poly.items(), reverse=True))
    print(f"Результат: {result_str}")
Task4()