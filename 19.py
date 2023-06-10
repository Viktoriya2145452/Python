'''Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально'''

data = [int(i) for i in input("Введите числа: ").split()]
steps = int(input("Введите кол-во сдвигов"))
steps = steps % len(data)
data = [data[i-steps] for i in range(len(data))]
print(data)

'''
n = int(input())
list_first = list()
list_result = list()
for i in range(n):
    list_first.append(int(input()))
print(*list_first)

k = int(input())
k = k%n
if k<0:
    k=-k
for i in range(k):
    list_result[i]=list_first[n - k + i]
for i in range(n - k):
    list_result[k+i] = list_first[i]
print(list_result)
    '''