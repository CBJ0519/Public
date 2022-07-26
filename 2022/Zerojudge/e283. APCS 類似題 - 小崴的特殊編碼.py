'''
(url: https://zerojudge.tw/ShowProblem?problemid=e283)

內容
小崴要來玩編碼了~~!!! 這次，他打算跟你講很多字串! 
這些字串均經過特殊編碼的~~ 祝你全部解讀成功!
P.S. 編碼方式: 每個字串均只由 A~F 組成，
並由以下對照表將每一個字元轉換成長度為4的二元序列
A  -> 0 1 0 1
B  -> 0 1 1 1
C  -> 0 0 1 0
D  -> 1 1 0 1
E  -> 1 0 0 0
F  -> 1 1 0 0

輸入說明
多筆輸入!!!
每筆輸入 第一行有一個 正整數N 代表此字串的長度，
接下來有n行，每一行給一個字元經編碼後的序列 !
以EOF結束~~

輸出說明
多筆輸出!!!
輸出原始字串
記得空行歐~~

範例輸入 #1
1
0 1 0 1
1
0 0 1 0
2
1 0 0 0
1 1 0 0
4
1 1 0 1
1 0 0 0
0 1 1 1
1 1 0 1
範例輸出 #1
A
C
EF
DEBD
'''
from sys import stdin
d={'0 1 0 1':'A','0 1 1 1':'B','0 0 1 0':'C','1 1 0 1':'D','1 0 0 0':'E','1 1 0 0':'F'}
for read in stdin:
    read=int(read)
    ans=''
    for i in range(read):
        s=stdin.readline().strip()
        ans+=d[s]
    print(ans)
