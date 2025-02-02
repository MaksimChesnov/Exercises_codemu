#1Дан список. Удалите из него каждый пятый элемент.

lst1 = ['biba', 'soya', 'slim', 1, 4, 6, 9, 24, 'fz', 5, 33, 'fhdj', 'bo', 'de', 'mm', '09hg']
print (lst1)
end = len(lst1)
print(end)
lst2 = []
for i in lst1[4:end:5]:
    #print (i)
    lst2.append(i)
    lst1.remove(i)
    
print(lst2)
print(lst1)    


#2Даны два числа. Получите список общих делителей этих чисел.

#Кривая формулировка. Непонятно что нужно делать


#3Даны два числа
#Получите кортеж цифр, которые есть и в одном, и в другом числе (4, 5)

txt1 = 12345
txt2 = 45678

st = set(str(txt1))&set(str(txt2))
print (st)

tup = tuple(st)
print (tup)

#4Дан список.
#Найдите сумму элементов этого списка.

lst1 = [
	[
		[11, 12, 13],
		[14, 15, 16],
		[17, 17, 19]
	],
	[
		[21, 22, 23],
		[24, 25, 26],
		[27, 27, 29]
	],
	[
		[31, 32, 33],
		[34, 35, 36],
		[37, 37, 39]
	]
]
print (f'Список {lst1}')
end_lst1 = len(lst1)
print (end)
s = 0
for i in lst1[0:end]:
    end_i = len(i)
    print (end_i, f'i=',i)
    for j in i[0:end_i]:
        end_j = len(j)
        print (end_j, f'j=', j)
        for k in j[0:end_j]:
            print (f'k=', k)
            s += k
            
print(s)
            