'''
(url: https://zerojudge.tw/ShowProblem?problemid=g276)

內容
在一個 n*m 的棋盤上有 k 個魔王，一開始第 i 魔王會位在 (ri,ci) 的位置上，並且每回合會移動 (si,ti)。
也就是說，若本來在 (x,y) 位置，經過移動後會跳到 (x+si,y+ti) 位置。
每個魔王都有不同的 r,c,s,t 值，每回合每個魔王移動前會在所在位置上放下一顆炸彈，然後才進行移動，
而若魔王移動到已經被放有炸彈的位置，炸彈則會被引爆，該位置的魔王和炸彈則消失不見。
如果兩個魔王同時踏到同一個炸彈上會一起被炸掉，如果同一位置上有多個炸彈也會被一起引爆。
當魔王移動超出整個棋盤的範圍，則被視為消失
請計算，當棋盤上沒有任何魔王時，盤面上總共剩下幾格有炸彈?

輸入說明
第一行輸入三個正整數 n(1<=n<=100), m(1<=m<=100), k(1<=k<=500) 代表盤面大小為 n*m，上面一開始有 k 個魔王。
接下來有 k 行，第 i 行有四個整數 ri, ci, si, ti (0<=r<n, 0<=c<m)

輸出說明
輸出當場上沒有魔王的時候剩下幾格有炸彈

範例輸入 #1
1 6 3
0 0 0 0
0 2 0 -1
0 4 0 2
範例輸出 #1
4
範例輸入 #2
5 5 2
0 0 3 2
0 0 2 3
範例輸出 #2
3
'''
n,m,k=map(int,input().split())
mp=[]
for i in range(n):
    mp.append([0]*m);
data=[]
for i in range(k):
    data.append([int(x) for x in input().split()])
while True:
    if data==[]:
        break
    rm=[];clear=[]
    for i in data:
        mp[i[0]][i[1]]=1
    for i in data:
        newx=i[0]+i[2];newy=i[1]+i[3]
        i[0],i[1]=newx,newy
        if newx<0 or newy<0 or newx>=n or newy>=m:
            rm.append(i)
            continue
        if mp[newx][newy]==1:
            clear.append((newx,newy))
            rm.append(i)
    for i in rm:
        data.remove(i)
    for i,j in clear:
        mp[i][j]=0
ans=0
for i in mp:
    ans+=sum(i)
print(ans)
