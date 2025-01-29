import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def checkIP():
    ip = req.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    print(soup.find('body').text)

checkIP()

url = 'https://code.mu/ru/python/tasker/stager/'
level = input('Уровень задачи: ')
task = input('Номер задачи: ')
#qua_task = input('Сколько задач создать? ')
delim = '/'

url_full = url+level+delim+task+delim
print (url_full)

#Не отдает ничего. Ошибка 403 - доступ запрещен
#req1 = req.get(url_full)
#print (req1.status_code)


#Причина - заголовок. В нем прописано, что подключаемся через Python-requests
#for key, value in req1.request.headers.items():
    #print (key+':'+value)

#Зайдем с адекватным заголовоком (header)
req1 = req.get(url_full, headers = {'User-Agent': UserAgent().chrome})
print (req1.status_code, ',', UserAgent().chrome)

html = req1.content
soup = BeautifulSoup(html, 'html.parser')
#print (soup)

#print(soup.html.head.title)
#print(soup.html.head.title.text)

#for i in range(task, qua_task):

file_name = (f'les{level}_{task}.py')
path = '/home/user/Projects/Exercices/'
file = open(path+file_name, 'w')
file.write(soup.html.body.text)
file.close()

#Можно докрутить так, чтобы можно было задать, например, скачай 5 задач. Программа скачивает и создает 5 файлов
#При этом, она лезет в путь, где лежат файлы. Считывает их названия. Анализирует. Берет самый большой и прибавляет 1.
#Можно функцию отдельную написать.

#Доступ заблокировали, 403
#Так даже интереснее.
#Надо найти еще справочник и сразу выкачать его весь. 



