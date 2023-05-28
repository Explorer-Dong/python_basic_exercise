# @Time   : 2023-05-28 13:39
# @File   : dict.py
# @Author : Mr_Dwj

s = input().split()
word_cnt = {}
for it in s:
    if it in word_cnt:
        word_cnt[it] += 1
    else:
        word_cnt[it] = 1

word_list = list(word_cnt)
word_list.sort()
for it in word_list:
    print(it, word_cnt[it])