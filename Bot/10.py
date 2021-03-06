def change(s):
    s = list(filter(None, s)) # удаление пустого из строки таблицы
    for i in range(len(s)):
        # Преобразование по примеру (Поменять имя фамилию местами)
        if ' ' in s[i]:
            s[0] = s[i][s[i].rindex(' ')+1:] + ' ' + s[i][:s[i].index(' ')]
        # Разделение по символу '&' и преобразование по примеру (замена 0 и 1 на да-нет)
        if '&' in s[i]:
            s[1] = s[i][:s[i].index('&')]
            if '1' == s[1]:
                s[1] = 'Y'
            elif '0' == s[1]:
                s[1] = 'N'
        # Преобразование по примеру (удаление цифр до '-', разделение оставшихся '-')
        if '-' in s[i]:
            s[2] = s[i][s[i].index('-')+1: s[i].rindex('-')] + '-' + s[i][s[i].rindex('-')+1:12] + '-' + s[i][12:]
    return s


def main(s):
    for i in range(len(s)):
        s[i] = change(s[i])
    return s

print(main([['Тимофей Мокувяк', None, 'Тимофей Мокувяк', '0&039-092-8841'], ['Ильдар Фицич', None, 'Ильдар Фицич',  '1&850-573-5628'],
            ['Артемий Вабодян', None, 'Артемий Вабодян', '0&706-696-2986']]))