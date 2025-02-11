#1 Попросите пользователя ввести два числа целых числа через консоль. 
#Заполните список целыми числами от минимального введенного числа до максимального.
import itertools as iter
import datetime as dt

while True:
    num1 = input('Введите первое число:')
    if num1.isdigit():
        break
    else:
        print(f'Это не число.')

while True:
    num2 = input('Введите второе число:')
    if num2.isdigit():
        break
    else:
        print(f'Это не число.')

lst = [i for i in range(int(num1), int(num2)+1)]
print (lst)

#lst2 = [i for i in iter.count() if i <= num2]
lst2 = []
for i in iter.count(int(num1), 1):
    #print(i, num1, num2)
    lst2.append(i)
    if i == int(num2):       
        break

print(lst2)



#2 Попросите пользователя ввести дату в формате год-месяц-день. 
#Определите день недели, соответствующий этой дате.

days = ["Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday", "Sunday"] 

d = input('Введите дату в формате год-месяц-день YYYY-MM-DD:')
dat = d.split('-')  
print(d, dat)
year, month, day = dat
print (year, month, day)

den = dt.date(int(year), int(month), int(day))
den_ned = den.weekday()

print(den_ned, days[den_ned])





#3 Попросите пользователя ввести год. Определите, високосный этот год или нет.

d = input('Введите год YYYY:')
ost = int(d) % 4
if ost:
    print ('Год невисокосный')
else:
    print ('Год високосный')


#4 Напишите программу, которая сформирует следующую строку: '54321'

lst = [i for i in range(5, 0, -1)]
print(lst)
end = len(lst)
str1 = ''
for i in range(end):
    str1 += str(lst[i])

print(str1)


#5 Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6]
#Поменяйте местами пары элементов этого списка: [2, 1, 4, 3, 6, 5]

lst = [i for i in range(1,7)]
print (lst)
lst1 = [i for i in lst[::2]]
lst2 = [i for i in lst[1::2]]
print(lst1)
print(lst2)

lst3 = []
for i, j in zip(lst1, lst2):
    lst3.append(j)
    lst3.append(i)

print(lst3)
