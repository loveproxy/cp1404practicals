#a
for i in range(0, 110, 10):
    print(i, end=' ')
print()
#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()
#c
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

#d
for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()
print()

