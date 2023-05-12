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
# 就要写递归~
'''
def sum(a, b, res):
    if a > b: return res
    return sum(a + 1, b, res + a)

a, b = map(int, input().split())
res = 0
res = sum(a, b, res)
print(res)
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









