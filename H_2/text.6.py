# 6.Напишите сценарий для проверки того, содержится ли значение из пользовательского ввода
# в группе значений.
#e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#[1, 2, 'u', 'a', 4, True] --> 5 --> False

a = [1, 2, 'u', 'a', 4, True]
b = input("Введите текст: ")
if b.isdigit():
    b = int(b)
print(b in a)
