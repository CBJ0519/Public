'''
(url: https://zerojudge.tw/ShowProblem?problemid=g275)

中文依照發音方式可以分為平聲與仄聲，假設我們把平聲標記為 0 而仄聲標記為 1

一個七言對聯包含兩個句子，每個句子包含恰好七個字

七言對聯有三個限制：
A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄
B: 仄起平收：第一句的結尾必須為仄聲，第二句的結尾必須為平聲
C: 上下相對：第一、二句的第二、四、六個字平仄必須不同
給你n組對聯，分別用 0, 1 代表平仄，請輸出它違反了哪幾條規則
若以上規則皆無違反，請輸出None

輸入說明
輸入一個正整數 n ( 1 <= n <= 30 ) 代表對聯數量，接下來有 2n 行，每行有 7 個數字，數字不是 0 就是 1

輸出說明
對於每個對聯，輸出一行表示它違反了哪些規則，若三個規則都遵守則輸出 None

'''
#code
n=int(input())
ans=''
for i in range(n):
    fir=[0]+[int(x) for x in input().split()]
    sec=[0]+[int(x) for x in input().split()]
    A=B=C=0
    result=''
    if fir[2]==fir[4] or fir[2]!=fir[6] or sec[2]==sec[4] or sec[2]!=sec[6]:
        A=1
    if fir[-1]!=1 or sec[-1]!=0:
        B=1
    if fir[2]==sec[2] or fir[4]==sec[4] or fir[6]==sec[6]:
        C=1
    if A==1:
        result+='A'
    if B==1:
        result+='B'
    if C==1:
        result+='C'
    if result=='':
        result+='None'
    ans+=result+'\n'
print(ans)
