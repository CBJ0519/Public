'''
(url: https://zerojudge.tw/ShowProblem?problemid=c295)

內容
給定N群數字，每群都恰有M個正整數。
若從每群數字中各選擇一個數字 (假設第 i群所選出數字為ti)，將所選出的N個數字加總即可得和 S = t1+t2+…+ +…+ tN。
請寫程式計算 S的最大值 (最大總和 )，並判斷各群所選出的數字是否可以整除 S。

原題 : https://ppt.cc/fO8Otx@.png

輸入說明
第一行有二個正整數 N和 M， 1≦ N ≦ 20 ，1≦ M ≦ 20 。
接下來的N行，每一行各有M個正整數 xi ，代表一群整數，數字與數字間有一個空格，且 1≦ i ≦M，以及 1≦ xi ≦256 。

輸出說明
第一行輸出最大總和 S。
第二行按照被選擇數字所屬群的順序，輸出可以整除S的被選擇數字，數字與數字間以一個空格隔開，最後一個數字後無空白；
若 N個被選擇數字都不能整除S，就輸出 -1。

範例輸入 #1
3 2
1 5
6 4
1 1
範例輸出 #1
12
6 1

範例輸入 #2
4 3
6 3 2
2 7 9
4 7 1
9 5 3
範例輸出 #2
31
-1

提示 ：
（範例一說明） 挑選的數字依序是 5, 6, 1，總和S=12。
而此三數中可整除S的是 6與 1，6在第二群，1在第3群所以先輸出6再輸出1。
注意，1雖然也出現在第一群，但她不是第一群中挑出的數字，所以順序是先 6後 1。
（範例二說明） 挑選的數字依序是6,9,7,9，總和 S= 31 。而此四數中沒有可整除 S的， 所以第二行輸出 -1。

'''
while True:
    try:
        n,m=map(int,input().split())
        total=0
        choice=[]
        for i in range(n):
            s=list(map(int,input().split()))
            choice.append(max(s))
        total=sum(choice)
        print(total)
        a=[]
        for j in choice:
            if total%j==0: a.append(j)
        if a==[]: print(-1)
        else: print(*a,sep=' ')
    except EOFError:
        break
