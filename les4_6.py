#1Дан список с числами. Оставьте в нем только те числа, которые содержат цифру ноль.

lst1 = [10, 9, 4, 509, 3092, 200]
print (lst1)
lst2 = []
for i in lst1:
    str1 = str(i)
    end_str1 = len(str1)
    for j in range(end_str1):
        print (str1[j], i)
        if str1[j] == '0':       
            lst2.append(i)
            break

print(lst2)    

#2 Дана следующая структура:
#Найдите сумму элементов этой структуры.


lst1 = [
	{
		1: 11,
		2: 12,
		3: 13
	},
	{
		1: 21,
		2: 22,
		3: 23
	},
	{
		1: 24,
		2: 25,
		3: 26
	}
]

end_lst1 = len(lst1)
s = 0
for i in range(end_lst1):
    print(i, lst1[i])
    for j in lst1[i].values():
        print(j)
        s += j
    
print (s)