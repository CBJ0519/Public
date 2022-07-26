'''
(url: https://zerojudge.tw/ShowProblem?problemid=i399)

內容
給三個 1 ~ 9 的數字
先輸出一個數值 P 表示眾數數量
接下來將輸入的三個數字去除重複（剩下一個）後由大到小輸出
輸入說明
三個介於 1~9 的整數
輸出說明
先輸出一個數值 P 表示眾數數量
接下來將輸入的三個數字去除重複（剩下一個）後由大到小輸出

範例輸入 #1
6 6 6
範例輸出 #1
3 6

範例輸入 #2
7 9 7
範例輸出 #2
2 9 7

範例輸入 #3
4 1 8
範例輸出 #3
1 8 4 1
'''
from collections import Counter
L=[int(x) for x in input().split()]
a=Counter(L).most_common()
print(a[0][1],end=' ')
b=sorted(set(L),reverse=True)
for i in b:
    print(i,end=' ')
