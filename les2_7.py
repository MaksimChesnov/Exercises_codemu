
#Уровень 2.7 задачника Python
 
#1 Дан символ. Узнайте, в каком регистре этот символ - в верхнем или нижнем.

char = 'K'
if char.isupper(): 
    print(f'Символ {char} в верхнем регистре')
else:
    print(f'Символ {char} в нижнем регистре')
	
#2 Дано некоторое число, например, такое: 123789 Удалите из этого числа все нечетные цифры.
#В нашем случае получится такой результат: 28

num = 123789
str_num = str(num)
lst = []
for i in str_num:
    ostatok = int(i) % 2
    #print (i, ostatok)
    if ostatok == 0:
        lst.append(int(i))

end = len(lst)
str_num2 = ''
for i in range(end):
    str_num2 = str_num2 + str(lst[i])

#str_num2 = "".join(lst)
num2 = int(str_num2)

print(num,'->', lst, '->', num2)

#3 Дан кортеж с датой: ('2025', '12', '31')
#Преобразуйте эту дату в следующий словарь:{'year' : '2025', 'month': '12', 'day'  : '31',}

tup = ('2025', '12', '31')
lst = ['year', 'month', 'day']
dict1 = dict(zip(lst,tup))
print (dict1)
