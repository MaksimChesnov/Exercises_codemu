#1 Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.

import pip._vendor.requests as req
#import re

res = req.get('https://rus.hitmotop.com')
print (res.status_code)
site_txt = res.text
find_txt = 'https://'
find_txt2 = '.mp3'

txt3 = site_txt.find(find_txt)
print (f'Количество ссылок {find_txt} =', txt3)

spl_site_txt = site_txt.split()
lst_str2 = []
for i in spl_site_txt:
    if find_txt2 in i:
        lst_str2.append(i)

print (lst_str2)      


#2 Дана некоторая строка. Найдите позицию первого нуля в строке.

str1 = 'Wel0come 012304569084'
print ('Индекс первого вхождения цифры 0 = str1[', str1.find('0'), ']')

#3 Дан список. Удалите из него элементы с заданным значением.

lst1 = ['борода', 'muqi', 'sell', 6, 986, 345, 'meditation']
lst1.remove('muqi')
print (lst1)


#4 Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.

for i in range(10,101): 
    str2 = str(i)
    s = int(str2[0])+int(str2[1])
    if s == 5:
        print (i)

#5 Дана некоторая строка: 'abcdeabc'. Очистите ее от дублей символов: 'abcde'

str3 = 'abcdeabc'
lst2 = []
for s in str3:
    if s in lst2:
        continue
    else:
        lst2.append(s)

print (f'Строка {str3} без дублей = ', lst2)