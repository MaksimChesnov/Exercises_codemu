#1Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.
str1 = 'hdfj890333kkk'
for i in str1:
    if i.isdigit() == True:
        ind = str1.index(i)
        break

print (f'Позиция первой цифры строки {str1}=', ind)

#2Дано число. Выведите в консоль количество четных цифр в этом числе.

num1 = 478632986
cnt_chtn = 0
for i in str(num1):
    ostatok = int(i) % 2
    if ostatok == 0:
        cnt_chtn = cnt_chtn + 1
        
print (f'Количество четных цифр в числе {num1} = ', cnt_chtn)

#3Дан словарь. Получите список его ключей: ['a', 'b', 'c', 'd']

dict1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}

lst1 = [i for i in dict1.keys()]
print(f'Список ключей словаря {dict1}=', lst1)

#4Дана некоторая строка:'abcde' Переведите в верхний регистр все нечетные буквы этой строки. 
#В нашем случае должно получится следующее: 'AbCdE'

str1 = 'abcde'
str2 = []
for i in str1:
    ind = int(str1.index(i)) + 1
    ostatok = ind % 2
    print(i, ind, ostatok)
    if ostatok != 0:
        str2.append(i.upper())
    else:
        str2.append(i)
        
print(f'Если перевести в верхний регистр все нечетные буквы строки {str1}, то результат будет = ', str2)



#5Дана некоторая строка со словами: 'aaa bbb ccc' Сделайте заглавным первый символ каждого слова в этой строке. 
#В нашем случае должно получится следующее: 'Aaa Bbb Ccc'

str_abc = 'aaa bbb ccc'
str_ABC = str_abc.title()
print(f'Сделайте заглавным первый символ каждого слова в строке {str_abc}=', str_ABC)

#6 Дана дата в следующем формате: '2025-12-31' Преобразуйте эту дату в следующий кортеж:('31', '12', '2025')

str_date = '2025-12-31'
str_date1 = str_date.split('-')
tup = tuple(str_date1)
print('Кортеж=', tup)