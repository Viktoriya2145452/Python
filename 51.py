# a(append) - добавление информации
# w(запись) - добавление информации(с учетом удаления всех старых записей)
# r(считать) - прочтение данных


database = open('data.txt', 'a', encoding='utf-8')
database.write('Ivan;Ivanov;+79991112233\n')
database.close()


with open('data.txt', 'w', encoding='utf-8') as database:
    database.write('Petr;Sidorov;+79042536932\n')

database = open('data.txt', 'a', encoding='utf-8')
database.write('Ivan;Ivanov;+79991112233\n')
database.close()


database = open('data.txt', 'a', encoding='utf-8')
database.write('Ivan;Ivanov;+79991112233\n')
database.close()


database = open('data.txt', 'a', encoding='utf-8')
database.write('Ivan;Ivanov;+79991112233\n')
database.close()

with open('data.txt', 'r', encoding='utf-8') as database:
    print(database.readlines())