# OJ网站   https://vijos.org/d/nnu_contest/p/category/《程序设计基础》课程赛事

## 1-1 数字循环左移
# 字符串切片、拼接
'''
s = input()
print(s[1::]+s[0])
'''
import math

## 1-2 斐波那契数列的和
# 递归函数自定义、多整数读入、for+range遍历操作
'''
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

a, b = map(int, input().split())
res = 0
for i in range(a, b + 1):
    res += f(i)
print(res)
'''

## 1-3 序列循环左移
# 将数组以字符串形式读入、按照空格切割、将切割后的元素转化为整型、列表拼接、
# 整型元素转化为字符串后使用join函数按空格输出
'''
n = int(input())
s = input().split()
s = [int(it) for it in s]
s = s[1::] + s[:1:]
print(' '.join(str(it) for it in s))
'''

## 1-4 最大值的个数
# 列表函数max(), count()的使用
'''
n = int(input())
nums = input().split()
nums = [int(it) for it in nums]
print(nums.count(max(nums)))
'''

## 2-1 单个数的3N+1猜想
# 循环、分支语句
'''
x = int(input())
cnt = 0
while x > 1:
    if x % 2 == 1:
        x = x * 3 + 1
        cnt += 1
    else:
        x /= 2
        cnt += 1
print(cnt)
'''

## 2-2 语言的起点
# 字符串拼接
'''
n = int(input())
a = input()
b = input()
for i in range(n):
    b += a
    a += b
print(a)
'''

## 2-3 参赛人数
# 利用set对列表进行去重
'''
na, nb = map(int, input().split())
a = input().split(); b = input().split()
res = set(a + b) # 去重操作
print(len(res))
'''

## 2-4 点名上前
# 列表下标索引、列表remove()函数
'''
n, k = map(int, input().split())
nums = input().split()
nums = [int(it) for it in nums]
leader = nums[k - 1]
nums.remove(leader)
res = [str(leader)] + [str(it) for it in nums]
print(' '.join(res))
'''

## 3-1 整数中的数字
# 列表初始化创建：打表
'''
def find_most_frequent_digit(xmin, xmax):
    freq = [0] * 10
    for i in range(xmin, xmax + 1):
        while i > 0:
            freq[i % 10] += 1
            i //= 10
    flag = max(freq)
    for i in range(0, 10):
        if freq[i] == flag:
            return i

a, b = map(int, input().split())
res = find_most_frequent_digit(a, b)
print(res)
'''

## 3-2 约瑟夫问题
# pop(idx)：根据下标删除元素，效率更高
# remove(a[idx])：删除从左到右的搜索到的第一个相等的元素
'''
n, k = map(int, input().split())
a = [i for i in range(1, n + 1)]
idx = 0
while len(a) > 1:
    idx = (idx + k - 1) % len(a)
    a.pop(idx)
print(a[0])
'''

## 3-3 炒股发财
# 数学模块math中的无穷大inf
'''
n = int(input())
nums = input().split()
nums = [int(it) for it in nums]

mi = nums[0]
res = -math.inf
for it in nums[1:]:
    res = max(res, it - mi)
    mi = min(mi, it)
print(res)
'''

## 3-4 颠倒单词
# split会按照要求自动分割读入的字符串并且返回一个列表
# split()会将多个空格自动合并为一个空格！
# 修改列表元素需要索引其中的元素
'''
sentence = input().split()
# 写法一：列表解析式法
# sentence = [word[::-1] for word in sentence]
# 写法二：循环索引列表
for i in range(len(sentence)):
    sentence[i] = sentence[i][::-1]

print(' '.join(sentence))
'''

## 3-5 计算器
# 字符串find函数用法：查找母串中第一个匹配到子串的第一个字符的下标，如果没找到，返回-1
# 三目运算符用法：res_1 if condition else res_2
'''
expression = input()
flag = '+' if expression.find('+') != -1 else '-'
a, b = map(int, expression.split(flag))
res = a + b if flag == '+' else a - b
print(res)
'''

## 3-6 查找资料
# 字符串count函数统计子串个数
'''
sentence = input()
word = input()
print(sentence.count(word))
'''

## 4-3 爱情故事
# replace() 函数实现替换指定字符串中的第一个匹配到的子串为指定子串，返回一个新的字符串而不会改变原来的字符串
'''
sentence = input()
word_before = input()
word_after = input()
# 写法一：循环解决
# while sentence.find(word_before) != -1:
#     sentence = sentence.replace(word_before, word_after)
# 写法二：增加replace的第三参数
new_sentence = sentence.replace(word_before, word_after, sentence.count(word_before))
print(new_sentence)
'''

## 5-6 过去了多少天
# datatime类的使用
'''
from  datetime import date
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
d1 = date(y1, m1, d1)
d2 = date(y2, m2, d2)
delta = d2 - d1
print(delta.days)
'''

## A1-1 分支结构练习：三数排序
# 直接按照字符串进行比较排序即可，否则还需要先转化为整型，再转化为str进行去掉列表输出的操作
# sorted()返回一个新的可迭代对象
# sorted()中有三个参数位置，一个是可迭代对象，一个是排序关键字key=，一个是升序降序关键字
'''
a = input().split()
print(' '.join(sorted(a, reverse=True)))
'''

## A1-2 分支结构练习：三数的特征值
# 由于python中字符串的比较默认是按照Unicode码进行的，因此对于纯数字的字符串比较，可以直接用字符串比较得出
# 而不需要强制类型转化了
'''
nums = input().split()
# nums = [int(it) for it in nums]
print(sorted(nums)[1], max(nums))
'''

## A1-4 分支结构练习：今年过去了多少天
# 通过datetime.date()进行构造
'''
import datetime
year, month, day = map(int, input().split())
now = datetime.date(year, month, day)
start = datetime.date(year, 1, 1)
print((now - start).days + 1)
'''

## A2-1 循环结构入门：数列求和
# 循环
'''
a, b = map(int, input().split())
res = 0
l, r = a, b
while l <= r:
    res += l
    l += 1
print(res)
'''

# 特以此题留念一下我自己编写的第一个递归程序
# 在Python中，默认的最大递归深度是1000
'''
def sum(a, b):
    if a == b: return b;
    return a + sum(a + 1, b)

a, b = map(int, input().split())
print(sum(a, b))
'''

## A2-2 循环结构入门：斐波拉契数列
# 列表添加元素、遍历列表
'''
arr = []
n = int(input())
a, b = 1, 1
c = a + b
while len(arr) < n:
    arr.append(a)
    a = b
    b = c
    c = a + b
for it in arr: print(it, end=' ')
'''

## A2-3 循环结构入门：斐波拉契数列的和
# 列表求和函数
'''
arr = []
n = int(input())
a, b = 1, 1
c = a + b
while len(arr) < n:
    arr.append(a)
    a = b
    b = c
    c = a + b
print(sum(arr))
'''

## A3-1 素数专题：因子的和
# pycharm中如果检测到了使用的模块，即使没有显式的导入，也会自动检测并导入
# 因此为了提高程序的稳定性，还是需要显示导入标准库
# / 与 // 的区别在于前者是浮点运算，而后者是整除运算
# sqrt可读性比较高而且可以进行复数运算，但是x**0.5不可以
'''
import math

x = int(input())
res = 0
for i in range(1, (int(math.sqrt(x)) + 1)):
    if x % i == 0:
        if x // i == i:
            res += i
        else:
            res += i + x // i
print(res)
'''

## A3-2 素数专题：素数判断
'''
import math

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

x = int(input())
if is_prime(x): print("Yes")
else: print("No")
'''

## A3-3 素数专题：素数个数
'''
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
cnt = 0
for i in range(2, n + 1):
    if is_prime(i):
        cnt += 1
print(cnt)
'''

## A3-4 素数专题：验证哥德巴赫猜想
# 注意输出格式: print('%d+%d=%d' % (i, n - i, n))
'''
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n // 2 + 1):
    if is_prime(i) and is_prime(n - i):
        print('%d+%d=%d' % (i, n - i, n))
'''

## A5-1 超级素数判断
'''
import math

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
flag = True
while n > 0:
    if not is_prime(n):
        flag = False
        break
    n //= 10
print("Yes" if flag else "No")
'''

## A5-2 超级素数的个数
# 主要讨论传入值是否可以被改变的问题
# 首先python中传入的都是变量的引用
# 其次就是对于传入的变量，数字，字符串，元组，不可变集合是无法修改的
# 传入列表会自动识别为元组
# 传入参数的形式有待研究
'''
import math

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_super_prime(x):
    while x:
        if not is_prime(x):
            return False
        x //= 10
    return True

n = int(input())
cnt = 0
for i in range(2, n + 1):
    if is_super_prime(i):
        cnt += 1
print(cnt)
'''

## A6-3 最大公约数专题：多个分数的加法
# 分数计算的底层方法
# print函数输出的用法，直接用逗号分隔就直接依次输出，中间有空格，如果不想有空格直接写成变量A+变量B
'''
import math

n = int(input())
up = 0
low = 1
for i in range(n):
    a, b = map(int, input().split())
    up = up * b + low * a
    low *= b
div = math.gcd(up, low)
up, low = up // div, low // div
print(up, low)
'''

## A6-4 最大公约数专题：多个数的最大公约数
#
'''
import math

n = int(input())
nums = input().split()
nums = [int(it) for it in nums]
num = nums[0]
for i in range(1, n):
    num = math.gcd(num, nums[i])
print(num)
'''

## A7-5 数组的有序插入函数
#
'''
n = int(input())
nums = input().split()
nums = [int(it) for it in nums]
num = int(input())

nums.append(num)
print(*sorted(nums))
'''

## A7-6 数组的左移函数
# 在输出单个字符的时候不会加单引号
'''
def fun():
    n = int(input())
    nums = input().split()
    k = int(input())

    for i in range(k):
        tmp = nums[0]
        nums.pop(0)
        nums.append(tmp)

    print(*nums)


if __name__ == '__main__':
    fun()
'''

## A7-7 数组的右移函数
'''
from collections import deque

def MoveRight():
    n = int(input())
    nums = deque([int(it) for it in input().split()])
    k = int(input())

    nums.rotate(k)

    print(*nums)

if __name__ == '__main__':
    MoveRight()
'''

## A8-1 字符串的输出函数
#
'''
def f(str):
    hi = sum([c.isupper() for c in str])
    lo = sum([c.islower() for c in str])
    return hi - lo

if __name__ == '__main__':
    s = input(); t = input()
    print(f(s), f(t))
'''

## A8-2 字符串的统计函数
# 压行压到位
'''
s = input()
t = input()
print(sum([c.islower() for c in s]), end=' ')
print(sum([c.islower() for c in t]))
'''

## A8-3 字符串的统计函数
# 同上
'''
def f(str):
    hi = sum([c.isupper() for c in str])
    lo = sum([c.islower() for c in str])
    return hi - lo

if __name__ == '__main__':
    s = input(); t = input()
    print(f(s), f(t))
'''

## A8-4 字符串的连接函数
# 注意负数索引在python中的灵活应用
'''
def Concat(s1: str, s2: str) -> str:
    return s1 + s2

if __name__ == '__main__':
    s = input(); t = input()
    ans = Concat(s[:-1], t[1:])
    print(ans)
'''

## A8-5 删除字符串中多余的一种字符
# 列表推导式、解包、print函数的分隔符参数sep
'''
s = input()
ch = input()
print(*[c if c != ch else '' for c in s], sep='')
'''

## A8-6 删除字符串中多余的多种字符
# 同上
'''
s = input()
t = input()
print(*[c if c not in t else '' for c in s], sep='')
'''

## A8-7 删除字符串中一个子串
# python中的索引已经做好防越界保护了
'''
s = input()
bi, le = map(int, input().split())
print(s[:bi] + s[(bi + le):])
'''

## A9-1 数组中的素数个数
# 如果不对一个线性表中的数据进行修改的话，建议使用元组，速度大约是列表的三倍
# str.split()返回一个列表！！！
'''
import math

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def f(nums):
    cnt = 0
    for it in nums:
        if is_prime(int(it)):
            cnt += 1
    return cnt

if __name__ == '__main__':
    m, n = map(int, input().split())
    a = [int(it) for it in input().split()]
    b = [int(it) for it in input().split()]
    print(f(a), f(b))
'''


## A9-2 数组中最小正数的下标
# 详细标注见supplement文件的第五代码块
'''
from typing import Tuple

def f(nums: Tuple) -> int:
    return nums.index(min(filter(lambda x : x > 0, nums)))

if __name__ == '__main__':
    m, n = map(int, input().split())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    print(f(a), f(b))
'''


