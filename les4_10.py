#1 Дан список
#Слейте элементы этого списка в один одномерный список:
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

lst1 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print (lst1)
end = len(lst1)
lst2 = []
for i in range(end):
    #print(i, lst1[i])
    lst2 += lst1[i]

print (lst2)


#2 Дан список.
#Отсортируйте элементы в каждом подсписке.

lst1 = [
	[2, 1, 4, 3, 5],
	[3, 5, 2, 4, 1],
	[4, 3, 1, 5, 2]
]
print (lst1)
end = len(lst1)
for i in range(end):
    lst1[i].sort()
    
print (lst1)
