def parse_subj(text):
    groups = []
    group_numbers = []
    variants = []
    part_of_text = []
    final_text = []
    #Название группы
    for element in text:
        if "py" in element or "u" in element:
            groups.append("")
            continue
        added = False
        for i in range(len(element)):
            if element[i] == "n" or element[i] == "N" or element[i] == "н" or element[i] == "Н":
                groups.append("ИНБО-")
                added = True
                break
            elif element[i] == "v" or element[i] == "V" or element[i] == "в" or element[i] == "В":
                groups.append("ИВБО-")
                added = True
                break
            elif element[i] == "k" or element[i] == "K" or element[i] == "к" or element[i] == "К":
                groups.append("ИКБО-")
                added = True
                break
        if not added:
            groups.append("")
    #Номер группы
    for element in text:
        for i in range(1, len(element)):
            group_number = ''
            index = 0
            if element[i - 1].isdigit():
                group_number += element[i - 1]
                index = i - 1
                if element[i].isdigit():
                    group_number += element[i]
                    index = i
                break
        part_of_text.append(element[(index + 1):])
        group_numbers.append(group_number)
    #Номер варианта
    for element in part_of_text:
        variant = ''
        for i in range(len(element)):
            if element[i].isdigit():
                variant += element[i]
        variants.append(variant)

    for i in range(len(groups)):
        final_text_element = ''
        if groups[i] == "":
            final_text.append("Мусор!")
        elif group_numbers[i] == "":
            final_text.append("Мусор!")
        elif variants[i] == "":
            final_text_element += groups[i] + group_numbers[i] + '-19, нет варианта'
        else:
            final_text_element += groups[i] + group_numbers[i] + '-19, вариант: ' + variants[i]
        final_text.append(final_text_element)
    final_text_copy = final_text
    final_text = []
    #Удаление пустот
    for i in range(len(final_text_copy)):
        if final_text_copy[i] != "":
            final_text.append(final_text_copy[i])
    return final_text


bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py', 'В 11 4',
            '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23',
            '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013',
            'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10', 'ПитонН4 н11', 'K13 28', 'К4',
            'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']
print(parse_subj(bad_subj))
