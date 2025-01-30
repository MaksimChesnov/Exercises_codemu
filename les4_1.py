#1 Дано некоторое число. Проверьте, что цифры этого числа расположены по возрастанию.

num = 456789
print (num)
str_num = str(num)
end = len(str_num)
bl = True

print (bl)  

#2 Дан список: [1, '', 2, 3, '', 5]
#Удалите из списка все пустые строки.

lst1 = [1, '', 2, 3, '', 5]
print (lst1)
lst2 = []
for i in range(len(lst1)):
    if lst1[i] == '':
        continue
    else:
        lst2.append(lst1[i])
        
print (f'Если убрать из списка {lst1} пустые строки=', lst2)

#3 Дан список
#Выведите в консоль все элементы этого списка.

lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(lst1)):
    print(lst1[i], end= ' ')
    
print ('\n')