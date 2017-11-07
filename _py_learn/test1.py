print('-------------------------------')

# 字符串与编码
print(ord('中'), ord('国'))
print(chr(20013), chr(20014))

# encode decode
x = 'abc'
y = '我'
print(x, y)

xx = x.encode('ascii')
yy = y.encode('utf-8')
print(xx, yy)

x = xx.decode('ascii')
y = yy.decode('utf-8')
print(x, y)

print('-------------------------------')

# list 与 tuple

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0], L[1][1], L[2][2])

L.pop(1)
print(L)

L.insert(1, 'a new Element')
L.append('the rear')
print(L)

t = ('a', 'b', 'c')

print('-------------------------------')

while 1:
    s = input("birth: ")
    birth = int(s)
    if birth >= 2000:
        print('after 00')
    elif birth >= 1990:
        print('after 90')
    else:
        break

print('-------------------------------')

# dic: key-value
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])
print(d.get('c'))

# set
print()
l = ['1', '2', '3']
t = (1, 2, 3)
s1 = set(l)
s2 = set(t)
print(s1)
print(s2)

print('-------------------------------')