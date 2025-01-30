#1 Дана строка. Сделайте заглавной последнюю букву каждого слова в этой строке.

str1 = 'Python is language for programmers and snake too'
lst1 = str1.split(' ')
end = len(lst1)
print(lst1)
lst2 = [lst1[i][-1].upper() for i in range(end)]
for i in range(end):
    lst1[i] = lst1[i].replace (lst1[i][-1], '')
    lst1[i] += lst2[i]

print(lst1)


#2 Дана строка. Проверьте, что эта строка состоит только из четных цифр.

str1 = '248684267'
bl = True
for i in str1:
    ost = int(i)% 2
    #print(ost)
    if ost:
        bl = False
        break

if bl:
    print(f'Строка {str1} состоит только из четных цифр')
else:
    print(f'Строка {str1} состоит не только из четных цифр')

#3 Даны две строки. Получите символы, которые есть и в одной, и в другой строке: '45'

txt1 = '12345'
txt2 = '45678'

st = set(txt1) & set(txt2)
print(st)

#4 Дана некоторая строка: 'a bc def ghij'
#Переведите в верхний регистр все подстроки, в которых количество букв меньше или равно трем. 
#В нашем случае должно получится следующее: 'A BC DEF ghij'

str1 = 'a bc def ghij'
