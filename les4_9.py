import re

#1 Сформируйте с помощью циклов следующий список:
'''
[
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
'''

lst1 = []
for i in range(1,4):
    lst2 = []
    lst1.append(i)
    for j in range(1,4):
        lst2.append(lst1)
        
print(lst2)

lst1 = [[i for i in range(1,4)] for j in range(1,4)]
print(lst1)

#2 Дан текст
#Разбейте эту строку в словарь следующим образом
'''
{
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}
'''


txt = '''
	a-1
	b-2
	c-3
	d-4
	e-5
'''
print(txt)

lst = re.split("\n|\t|'-'", txt)
lst = [i.replace('-', ':') for i in lst if i]
print(lst)


