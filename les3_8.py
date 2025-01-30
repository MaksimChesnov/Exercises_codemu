#1 Дан список со числами. Проверьте, что все числа из этого списка содержат в себе цифру 3.

lst1 = [3, 33, 331, 132]
for i in lst1:
    bl = False
    for j in str(i):       
        if j == '3':
            bl = True
            break

print (f'Все числа списка {lst1} содержат цифру 3 =', bl)

#2 Через запятую написаны числа. Получите максимальное из этих чисел.

tp = 1, 2, 3, 8
print (f'Максимальное число кортежа {tp}=', max(tp))

#3 Дана строка в формате: 'kebab-case'. Преобразуйте ее в формат:'snake_case'

str1 = 'kebab-case'
print(str1)
str1 = str1.replace('kebab-', 'snake_')
print(str1)

#4 Дана строка в формате: 'snake_case'. Преобразуйте ее в формат: 'camelCase'

str1 = 'snake_case'
str1 = str1.replace('snake_', 'camel')
str1 = str1.replace('case', 'Case')

print(str1)

#5 Дана строка в формате: 'camelCase'. Преобразуйте ее в формат: 'snake_case'

str1 = 'camelCase'
str1 = str1.replace('camel', 'snake_')
str1 = str1.replace('Case', 'case')

print(str1)