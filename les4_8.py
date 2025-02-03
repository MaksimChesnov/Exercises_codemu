
import re

#1 Сформируйте с помощью циклов следующий список:
'''
[
	['x', 'x', 'x'],
	['x', 'x', 'x'],
	['x', 'x', 'x'],
]
'''

lst1 = []
for i in range(3):
    lst2 = []
    lst1.append('x')
    for j in range(3):       
        lst2.append(lst1)

print(lst2)

nested_list = [['x' for j in range(3)] for i in range(3)]        
print(nested_list)

#2 Сформируйте с помощью циклов следующий список:

'''
[
	[1, 2, 3],
	[1, 2, 3],
	[1, 2, 3],
	[1, 2, 3],
	[1, 2, 3]
]
'''
lst1 = []
for i in range(1,4):
    lst2 = []
    lst1.append(i)
    for j in range(5):
        lst2.append(lst1)

print(lst2)

inn_lst = [i for i in range(1,4)]
nested_lst = [inn_lst for i in range(5)]
print(inn_lst)
print (nested_lst)

nested_lst = [[i for i in range(1,4)] for j in range(5)]
print (nested_lst)

#3 Дана строка.
#Удалите из нее все пустые строки, находящиеся не в начале и не в конце текста:
'''
	text1
	text2
	text3
	text4
	text5
'''

str1 = '''
	text1
	text2
	
	text3
	text4
	
	text5
'''
print(str1)

#Разделяем строку по делиметрам - табуляция, перевод строки 
lst1 = re.split("\t|\n", str1)
print (lst1)

#Убираем из полученного списка все пустые строки.Добавляем перед каждым значение табуляцию
lst1 = ['\t'+i for i in lst1 if i]

#Соединяем то, что получилось
str1 = '\n'.join(lst1)
print(str1)


