# for (int i = 0; i <= 10; i++)

for i in 1, True, "Hello", 4.57:
    print(i)

# range()
print(list(range(5)))
for i in [0, 1, 2, 3, 4]:
    print(i)

begin = 10
end = 0
step = -1
print(list(range(begin, end, step)))
print(list(range(5))) # begin = 0           step = +1
print(list(range(10, 20)))