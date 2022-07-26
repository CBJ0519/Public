/*
(url: https://zerojudge.tw/ShowProblem?problemid=c143)

題目說明 : https://ppt.cc/fNEzax@.png

輸入說明
測試資料第一列為土地的東西及南北單位長(1<n,m<=500)，第二列是共種幾排樹(1<=t<=500)。
以下每列分別為各排樹的起點及終點座標。
註：客戶給爺爺的各排座標有可能會重覆、重疊。

輸出說明
請輸出一整數，代表總共種了幾棵樹。

範例輸入 #1
7 8
8
2 8 6 8
4 7 2 5
6 7 4 5
1 5 1 7
7 7 7 5
6 4 2 4
2 3 4 1
6 3 4 1
範例輸出 #1
27
*/
#include <bits/stdc++.h>
#define N 501
using namespace std;
int t[N][N];
int main(){
    int n,m,row;
    cin>>n>>m>>row;
    int r1,c1,r2,c2;
    memset(t,0,sizeof(t));
    for(int i=0; i<row; i++){
        cin>>c1>>r1>>c2>>r2;
        int dr=r2-r1;
        int dc=c2-c1;
        if(dr>0) dr=1; else if(dr<0) dr=-1;
        if(dc>0) dc=1; else if(dc<0) dc=-1;
        
        t[r2][c2]=1;
    
        if (r1==r2){
            for (int c=c1;c!=c2;c+=dc){
                t[r1][c]=1;
            }
        }else{
            for(int r=r1,c=c1; r!=r2;r+=dr,c+=dc){
                t[r][c]=1;
            }
        }
    }
    int tsum=0;
    for(int r=1;r<=m;r++){
        for(int c=1;c<=n;c++){
            if (t[r][c]==1) tsum++;
        }
    }
    cout << tsum << "\n";
    return 0;
}
