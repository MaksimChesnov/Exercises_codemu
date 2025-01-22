#1 Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.

lst1 = [0, 1, -9, -785, 100, 500, -1, -234]
cnt = 0
for i in lst1:
    if i < 0:
        cnt += 1

print (f'В списке {lst1} количество отрицательных чисел=', cnt)

#2 Дан список с числами. Оставьте в нем только положительные числа.
lst2 = []
for i in lst1:
    if i < 0:
        continue
    else:
        lst2.append(i)

print (f'В списке {lst1} только положит числа=', lst2)

#3 Дана строка. Удалите предпоследний символ из этой строки.
str1 = 'In simple words, we can say that number..R.'
print (str1)

str2 = str1.replace('R', '')
print (str2)

str2 = str1.replace(str1[-2:-1:], '')
print (str2)

#4 Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.
lst_str = ['fuckyou.html', 'pidavilli.com', 'chmo.html']
lst_str2 = []
for i in lst_str:
    if '.html' in i:
        lst_str2.append(i)

print (lst_str2)        


#5 Дан список с дробями: [1.456, 2.125, 3.32, 4.1, 5.34]. Округлите эти дроби до одного знака в дробной части.

lst_drob = [1.456, 2.125, 3.32, 4.1, 5.34]
lst_round = [round(i,1) for i in lst_drob]
print (lst_round)

#6 Дан словарь. Получите список его значений: [1, 2, 3, 4]

dict1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4
}

lst1 = []
for i in dict1.values():
    lst1.append (i)

print (lst1)