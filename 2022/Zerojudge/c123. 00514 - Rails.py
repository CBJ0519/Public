'''
(url: https://zerojudge.tw/ShowProblem?problemid=c123)

內容
在一個叫「堆疊市」的城市中有一個有名的火車站。
由於地形限制以及經費的關係，火車站及唯一的鐵路的樣子如下圖：
現在火車從A方向來，預定從B方向離開。
火車共有N節車廂（N <=1000），並且各車廂依次以1到N來編號。
你可以假設各車廂在進站之前可以單獨與其他車廂分離，也可以單獨離開車站到往B方向的鐵軌上。
你也可以假設在任何時間火車站都可以容納所有的車廂。
但是一旦一節車廂進站後，就不能再回到A方向的鐵軌上了，並且一旦離開車站往B方向後，也不能再回到車站。
現在你的任務是寫一個程式，判斷火車能否以一特定的排列方式在B方向的鐵軌上。

例圖 : https://ppt.cc/fBBmNx@.gif

輸入說明
輸入含有多組測試資料。每組測試資料的第一列，有1個整數N，其意義如上所述。
對於此組測試資料接下來有0到多個不等的測試，每個測試一列，每列有N個整數，內容為1,2,......,N的任意排列。
當遇到僅含有一個0的一列，代表該組測試資料結束。
N=0代表輸入結束，請參考Sample Input。

輸出說明
對每一組測試資料的每個測試，輸出該1,2,......,N的任意排列是否可能。
如果可能，請輸出yes，若不可能則輸出No。
每組測試資料後亦請空一列。請參考Sample Output。

範例輸入 #1
5
1 2 3 4 5
5 4 3 2 1
5 4 1 2 3
0
7
4 5 3 7 6 2 1
0
0
範例輸出 #1
Yes
Yes
No

Yes
'''
while True:
    n=int(input())
    if n==0: break
    while True:
        expect=[int(x) for x in input().split()]
        if expect==[0]: break
        station=[]
        train=list(range(1,n+1))
        while expect!=[]:
            if station==[]:
                station.append(train[0])
                train.pop(0)
            else:
                if station[-1]==expect[0]:
                    expect.pop(0)
                    station.pop()
                elif train!=[]:
                    station.append(train[0])
                    train.pop(0)
                    if station[-1]==expect[0]:
                        expect.pop(0)
                        station.pop()
                else: break
        if station==[]: print('Yes')
        else: print('No')
    print()
