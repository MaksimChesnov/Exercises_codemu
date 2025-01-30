#1 Дан список с числами. Удалите из него числа, имеющие два и более нуля.

lst1 = [9, 3, 7, 8, 90, 500, 820008]
print(lst1)
lst2 = []
for i in lst1:
    bl = False
    z_cnt = 0
    #print(i)
    for j in str(i):
        #print (j)
        if j == '0':
            z_cnt += 1
            if z_cnt >= 2: 
                lst2.append(i)
                break
    
print (lst2)

for i in lst2:
    lst1.remove(i)
    
print (lst1)


#2 Найдите все числа от 1 до 1000, сумма цифр которых равна 13. Результат запишите в сет.

#for i in range(1001):
    

#3 Дан список: [1, 2, 3] 
#Сделайте так, чтобы в нем каждый элемент повторился два раза: [1, 1, 2, 2, 3, 3]

lst1 = [1, 2, 3]
print (lst1)
lst2 = lst1.copy()
print (lst2)
lst3 = []
for i, j in zip(lst1, lst2):
    lst3.append(i)
    lst3.append(j)

print(lst3)

#4 Даны два списка.
#Переберите эти списки одним циклом и в каждой итерации выводите их элементы следующим образом:
#'1,4' '2,5' '3,6'

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

for i, j in zip(lst1, lst2):
    print (i, j)