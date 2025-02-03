#1 Дан список с числами. Проверьте, что в нем есть число, содержащее в себе цифру 3.

lst1 = [1, 3, 435, 23, 45, 63, 33, 7733, 87, 986]
#lst1 = [1, 2, 45, 22, 45, 63, 24, 7766, 87, 986]

print (lst1)

str1 = [str(num) for num in lst1]
print(str1)
end = len(str1)
bl = False
for i in range(end): 
    if bl: 
         break
    end2 = len(str1[i]) + 1
    print (i, str1[i], end2)
    for j in range(end2):
        print ('j=', j)
        if str1[j] == '3':
            print ('!!', str1[j])
            bl = True
            break

if bl:            
    print(f'Список чисел {lst1} содержит цифру три')
else:
    print(f'Список чисел {lst1} не содержит цифру три')

#2 Дана следующая структура:
#Найдите сумму элементов этой структуры.
lst1 = [
    {
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3)
	},
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3)
	},
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3)
	}
]

end = len(lst1)
s = 0
for i in range(end):
    #print (i)
    for j in lst1[i].values():
        #print (j)
        for k in j:
            #print (k)
            s += k
        
print (s)


#3 Дан список:
#Сделайте из этого списка строку так, чтобы каждый элемент списка был на новой линии:

lst1 = [
	'text1',
	'text2',
	'text3',
	'text4',
	'text5'
]
print(lst1)

str1 = '\n'.join(lst1)
print(str1)


'''
	text1
	text2
	text3
	text4
	text5
'''
