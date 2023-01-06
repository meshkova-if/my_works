print('Hello world')
name = 'John'
dayofweek = 'Friday'
print('Hello, {}! Today is {}.Have a nice day!'.format(name, dayofweek))
h = [(range(1, 111))]
print(h)
k = range(1, 10)
print(k)
a = list(range(-10, 100))
print(a)
b = list(range(50, 20, -2))
print(b)
a = ["a", "b", "c", "d", "e"]
print(a)
print(a[0:4:2])
b = a[::-1]
print(b)
b_slice = list(range(1, 10))
print(b_slice)
a_slice = b_slice[::2]
print(a_slice)
a = ["a", "b", "c", "d", "e"]
a_spisok = list(range(-5, 5))
print(a_spisok)
b_spisok = a_spisok[:-2:1]
print(b_spisok)
a = {"a", "b", "c", "d", "e"}
b = {"bad boy"}
a.difference(b)
a, b, c = map(int, input('Введите сторону треугольника:').split())
print('Периметр:', a + b + c)
#a = 7
#b = -4P
#c = 3
#print(a, b, c, sep=' ')
#s1, s2 = map(str.strip, input().split())
#print(f'Word 1: {s1} ',f' Word 2: {s2}',sep='|')
#a, b = map(float, input().split())
#print(a+b)
#X, Y = map(int, input().split())
#X_x = X*2
#Y_y = Y*4
#print(X+Y+X_x+Y_y)
#a = float(input())
#b = float(input())
#print((a + b)*2)
#import math
#print(round(math.pi,3))
#a = float(input())
#print("Вы ввели число", a)
#y = 1.85
#print(y >= -2 and y <= 5)
#print((1+2)*('7'+'8'))
#a, b = map(str, input().split())
#print("Переменная a = "+str(a)+ ","+" переменная b = " +str(b))
#a = input()
#print('Строка:' , a + '.','Длина:', len(a))
#a, z = map(str, input().split())
#print(f"Коды: {a} = {ord(a)}, {z} = {ord(z)}")
#print(input().find('ra'))
#s1 = input().replace('--', '-').replace('--', '-')
#print(s1)