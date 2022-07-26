'''
(url: https://zerojudge.tw/ShowProblem?problemid=d010)

內容
對一個正整數 N 而言，將它除了本身以外所有的因數加起來的總和為 S，
如果 S>N，則 N 為盈數，如果 S<N，則 N 為虧數，而如果 S=N，則 N 為完全數(Perfect Number)。
例如 10 的因數有 1、2、5、10，1+2+5=8<10，因此10 為虧數，而 12 的因數有 1、2、3、4、6、12，1+2+3+4+6=16>12，因此 12 為盈數。
至於 6 的因數有 1、2、3、6，1+2+3=6，所以 6 是完全數(它也是第一個完全數)。
現在請你寫一個程式，輸入一個正整數 N，然後印出它是盈數、虧數還是完全數。

輸入說明
輸出說明
範例輸入 #1
30
範例輸出 #1
盈數

範例輸入 #2
26
範例輸出 #2
虧數

範例輸入 #3
28
範例輸出 #3
完全數
'''
try:
    while True:
        n=int(input())
        ans=0
        for i in range(1,n):
            if n%i==0: ans+=i
        if ans>n: print("盈數")
        elif ans<n: print("虧數")
        elif ans==n: print("完全數")
except EOFError:
    pass
