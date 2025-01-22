#1Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.

wrd1 = 'this'
wrd2 = 'solid'

print (wrd1[-1], wrd2[0])

if wrd1[-1] == wrd2[0]:
    print (f'Последняя буква слова {wrd1} совпадает с первой буквой слова {wrd2}')

#2Дана некоторая строка. Найдите позицию третьего нуля в строке.

str1 = '6090gfds0llkj0j00'
cnt_all = 0
cnt_zero = 0
ind = 0
for i in str1:
    cnt_all = cnt_all + 1
    if i.isdigit() == True and int(i) == 0:
        cnt_zero = cnt_zero + 1
        if cnt_zero == 3:
            break

print (f'Количество символов в строке=',cnt_all)     
print (f'Третья цифра 0 в строке {str1}находится на позиции ', cnt_all-1, 'если считать позицию с 0, а не 1')

#3Даны числа, разделенные запятыми:'12,34,56' Найдите сумму этих чисел.

str2 = '12,34,56'
num = str2.split(',')

s = 0
for i in num: s = s + int(i)
print (f'Сумма чисел {num}=', s)


#4Дана дата в следующем формате: '2025-12-31'Преобразуйте эту дату в следующий словарь: dict1 = {'year':'2025','month':'12','day':'31'}
date = '2025-12-31'
lst_chisla = date.split('-')
lst_ymd = ['year', 'month', 'day']

print(lst_ymd, lst_chisla)

d = dict(zip(lst_ymd, lst_chisla))
print (f'Дата {date} преобразована в словарь ',d)


#5 Дан словарь. Получите сет его значений: {1, 2, 3, 4}

dict2 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
