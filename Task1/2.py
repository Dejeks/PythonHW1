##Задача 2: Найдите сумму цифр трехзначного числа.

numb = int(input("Введите число "))

print(sum([numb % 10, numb // 10 % 10, numb // 100 % 10]))