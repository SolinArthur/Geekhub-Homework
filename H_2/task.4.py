# 4.Напишите скрипт, который принимает <число> от пользователя, а затем <число> раз запрашивает
# у пользователя ввод строки. В конце скрипт должен распечатать результат объединения всех строк <number>.

numbers = int(input("Введите число: "))
for i in range(numbers):
    text = numbers * input("Текст: ")
    print(text)