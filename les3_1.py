
#1 С помощью включения создайте следующий список: [1, 2, 3, 4, 5, 6]

lst1 = [i for i in range(1,7)]
print(lst1)

#2 Даны два списка. Объедините эти списки в один: [1, 2, 3, 4, 5, 6]

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = lst1 + lst2
print(lst3)

#3 Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6]
#Найдите сумму первой половины элементов этого списка.

lst1 = [1, 2, 3, 4, 5, 6]
len1 = int(len(lst1) / 2)
print(len1)
sum1 = 0
for i in range(1,len1+1): 
    sum1 = sum1 + i

print(f'Сумма половины списка {lst1}=', sum1)