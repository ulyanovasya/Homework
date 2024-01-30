"""
Я ПОВЕЛИТЕЛЬ ИЗВРАЩЁННОГО КОДА

Дан словарь email-адресов студентов, в качестве ключа используется домен, а в качестве значения список имен.
Необходимо вывести все email-адреса в формате Имя@домен.
"""
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
mgu = emails['mgu.edu']
for i in range(len(mgu)):
    mgu[i] = mgu[i] + "@" + "mgu.edu"
gmail = emails['gmail.com']
har = emails['harvard.edu']
ya = emails['yandex.ru']
mail = emails['mail.ru']
for i in range(len(gmail)):
    gmail[i] = gmail[i] + "@" + "gmail.com"
for i in range(len(ya)):
    ya[i] = ya[i] + "@" + "yandex.ru"
for i in range(len(har)):
    har[i] = har[i] + "@" + "harvard.edu"
for i in range(len(mail)):
    mail[i] = mail[i] + "@" + "mail.ru"
print(gmail)
print(ya)
print(har)
print(mail)
