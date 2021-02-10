#1010
m = input()
print(m)

#1011
m = input()
print(m)

#1012
m = float(input())
print("%6f" % m)

#1013
m,n = map(int, input().split())
print(m,n)

#1014
m,n = input().split()
print(n,m)

#1015
m = float(input())
print("%.2f" % m)

#1017
m = int(input())
print(m,m,m)

#1018
m = input()
print(m)

#1019
y,m,d = map(int, input().split('.'))
print("%04d.%02d.%02d" %(y,m,d))

#1020
m,n = input().split('-')
print("%s%s" % (m,n))

#1021
m = input()
print(m)

#1022
m = input()
print(m)

#1023
m,n = input().split('.')
print(m)
print(n)

#1024
m = input()
for i in m:
    print("\'%s\'" %i)

#1025
m = input()
n = len(m)
for i in m:
    print("[%s]" %i.ljust(n, "0"))
    n = n-1

#1026
m = input()
n = len(m)
for i in m:
    print("[%s]" %i.ljust(n, "0"))
    n = n-1

#1027
y,m,d = map(int, input().split('.'))
print("%02d-%02d-%04d" %(d,m,y))

#1028
n = input()
print(n)

#1029
n = float(input())
print("%.11f" %n)

#1030
n = input()
print(n)

#1031
n = int(input())
print("%o" % n)

#1032
n = int(input())
print("%x" % n)

#1033
n = int(input())
print("%X" % n)

#1034
n = input()
print("%d" % int(n, 8))

#1035
n = input()
print("%o" % int(n, 16))

#1036
n = input()
print(ord(n))

#1037
n = int(input())
print(chr(n))

#1038
n,m= map(int, input().split())
print(m+n)

#1039
n,m= map(int, input().split())
print(m+n)

#1040
n = int(input())
print(-n)

#1041
n = ord(input())
print(chr(n+1))

#1042
n,m= map(int, input().split())
print(int(n/m))

#1043
n,m = map(int, input().split())
print(n%m)

#1044
n= int(input())
print(n+1)

#1045
m, n= map(int, input().split())
print(m+n)
print(m-n)
print(m*n)
print(int(m/n))
print(m%n)
print("%.2f" %(m/n))

#1046
n,m, r = map(int, input().split())
print(n+m+r)
print("%.1f" %((n+m+r)/3))

#1047
n = int(input())
print("%d" %(n<<1))

#1048
m, n= map(int, input().split())
res = m
for i in range(n):
    res = res * 2
print(res)
'''
import math
m, n= map(int, input().split())
m = m * math.pow(2, n)
print(int(m))
'''

#1049
m, n= map(int, input().split())
if m-n > 0:
    print(1)
else:
    print(0)

#1050
n1, n2 =map(int, input().split())
res = 0
if n1 == n2:
    res = 1
print(res)

#1051
n1, n2 =input().split()
res = 0
if int(n1) <= int(n2):
    res = 1
print(res)

#1052
n1, n2 =input().split()
res = 0
if int(n1) != int(n2):
    res = 1
print(res)

#1053
m = int(input())
if m == 0:
    print(1)
else:
    print(0)

#1054
m, n = map(int, input().split())
if m == 1 and n == 1:
    print(1)
else:
    print(0)

#1055
n1, n2 =input().split()
res = 0
if int(n1) == 1 or int(n2) == 1:
    res = 1
print(res)

#1056
n1, n2 =input().split()
res = 0
if int(n1) != int(n2):
    res = 1
print(res)

#1057
n1, n2 =input().split()
res = 0
if int(n1) == int(n2):
    res = 1
print(res)

#1058
m, n = map(int, input().split())
if m == 0 and n == 0:
    print(1)
else:
    print(0)

#1059
n1 = int(input())
print(~n1)

#1060
n1,n2 = map(int, input().split())
print(n1 & n2)

#1061
n1,n2 = input().split()
print(int(n1) | int(n2))

#1062
n1,n2 = input().split()
print(int(n1) ^ int(n2))

#1063
n1 , n2 = input().split()
if int(n1) < int(n2):
    print(n2)
else:
    print(n1)

#1064
m, n, r = map(int, input().split())
print(min(m,n,r))

#1085
h, b, c, s = map(int, input().split())
print('%.1f MB' % (h*b*c*s/8/1024/1024))

#1086
w, h, b = map(int, input().split())
print("%.2f MB" %(w*h*b/8/1024/1024))

#1110
m = input()
print(m)

#1111
n = int(input())
print("%d%%" %n)

#1112
m,n = map(int,input().split())
print(m, n)

#1113
m,n = map(int,input().split())
print(n, m)

#1114
m,n = map(int,input().split())
print(n+m)

#1115
m,n = map(int,input().split())
print(n+m)

#1116
m,n = map(int, input().split())
print("%d+%d=%d" %(m,n,m+n))
print("%d-%d=%d" %(m,n,m-n))
print("%d*%d=%d" %(m,n,m*n))
print("%d/%d=%d" %(m,n,int(m/n)))

#1117
m,n = map(float, input().split())
print("%.2f" %(m*n))

#1118
m,n = map(int, input().split())
print("%.1f" %(m*n/2))

#1119
m = int(input())
print(m*24)

#1120
m,n, r = map(int, input().split())
print("%.2f" %((m+n+r)/3))

#1121
m,n = map(int, input().split())
print(m%n)

#1122
m = int(input())
print("%d %d" % (int(m/60),m%60))

#1123
m = int(input())
print("%.3f" %(9/5*m+32))

#1125
m = int(input())
print("%o %X" %(m,m))

#1131
m = input()
print(m)

#1132
m = input()
print(m)

#1133
m = input()
print(m)

#1135
m, n = map(int, input().split())
if m >= n:
    print(1)
else:
    print(0)

#1136
m, n = map(int, input().split())
if m == n:
    print(1)
else:
    print(0)

#1137
m, n = map(int, input().split())
if m != n:
    print(1)
else:
    print(0)

#1138
m = int(input())
if m == 0:
    print(1)
else:
    print(0)

#1139
m,n = map(int, input().split())
if m == 1 and n ==1:
    print(1)
else:
    print(0)

#1140
m,n = map(int, input().split())
if m == 1 or n ==1:
    print(1)
else:
    print(0)

#1143
m,n = map(int, input().split())
print(m&n)

#1144
m,n = map(int, input().split())
print(m|n)

#1147
m,n = map(int, input().split())
print(m<<n)

#1148
m,n = map(int, input().split())
print(m>>n)

#1149
m,n = map(int, input().split())
print(max(m,n))

#1150
m, n ,r = map(int, input().split())
print(min(m,n,r))
