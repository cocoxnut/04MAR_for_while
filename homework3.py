name = input('Ваше имя: ')
age = input('Ваш возраст: ')
job = input('Место работы: ')
while name == '' or age == '' or job == '':
    if name == '':
        name = input('Ваше имя: ')
    if age == '':
        age = input('Ваш возраст: ')
    if job == '':
        job = input('Место работы: ')
    if name != '' and age != '' and job != '':
        break
