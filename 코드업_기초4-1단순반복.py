#1071
n = input().split()
for i in n:
    if int(i) == 0:
        break
    print(i)

#1072
n = int(input())
m = input().split()
for i in range(n):
    print(m[i])

#1073
m = input().split()
for i in m:
    if int(i) == 0:
        break
    print(i)

#1074
#1075
#1076
m = ord(input())
a = ord('a')
while a <= m:
    print(chr(a), end=' ')
    a += 1

#1077
#1078
#1079
m = input().split()
for i in m:
    if i == 'q':
        print(i)
        break
    print(i)

#1080
m = int(input())
a = 1
sum_a = 0
while sum_a < m:
    sum_a += a
    a += 1
print(a-1)

#1083
m = int(input())
for i in range(m):
    if (i+1) % 3 == 0:
        print("X", end=' ')
    else:
        print(i+1, end=' ')

#1087
#1088
#1089
#1090
a, r, n = map(int, input().split())
for i in range(n-1):
    a = a * r
print(a)

#1091
a, m, d, n = map(int, input().split())
for i in range(n-1):
    a = a * m + d
print(a)

#1092
#1251
#1252
#1253
a, b = map(int, input().split())
for i in range(min(a,b),max(a,b)+1):
    print(i, end=' ')

#1254
#1255
a, b = map(float, input().split())
while a <= b:
    print("%.2f" % a, end=' ')
    a += 0.01

#1256
#1257
#1258
#1259
#1260
#1261
a = map(int, input().split())
check = False
for i in a:
    if i % 5 == 0:
        print(i)
        check = True
        break
if check != True:
    print("0")

#1265
#1266
#1267
#1268
#1269
#1270
#1271
#1272
k, h = map(int, input().split())
s = 0
if k % 2 == 0:
    s += k * 5
else:
    s += int((k-1) / 2 + 1)
if h % 2 == 0:
    s += h * 5
else:
    s += int((h-1) / 2 + 1)
print(s)

#1273
#1274
#1275
#1276
#1277
#1278
#1279
#1280
#1281
a, b = map(int, input().split())
s = 0
for i in range(a, b+1):
    if i % 2 == 0:
        print("-%d" % i, end='')
        s -= i
    else:
        if i == a:
            print(i, end='')
        else:
            print("+%d" % i, end='')
        s += i
print("=%d"%s)

#1282
import math
a = int(input())
b = 0
while 1:
    if math.sqrt(a-b) % 1 == 0:
        a = math.sqrt(a-b)
        break
    b += 1
print("%d %d" %(b, a))

#1283
a = int(input())
b = int(input())
v = list(map(int, input().split()))
final = a
for i in v:
    if i < 0:
        final = final - (final * (i * -1 / 100))
    else:
        final = final + (final * (i / 100))
a = int('{0:.0f}'.format(final-a))
print(a)
if a > 0:
    print("good")
elif a ==0:
    print("same")
else:
    print("bad")

#1284
def so(m):
    for j in range(2,int(m/2)+1):
        if m % j == 0:
            return False
    return True

n = int(input())
check = False
for i in range(2,int(n/2)+1):
    if n % i == 0 and so(i) == True and so(int(n/i))== True:
        print("%d %d" %(i, int(n/i)))
        check = True
        break
if check == False:
    print("wrong number")

#1285
n = input()
a = ['+', '-', '*', '/', '=']
check, ans, ans2 = 0, '', ''
b = '+'
for i in n:
    if check == 1 and i in a:
        ans2 = str(int(eval(ans2+b+ans)))
        ans = ''
        b = i
    elif i in a:
        check = 1
        b = i
    elif check == 0:
        ans2 = ans2 + i
    else:
        ans = ans + i
print(ans2)

#1286
#1287
#1294
n = input()
for i in n:
    if i == 'x' or i == 'y' or i == 'z':
        i = ord(i)
        print(chr(i - 23), end='')
    elif i == ' ':
        print(end=' ')
    else:
        i = ord(i)
        print(chr(i+3), end='')

#1295
#1675
n = input()
for i in n:
    if i == 'a' or i == 'b' or i == 'c':
        i = ord(i)
        print(chr(i + 23), end='')
    elif i == ' ':
        print(end=' ')
    else:
        i = ord(i)
        print(chr(i-3), end='')
