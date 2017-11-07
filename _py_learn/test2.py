# 变量引用函数
a = abs
print(a(-67))


# 返回多个值（tuple）
def return_multi_value(x, y):
    return x * x, y * y


x = 2
y = 3
x, y = return_multi_value(x, y)
t = return_multi_value(x, y)
print(x, y)
print(t)


# 默认参数必须指向不变对象
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


print(add_end())
print(add_end())


# 可变参数
def calc(*nums):
    sum = 0
    for num in nums:
        sum += num * num
    return sum


nums = [1, 2, 3]
print("1^2 + 2^2 + 3^2 = ", calc(*nums))


# 关键字参数
def person(name, age, **kwargs):
    print("name : ", name, " age : ", age, " others : ", kwargs)


name = 'snow'
age = 20
args = {'city': 'wuhan', 'university': 'whu'}
person(name, age)
person(name, age, **args)

# 命名关键字参数


# 参数组合



print("-----------------")

for i in range(0):
    print(i, "\n")