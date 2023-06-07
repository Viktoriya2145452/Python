'''Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
второй вариант'''

data_ = [i for i in input ("Введите символы: ").split()]
print (data_)
data_2 = set (data_)
for i in data_2:
    count = 0
    for j in range (len(data_)):
        if i == data_[j]:
            if count > 0:
                data_[j] = f"{data_[j]}_{count}"
            count += 1
print (*data_)
       