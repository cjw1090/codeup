#1081
n, m = input().split()
for i in range(1, int(n)+1):
    for j in range(1, int(m)+1):
        print(i, j)

#1082
a = int(input(), 16)
for i in range(1, 16):
    print("%X*%X=%X" %(a,i,a*i))

#1084
r, g, b= map(int, input().split())
n = 0
for i in range(0, r):
    for j in range(0, g):
        for m in range(0, b):
            print(i,j,m)
            n += 1
print(n)

#1351
#1352
#1353
#1354
#1355
#1356
#1357
#1358
#1361
#1365
n = int(input())
for i in range(0, n):
    print('*', end='')
print()
for i in range(1, n-1):
    for j in range(0, n):
        if (j == 0) or (j == i) or (j == n-1) or (j == n-i-1):
            print('*', end='')
        else:
            print(' ', end='')
    print()

for i in range(0, n):
    print('*', end='')

#1366
#1368
j, k, d = input().split()
if d == 'L':
    for i in range(0, int(j)):
        for m in range(0, i):
            print(' ', end='')
        for m in range(0, int(k)):
            print('*', end='')
        print()
else:
    for i in range(int(j)-1, -1, -1):
        for m in range(0, i):
            print(' ', end='')
        for m in range(0, int(k)):
            print('*', end='')
        print()

#1369
n, k = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == 1) or (i == n) or (j == 1) or (j == n):
            print('*', end='')
        elif (i+j-1) % k == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#1370
#1371
#1378
#1380
#1382
for i in range(1, 10):
    for j in range(2, 6):
        print('%d x %d = %2d' % (j, i, j*i), end='')
        print('\t', end='')
    print()

#1677