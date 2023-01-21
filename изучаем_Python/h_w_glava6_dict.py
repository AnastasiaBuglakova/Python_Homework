alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
print('yes, baby') if alien_0['color']!='green'  else print('no no')
alien_0['mood'] = 'furious'
print(alien_0)
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'pink'
alien_1['poins'] = 33
print(alien_1)
alien_1['color'] = 'yellow'
print(alien_1)
alien_0['speed'] = 'medium'
print(alien_0)
if alien_0['speed'] == 'slow': x_increment = 1
elif alien_0['speed'] == 'medium': x_increment = 2
else:  x_increment = 3
alien_0['x_pos'] += x_increment
print(f"New position: {alien_0['x_pos']}")
del alien_0['mood']
print(alien_0)
print(alien_0.get('mood', 'you have a problem'))
print(alien_0.get('mood'))
glossary={
    'pop()': 'удаляет значение из списка и сохраняет его',
    'del --': 'удаляет элемент без сохранения',
    'strip': 'отсекает пробелы и вводы слева и справа',
    'lstrip': 'отсекает пробелы и вводы слева',
    'rstrip': 'отсекает пробелы и вводы справа',
    'name.lower()':'строку в нижний регистр',
    'name.upper()':'строку в верхний регистр',
    'name.title()': 'все слова строки с большой буквы',
    '/n': 'enter str',
    '/t': 'tab',
    'max()': '',
    'min()': "",
    'sum()': '',
    'name.insert(0, "dukati")': 'insert in position',
    'name.remove("value")': 'delete in value',
    'name.append("sms")': 'добавить значение в конец списка',
    'guests.sort(reverse=True)': "сортировка с изменением списка",
    'sorted(name,reverse=True)': "сортировка без изменения списка",
    '"".join(res)': 'объединяет список в строку',
    'reversed()': 'Переворот строки (реверс строки)',
    'list.reverse()':'Переворот списка в обратном порядке',
    '[value**8 for value in range(0,21)]':'Генерация списка чисел циклом в одну строку',
    'range(start,stop,step)':'Создание списка чисел',
    'num == 2 if True else False':'Тернарный оператор',
    'my_foods[-5:2]':'Срез строки от конца до второго элемента',
    'dict.items()':'Позволяет получить пары "ключ-значение" словаря',
    'str.replace('x','y', кол-во вхождений)':'Позволяет получить пары "ключ-значение" словаря',
    'str.endswith().,':''
    'str.startswith().,':''
    'split()': 'разделяет строку на список подстрок по разделителю или он по умолчанию 0 str.split(sep=None, maxsplit=-1)',
    'join()': 'объединение списка строк с помощью определенного указателя ",".join(vowels)',
    'letters = string.ascii_lowercase + "±!@£$%^&*()_+}{|:?><~`,./\;][=-§"': 'делаем строку символов для случайного выбора символов ниже',
    'random.randint(0, 10)':'создать случайное число'
    "res = ''.join((random.choice(letters)))": 'генерим случайный символ'
    'res1 = ''.join((random.sample(letters, 2)))': 'генерим случайные сроки без повторов в формате списка',
    'my_str.isdigit()': 'возвращает True, если все символы в строке str являются цифрами и есть хотя бы один символ (строка является не пустой и не состоит из пробелов), в противном случае False'
    'str.istitle()': 'возвращает True, если каждое слово в строке str начинается с заглавной буквы и в ней есть хотя бы один символ в верхнем регистре. Возвращает False в противном случае'
for k,v in glossary.items():
    if len(k) < 10: print(f'{k}: \t\t\t{v}')
    elif len(k) > 24: print(f'{k}: \t{v}')
    elif len(k) >= 10 and len(k) <= 24: print(f'{k}: \t\t{v}')
    else: print(f'{k}: {v}')