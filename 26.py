'''Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()'''

input_str = "a a a b c a a d c d d".split()
letters = {}
for i in input_str:
    if i in letters.keys():
        print(i + "_" + str(letters[i]), end = " ")
        letters[i] += 1
    else:
        print (i, end = " ")
        letters[i] = 1

