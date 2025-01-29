#Уровень 3.4 задачника Python

#1 Дана строка. Удалите из нее все гласные буквы.

str1 = 'Create and test a Python package on multiple Python versions'
print(str1)

# Строка с гласными
str_glasn = 'aeiou'
for i in str1:
    if i in str_glasn:
        str1 = str1.replace(i, '')

print (str1)

#2 Даны два сета. Получите сет их общих элементов: {4, 5}

st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}

st3 = st1 & st2
print(st3)

#3 Даны два сета. Получите сет элементов, входящих только в один из сетов: {1, 2, 3, 6, 7, 8}

st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}

st3 = st1 ^ st2
print(st3)