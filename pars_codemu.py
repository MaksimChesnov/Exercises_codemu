import pip._vendor.requests as req

url = 'https://code.mu/ru/python/tasker/stager/'
level = '2'
task = '4'
delim = '/'

url_full = url+level+delim+task+delim

print (url_full)

req1 = req.get(url_full)
txt = req1.text
print (req1.status_code)
print (txt)

#Не отдает ничего. Ошибка 403 - доступ запрещен