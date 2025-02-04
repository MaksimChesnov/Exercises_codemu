import re

#1 Сформируйте с помощью циклов следующий список:
'''
[
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
'''
#Не осилил пока. Задача хорошая.

lst1 = [[i for i in range(1,4)] for j in range(1,4)]
print(lst1)

end = len(lst1)

for i in range(end):
	print (i, lst1[i])
	if i > 0:
		for j in lst1[i]:
			print(j+3)

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

lst = txt.split()
end = len(lst)
keys = []
val = []
for i in range(end):
	#print (i, lst[i])
	end2 = len(lst[i])
	for j in range(end2):
		#print(j, lst[i][j])
		if lst[i][j].isdigit():
			val.append(lst[i][j])
		elif lst[i][j].isalpha():
			keys.append(lst[i][j])

dct = dict(zip(keys, val))
print(keys, val)
print (dct)


