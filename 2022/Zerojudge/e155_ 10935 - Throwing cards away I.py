'''
(url: https://zerojudge.tw/ShowProblem?problemid=e155)

內容
給你一副照順序放好的紙牌，其中卡片的編號從1~n，且1號排在最上面，n號牌在最底下。
只要這副牌還有兩張以上，你就必須照以下的規則操作：
丟掉最上面的那張牌，然後把目前最上面的那張牌放到牌堆的最下面。
你的工作是找出每張牌被丟掉的順序，以及最後剩下的那張牌。

輸入說明
輸入的每一列包含一個整數 n≤50，當輸入為0時代表輸入結束，你不應該處理這個輸入。

輸出說明
對每個輸入的數字產生兩列輸出，第一列是每張牌被丟掉的順序，第二列則是剩下的那張牌。
任何一列都不應該有任何前置或尾隨的多餘空白，輸出細節請參考sample output。

範例輸入 #1
7
19
10
6
0
範例輸出 #1
Discarded cards: 1, 3, 5, 7, 4, 2
Remaining card: 6
Discarded cards: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14
Remaining card: 6
Discarded cards: 1, 3, 5, 7, 9, 2, 6, 10, 8
Remaining card: 4
Discarded cards: 1, 3, 5, 2, 6
Remaining card: 4
'''
while True:
    n=int(input())
    if n==0: break
    discarded=[]
    cards=list(range(1,n+1))
    while len(cards)>1:
        discarded.append(cards[0])
        cards.pop(0)
        tmp=cards[0]
        cards.pop(0)
        cards.append(tmp)
    print('Discarded cards:',end=' ')
    print(*discarded,sep=', ')
    print('Remaining card:',cards[0])
