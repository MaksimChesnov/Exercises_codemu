#Уровень 2.5 задачника Python
#1 Дана некоторая строка, например, вот такая: '023m0df0dfg0' Получите сет позиций всех нулей в этой в строке.

str1 = '023m0df0dfg0'
end = len(str1)
lst = []
for i in range(0, end):
    #print (i, str1[i])
    if str1[i].isdigit() == True:
        z = int(str1[i])
        #print ('z=', z)
        if z == 0:
            lst.append(i)
        else:
            continue

print(f'Индексы нулей в строке {str1}=', lst)

#2 Дана некоторая строка: 'abcdefg' Удалите из этой строки каждый третий символ. В нашем случае должно получится следующее: 'abdeg'

str2 = 'abcdefghk'
end2 = len(str2)
print (end2)
lst2 = []
for i in range(0, end2):
    print (str2[i], i, str2[2::3])
    if str2[i] in str2[2::3]:
        continue
    else:
        lst2.append(str2[i])

print(f'{str2}', lst2)



#3Дан некоторый список, например, вот такой:[1, 2, 3, 4, 5, 6]
#Поделите сумму элементов, стоящих на четных позициях, на сумму элементов, стоящих на нечетных позициях.

lst3 = [1, 2, 3, 4, 5, 6]

s_chet = 0
s_nechet = 0
for i in lst3:
    ostatok = i % 2
    if ostatok == 0:
        s_chet += i
    else:
        s_nechet += i

print (f'{s_chet}/{s_nechet}=', s_chet/s_nechet)

#4Дана дата в следующем формате: ['2025', '12', '31'] Преобразуйте эту дату в следующий кортеж: ('31', '12', '2025')

lst_date4 = ['2025', '12', '31']
tup4 = tuple(lst_date4[::-1])
print(tup4)