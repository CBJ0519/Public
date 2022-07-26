'''
(url: https://zerojudge.tw/ShowProblem?problemid=a005)

內容
Eva的家庭作業裏有很多數列填空練習。
填空練習的要求是：已知數列的前四項，填出第五項。
因為已經知道這些數列只可能是等差或等比數列，她決定寫一個程式來完成這些練習。

輸入說明
第一行是數列的數目t（0 <= t <= 20）。 
以下每行均包含四個整數，表示數列的前四項。 
約定數列的前五項均為不大於105的自然數，等比數列的比值也是自然數。

輸出說明
對輸入的每個數列，輸出它的前五項。

範例輸入 #1
2
1 2 3 4
1 2 4 8
範例輸出 #1
1 2 3 4 5
1 2 4 8 16
'''
n = int(input())
for i in range(n):
    T = [int(x) for x in input().split()]
    k = [T[3]-T[2],T[3]//T[2]]
    if T[2]-T[1]==k[0] and T[1]-T[0]==k[0]:
        T.append(T[3]+k[0])
    else:        
        T.append(T[3]*k[1])
    for j in T:
        print(j,end=' ')
    print()
