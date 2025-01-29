
#1 Дан список с числами. Удалите из него числа, состоящие более чем из трех цифр.

lst1 = [1, 345, 67383, 9383, 23, 45, 763]
lst2 = []
print(lst1)
for i in lst1:
    len_lst1 = len(str(i))
    #print (len_lst1)
    if  len_lst1 <= 3:
        lst2.append(i)

print(lst2)

#2 Дана строка. Проверьте, что эта строка состоит только из цифр.

str1 = '12345'
bool1 = True
for i in str1:
    if not str1.isdigit():
        bool1 = False
        break

if bool1 == True:
    print(f'Строка {str1} содержит только цифры')
else:
    print(f'Строка {str1} содержит не только цифры')


#3 Дано число, например, вот такое. Проверьте, что все цифры этого числа больше нуля.

num = 123405;
str_num = str(num)
bl = True
for i in str_num:
    if not int(i):
        bl = False
        break

if bl:
    print(f'Все цифры числа {num} больше 0')
else:
    print(f'Не все цифры числа {num} больше 0')


#4 Даны два списка. Проверьте, что все элементы первого списка есть во втором.

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3]

st = set(lst1) & set(lst2)
print(f'Цифры списка {lst1} пересекаются с цифрами списка {lst2}=', st)