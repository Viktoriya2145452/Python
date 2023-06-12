'''Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод: Парам пам-пам'''

'''def ritm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_word = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_word += 1
        list_1.append(sum_word)
    return len(list_1) == list_1.count(list_1[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if ritm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')'''


def ritm(string):
    string = string.lower().split()
    result = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    r = result(string[0])
    if all([result(i) == r for i in string]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(ritm("пара-ра-рам рам-пам-папам па-ра-па-дам"))

'''
text = input().lower().split()
result = set()
vowels = 'ёуеыаоэяию'
for word in text:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    result.add(count)
if len(result) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
    '''
'''
text = input().lower().split()
result = set()
vowels = 'ёуеыаоэяию'
for word in text:
    count = [int(char in vowels) for char in word]
    result.add(sum(count))
if len(result) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")

'''