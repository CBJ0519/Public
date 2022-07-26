'''
(url: https://zerojudge.tw/ShowProblem?problemid=d732)

內容
給你一個嚴格遞增的數列A1,A2,A3.....An(1<=n<=100000), 
下面有幾個問題的詢問數k(1<=K<=100000),以及k個詢問的整數x,
求數列中是否存在一個Ai(1<=i<=n)的值與X相等?

輸入說明
第一行包含兩個整數n,k分別表示數列長度以及詢問數,
第二行包含n個整數第i(1<=i<=n)個整數依序為數列中Ai的值,
第三行包含k個詢問的整數x. 

輸出說明
對於每個詢問整數x對應一行輸出:
輸出i的值
其中1<=i<=n且Ai=x
若沒有這樣的i值請輸出0代替.

範例輸入 #1
5 5
1 3 4 7 9
3 1 9 7 -2
範例輸出 #1
2
1
5
4
0
'''
def binarysearch(d,q,s,e):
    mid=(s+e)//2
    if e-s==1: return -1
    elif q==d[s]: return s
    elif q==d[e]: return e
    elif q==d[mid]: return mid
    elif q<d[mid]: return binarysearch(d,q,s,mid)
    elif q>d[mid]: return binarysearch(d,q,mid,e)
input()
d=[int(x) for x in input().split()]
q=[int(x) for x in input().split()]
for i in range(len(q)): print(int(binarysearch(d,q[i],0,len(d)-1))+1)
