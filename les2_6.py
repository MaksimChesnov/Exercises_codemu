#1 Дана некоторая строка с буквами и цифрами. Получите список позиций всех цифр из этой строки.

str1 = 'Create and test 8933 a Python package on multiple Python versions.'
lst1 = []
end = len(str1)
for i in range(end):
    if str1[i].isdigit() == True:
        lst1.append(i+1)

print(f'Позиции цифр в строке {str1}=', lst1)
         

#2 Дана некоторая строка: 'AbCdE' Смените регистр букв этой строки на противоположный. 
#В нашем случае должно получится следующее: 'aBcDe'

str2 = 'AbCdEiao'
lst2 = []
end2 = len(str2)
for i in range(end2):
    if str2[i].isupper() == True:
        lst2.append(str2[i].lower())
    else:
        lst2.append(str2[i].upper())

print(f'Поменять регистр букв строки {str2} на противоположный =', lst2)


#3 Дан некоторый список с числами, например, вот такой: [1, 2, 3, 4, 5, 6] Слейте пары элементов вместе:[12, 34, 56]

num1 = [1, 2, 3, 4, 5, 6]
end3 = len(num1)
new_num1 = []
for i in range(0, end3, 2):
    new_num1.append(str(num1[i])+str(num1[i+1]))

print (f'Если слить пары элементов списка {num1}=', new_num1)

#4 Дана некоторая строка со словами: 'aaa bbb ccc eee fff'
#Сделайте заглавным первый символ каждого второго слова в этой строке. В нашем случае должно получится следующее:
#'aaa Bbb ccc Eee fff'

#Не получается
str4 = 'aaa bbb ccc eee fff'
end4 = len(str4)
str4_1 = []
cnt4 = 1
for i in range(4, end4, 4):
    ost = cnt4 % 2
    print (str4[i], i, cnt4, ost)  
    if ost:
        str4_1 = str4.upper()
    cnt4 += 1

print (f'Если сделать заглавным первый символ каждого второго слова строки {str4}=', str4_1)

