from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Попробуйте ещё раз выбрать правильную команду')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')

    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second



def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        # ТУТ НАПИСАТЬ КОД
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        with open('data_first_variant.csv', "r", encoding="utf-8") as f:
            journal = f.read()
            line_journal = journal.split("\n")
            count_line_journal = len(line_journal)
            count_journal = (count_line_journal-1)//5

            num_journal = 1
            for i in range(count_line_journal-1):
                if (i%5 == 0):
                    print(f"Запись журнала {num_journal}:")
                    num_journal += 1
                print(line_journal[i])
        
            print(f"Какую строку из {count_journal} хотите изменить?")
            n = int(input('Введите номер строки: '))
            if n > 0 and n <= count_journal:
                y = int(input('Введите номер поля, которое хотите изменить: '))
                if y > 0 and y <= 4:
                    n_journal = int(input('Введите номер поля: '))
                    n_new = (n_journal-1)*5
                    index = n_new + y - 1
               
                    x = input(f"Введите информацию для поля {y} записи {n_journal}: ")
                    line_journal[index] = x
                    with open('data_first_variant.csv', "w", encoding='utf-8') as data:
                        data.write("\n".join(line_journal))   

   
def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
        with open('data_first_variant.csv', "r", encoding="utf-8") as f:
            journal = f.read()
            line_journal = journal.split("\n")
            count_line_journal = len(line_journal)
            count_journal = (count_line_journal-1)//5

            num_journal = 1
            for i in range(count_line_journal-1):
                if (i%5 == 0):
                    print(f"Запись журнала {num_journal}:")
                    num_journal += 1
                print(line_journal[i])
        
            print(f"Какую строку из {count_journal} Вы хотите удалить?")
            n = int(input('Введите номер строки: '))
            if n > 0:
                while n > count_journal:
                    print('Попробуй еще')
                    n = int(input('Введите номер записи: '))
            num = (n-1)*5
           
            del1 = line_journal.pop(num)
            del2 = line_journal.pop(num)
            del3 = line_journal.pop(num)
            del4 = line_journal.pop(num)
            line_journal.pop(num)
            with open('data_first_variant.csv', "w", encoding='utf-8') as data:
                data.write("\n".join(line_journal))
            print(f"Запись {n} была удалена со всем своим содержимым:")
            print(del1)
            print(del2)
            print(del3)
            print(del4)
    else:
        with open('data_second_variant.csv', "r", encoding="utf-8") as data:
            journal = data.read()
            print(journal)
        print("")
        line_journal = journal.split("\n")
        count_journal = len(line_journal)-1
        print(f"Какую именно запись из {count_journal} по порядку Вы хотите удалить?")
        n = int(input('Введите номер записи: '))