
#Уровень 2.10 задачника Python
 
#1 Дана строка с буквами и цифрами. Проверьте, что в этой строке не более трех букв.
	
str1 = '123abсв456'
lst1 = []
for i in str1:
    if i.isalpha():
        lst1.append (i)

if len(lst1) >= 3:
    print (f'В строке {str1} количество букв больше или равно 3=', len(lst1))
else:
    print(f'В строке {str1} меньше 3 букв=', len(lst1))


#2 Дано число. Получите первую четную цифру с конца этого числа.

num1 = 1234567
num1_str = str(num1)

for i in num1_str[::-1]:
    ost = int(i) % 2
    if ost == 0:
        print(f'Первая четная цифра с конца числа {num1}=', int(i))
        break
	

#3 Дана некоторая строка: 'abcde abcde abcde'
#Замените в ней первый символ каждого слова на '!': '!bcde !bcde !bcde'

str1 = 'abcde abcde abcde'

str2 = str1.replace('a', '!')
print(str2)


#4 Дан список со строками, содержащими целые числа: ['1', '2', '3', '4', '5']
#Найдите сумму элементов этого списка.

lst_str = ['1', '2', '3', '4', '5']
end = len(lst_str)
num = 0
for i in range(end):
    num = num + int(lst_str[i])
    
print(num)
	