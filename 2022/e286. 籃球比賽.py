'''
(url: https://zerojudge.tw/ShowProblem?problemid=e286)

內容
APCS國辦了一場籃球聯賽，其中的每一場有主隊與客隊。
你的任務是將每一場比賽的資訊做成簡訊輸出。

輸入說明
單筆輸入
共有四行數字，代表兩場比賽
每行有四個數字，代表四局的分數
第一行代表主隊在第一場比賽中四局的分數
第二行代表客隊在第一場比賽中四局的分數
第三行代表主隊在第二場比賽中四局的分數
第四行代表客隊在第二場比賽中四局的分數
所有數字都介於 0 ~ 100 之間

輸出說明
對每一場比賽輸出主隊與客隊的比數
最後輸出兩場比賽的勝敗情況
如果主隊贏了兩場輸出 "Win"
如果客隊贏了兩場輸出 "Lose"
平手則輸出 "Tie"
保證不會有同分狀況出現，每場都會分出勝負

範例輸入 #1
87 87 87 87
78 78 78 78
87 87 87 87
78 78 78 78
範例輸出 #1
348:312
348:312
Win
'''
win=0
try:
    for i in range(2):
        s=sum([int(x) for x in input().split()])
        t=sum([int(x) for x in input().split()])
        if s>t: win+=1
        print(f"{s}:{t}")
    if win==0: print('Lose')
    elif win==1: print('Tie')
    elif win==2: print('Win')
except EOFError:
    pass
