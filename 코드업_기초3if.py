#1065
a = list(map(int, input().split()))
for i in a:
    if i % 2 == 0:
        print(i)

#1066
a = list(map(int, input().split()))
for i in a:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

#1067
a = map(int, input().split())
for i in a:
    if i > 0:
        print("plus")
    else:
        print("minus")
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

#1068
n1 = int(input())
if n1 >= 90:
    print("A")
elif n1 >= 70:
    print("B")
elif n1 >= 40:
    print("C")
else:
    print("D")

#1069
a = input()

if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

#1070
n = int(input())
if n == 12 or n == 1 or n == 2:
    print("winter")
elif n == 3 or n == 4 or n == 5:
    print("spring")
elif n == 6 or n == 7 or n == 8:
    print("summer")
elif n == 9 or n == 10 or n == 11:
    print("fall")

#1151
n = int(input())
if n < 10:
    print("small")

#1152
n = int(input())
if n < 10:
    print("small")
else:
    print("big")

#1153
a, b = map(int, input().split())
if a > b:
    print(">")
elif a<b:
    print("<")
else:
    print("=")

#1154
a, b = map(int, input().split())
print(max(a,b)-min(a,b))

#1155
a = int(input())
if a % 7 == 0:
    print("multiple")
else:
    print("not multiple")

#1156
a = int(input())
if a % 2 == 0:
    print("even")
else:
    print("odd")

#1157
a = float(input())
if a >= 50 and a <= 60:
    print("win")
else:
    print("lose")

#1158
a = int(input())
if (a >= 30 and a <= 40) or (a >= 60 and a <= 70):
    print("win")
else:
    print("lose")

#1159
a = int(input())
if (a >= 50 and a <= 70) or (a % 6 == 0):
    print("win")
else:
    print("lose")

#1160
a = int(input())
if a % 2 == 0:
    print("enjoy")
else:
    print("oh my god")

#1161
a, b = map(int, input().split())
if a % 2 == 0:
    if b % 2 == 0:
        print("짝수+짝수=짝수")
    else:
        print("짝수+홀수=홀수")
else:
    if b % 2 == 0:
        print("홀수+짝수=홀수")
    else:
        print("홀수+홀수=짝수")

#1162
y, m, d = map(int, input().split())
if (y-m+d) % 10 == 0:
    print("대박")
else:
    print("그럭저럭")

#1163
y, m, d = map(int, input().split())
if (int((y+m+d) / 100) % 10) % 2 == 0:
    print("대박")
else:
    print("그럭저럭")

#1164
a, b, c = map(int, input().split())
if a > 170 and b > 170 and c > 170:
    print("PASS")
else:
    print("CRASH")

#1165
a, b = map(int, input().split())
while a < 90:
    b += 1
    a += 5
print(b)

#1166
a = int(input())
if a % 4 ==0 and a % 100 != 0:
    print("yes")
elif a % 400 == 0:
    print("yes")
else:
    print("no")

#1167
a = list(map(int, input().split()))
a.sort()
print(a[1])

#1168
a, b= map(int, input().split())
a= int(a/10000)
if b == 1 or b == 2:
    print(2012 - (1900 + a) + 1)
else:
    print(2012 - (2000 + a) + 1)

#1169
a = int(input())
b = (2012+1-a)
if int(b/100) == 20:
    print("%d 3" % (b - 2000))
else:
    print("%d 1" % (b - 1900))

#1170
a, b, c = map(int, input().split())
print("%d%d%02d" %(a, b, c))

#1171
a, b, c = map(int, input().split())
print("%d%02d%03d" %(a, b, c))

#1172
a = list(map(int, input().split()))
a.sort()
for i in a:
    print(i, end=' ')

#1173
a, b = map(int, input().split())
if b - 30 >= 0:
    print("%d %d" % (a, b-30))
else:
    if a == 0:
        print("%d %d" % (23, b + 30))
    else:
        print("%d %d" % (a-1, b + 30))

#1180
a = int(input())
b = a % 10
a = (int(a/10) + (b * 10)) * 2
if a >= 100:
    a = a % 100
print(a)
if a > 50 :
    print("OH MY GOD")
else:
    print("GOOD")

#1201
a = int(input())
if a > 0:
    print("양수")
elif a < 0 :
    print("음수")
else:
    print("0")

#1202
a = int(input())
if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else:
    print("F")

#1203
a = int(input())
if a > 20:
    print("비만")
elif a > 10:
    print("과체중")
else:
    print("정상")

#1204
a = int(input())
if a % 10 == 1:
    if a == 11:
        print("11th")
    else:
        print("%dst" % a)
elif a % 10 == 2:
    if a == 12:
        print("12th")
    else:
        print("%dnd" % a)
elif a % 10 == 3:
    if a == 13:
        print("13th")
    else:
        print("%drd" % a)
else:
    print("%dth" % a )

#1205
a, b = input().split()
c = []
d = ['+', '-', '*', '/', '**']
for i in d :
    c.append(eval(a+i+b))
    c.append(eval(b+i+a))
print("%.6f" %max(c))

#1206
a, b = map(int, input().split())
if max(a,b) % min(a,b) == 0:
    if max(a,b) == a:
        print("%d*%d=%d" % (b,int(a/b),a))
    else:
        print("%d*%d=%d" % (a, int(b / a), b))
else:
    print("none")

#1207
a = list(map(int, input().split()))
a = sum(a)
if a == 4:
    print("윷")
elif a == 3:
    print("걸")
elif a == 2:
    print("개")
elif a == 1:
    print("도")
else:
    print("모")

#1210
a, b = map(int, input().split())
cal = [400, 340, 170, 100, 70]
if cal[a-1]+cal[b-1] > 500:
    print("angry")
else:
    print("no angry")

#1212
a = list(map(int, input().split()))
a.sort()
if a[2] < a[0] + a[1]:
    print("yes")
else:
    print("no")

#1214
a, b = map(int, input().split())
c = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if b == 2:
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
        print(c[b-1]+1)
    else:
        print(c[b-1])

else:
    print(c[b-1])

#1216
a = list(map(int, input().split()))
if a[1] - a[2] < a[0]:
    print("do not advertise")
elif a[1] - a[2] > a[0]:
    print("advertise")
else:
    print("does not matter")

#1218
a = list(map(int, input().split()))
a.sort()
if a[2] < a[0] + a[1]:
    if a[0] == a[1] == a[2]:
        print("정삼각형")
    elif a[0] == a[1] or a[1] == a[2]:
        print("이등변삼각형")
    elif a[0]**2 + a[1]**2 == a[2]**2:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형아님")

#1222
a, b, c = map(int, input().split())
while a < 90:
    b += 1
    a += 5
if b > c:
    print("win")
elif b == c :
    print("same")
else:
    print("lose")

#1224
a, b, c, d = map(int, input().split())
if a/b > c/d:
    print(">")
elif a/b == c/d:
    print("=")
else:
    print("<")

#1226
a = list(map(int, input().split()))
jh = list(map(int, input().split()))
lo = a[:-1]
count = 0
for i in jh:
    if i in lo:
        count += 1
if count == 6:
    print(1)
elif count == 5:
    if a[6] in jh:
        print(2)
    else:
        print(3)
elif count == 4:
    print(4)
elif count == 3:
    print(5)
else:
    print(0)

#1228
a, b = map(float, input().split())
stand = (a - 100) * 0.9
con = (b-stand)*100 / stand
if con > 20 :
    print("비만")
elif con > 10:
    print("과체중")
else:
    print("정상")

#1229
h, w = map(float, input().split())
if h < 150:
    stand = h-100
elif h < 160:
    stand = (h - 150)/2 +50
else:
    stand = (h - 100) * 0.9
con = (w-stand)*100 / stand
if con > 20 :
    print("비만")
elif con > 10:
    print("과체중")
else:
    print("정상")

#1230
a, b, c = map(int, input().split())
if a <= 170:
    print("CRASH %d" %a)
elif b <= 170:
    print("CRASH %d" % b)
elif c <= 170:
    print("CRASH %d" % c)
else:
    print("PASS")

#1231
a = input()
if "/" in a:
    print("%.2f" % eval(a))
else:
    print(eval(a))