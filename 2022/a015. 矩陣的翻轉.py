'''
(url: https://zerojudge.tw/ShowProblem?problemid=a015)

已知一(m x n)矩陣A，我們常常需要用到另一個將A中之行與列調換的矩陣。
這個動作叫做矩陣的翻轉。舉例來說，若

A =	
3	1	2
8	5	4
則

AT =	
3	8	
1	5
2	4
 
現在 請您針對所讀取到的矩陣進行翻轉。

輸入說明
第一行會有兩個數字，分別為 列(row)<100 和 行(column)<100，緊接著就是這個矩陣的內容

輸出說明
直接輸出翻轉後的矩陣

範例輸入 #1
2 3
3 1 2
8 5 4
範例輸出 #1
3 8
1 5
2 4
'''
try:
    while True:
        r,c=map(int,input().split())
        s=[];
        for i in range(r): s.append([int(x) for x in input().split()])
        for i in range(c):
            ans=[]
            for j in s:
                ans.append(j[i])
            print(*ans,sep=' ')
except EOFError:
    pass
