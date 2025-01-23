import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

url = 'https://code.mu/ru/python/tasker/stager/'
level = '2'
task = '7'
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

print(soup.html.head.title)
print(soup.html.head.title.text)


file_name = (f'les{level}_{task}.py')
path = '/home/user/Projects/Exercices/'
file = open(path+file_name, 'w')
file.write(soup.html.body.text)
file.close()

#Можно докрутить так, чтобы можно было задать, например, скачай 5 задач. Программа скачивает и создает 5 файлов
#При этом, она лезет в путь, где лежат файлы. Считывает их названия. Анализирует. Берет самый большой и прибавляет 1.
#Можно функцию отдельную написать.


