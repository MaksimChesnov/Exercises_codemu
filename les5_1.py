#1 Выведите текущую дату в формате год-месяц-день.
import datetime
import math

d = datetime.date.today()
print(d)

#2 Попросите пользователя ввести число через консоль. В результате выведите квадратный корень этого числа.

while True:
    num = input('Введите число: ')
    if num.isdigit():
        koren = math.sqrt(int(num))
        break
    else:
        print(f'Это не число.')

print(num, koren)

#3 Напишите программу, которая сформирует следующую строку: 'xxxxx'

str1 = 'x' * 5
print(str1)

#4 Дана некоторая строка со словами: 'aaa bbb ccc eee fff'
#Удалите из этой строки каждое второе слово. В нашем случае должно получится следующее: 'aaa ccc fff'

str1 = 'aaa bbb ccc eee fff'
print(str1)
lst1 = str1.split()
print (lst1)
end = len(lst1)
lst2 = []
for i in range(end):
    print(i, i%2)
    if i % 2 == 0:
        lst2.append(lst1[i])

print(lst2)