f = open('input', 'w')
n = 3
for i in range(n):
    for j in range(n):
        print(1 / (3 + i + j), end=" ", file=f)
    print(file=f)