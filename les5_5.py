#1 Попросите пользователя ввести дату рождения в формате год-месяц-день. 
#Определите, сколько полных лет пользователю.

'''
from datetime import date

dat = input('Введите дату рождения в формате год-месяц-день:')
lst = dat.split('-')
lst = [int(i) for i in lst]
y, m, d = lst

print (lst, y, m, d)

birthdate = date(y, m, d)
today = date.today()

age_y = today.year - birthdate.year 
age_m = birthdate.month - today.month
age_d = birthdate.day - today.day 

print (today, birthdate)
print (f'Через {age_m} месяцев и {age_d} дней будет {age_y} лет')

'''
#2 Попросите пользователя ввести три числа. 
#Проверьте, что эти числа являются тройкой Пифагора: 
#квадрат самого большого числа должен быть равен сумме квадратов двух остальных.

#3 Дано некоторое число: 35142 Отсортируйте цифры этого числа. 
#В нашем случае должно получится следующее: 12345

num = 35142
str1 = str(num)
lst = [str1[i] for i in range(len(str1))]
lst.sort()
print(lst)
str2 = ''
for i in range(len(lst)):
    str2 += lst[i]

print (str2)

num = int(str2)

print (num)
