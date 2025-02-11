#1 Попросите пользователя ввести целое число через консоль. Получите факториал введенного числа.
import math

num = int(input('Введите целое число:'))
fact = math.factorial(num)
print(f'Факториал числа {num}=', fact)

#2 Напишите программу, которая сформирует следующую строку: '-1-2-3-4-5-'

lst = [i for i in range(1,6)]
print (lst)
str1 = '-'
for i in range(len(lst)):
    str1 += str(lst[i]) + '-'

print (str1)

#3 Дана некоторая строка: '1 22 333 4444 22 5555 1'
#Удалите из этой строки все подстроки, в которых количество символов больше трех. 
#В нашем случае должно получится следующее: '1 22 333 22 1'

str1 = '1 22 333 4444 22 5555 1'
print(str1)
lst = str1.split()
print(lst)
end = len(lst)
lst2 = []
for i in range(end):
    print(i, lst[i])
    end2 = len(lst[i])
    for j in range(end2):
        print(j, lst[i][j])
        if j <= 2:
            lst2.append(lst[i])

print(lst2)



print (lst)




