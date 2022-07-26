/*
(url: https://zerojudge.tw/ShowProblem?problemid=i401)

一個雷射光從 (0,0) 向右邊發射，平面上有很多個鏡子，問雷射光會反射幾次，保證輸入沒有無限循環的情形。
鏡子用三個數字表示 (xi,yi,ti)，代表座標在 xi 上。ti=0 代表 / 這種擺放方式的鏡子，ti=1 代表 \ 這種擺放方式的鏡子，保證不會有一個位置有多個鏡子。

輸入說明
輸入一個正整數 n (1 <= n < 250000)，代表鏡子的數量，接下來有 n 行，第 i 行有三個數字 xi, yi 和 ti。

輸出說明
輸出雷射光共反射幾次。

範例輸入 #1
10
2 0 1
2 -1 1
7 -1 0
7 2 1
4 2 0
4 1 0
3 1 1
3 2 0
1 -1 1
1 4 0
範例輸出 #1
9

範例輸入 #2
4
2 1 0
5 -3 1
4 2 1
6 -2 0
範例輸出 #2
0

提示 ：
本題若使用遞迴實作，可能因為遞迴深度過深而造成執行時期錯誤。
範例測資一，見例圖。
範例測資二可以發現沒有任何 y=0 的鏡子，因此反射次數為 0。
*/

#include <stdio.h>
int n,ref=0;
int X[250000],Y[250000],T[250000];
int toright(int x, int y);
int todown(int x, int y);
int toup(int x, int y);
int toleft(int x, int y);

int toright(int x, int y){
    int lim=30001,index,i;
    for(i=0; i<n; i++){
        if(Y[i]==y && X[i]<lim && X[i]>x){
            lim = X[i];
            index = i;
        }
    }
    if(lim!=30001){
        ref+=1;
        if(T[index]==1) todown(lim,y);
        else toup(lim,y);
    }
    return 0;
}
int todown(int x, int y){
    int max=(-300001),index,i;
    for(i=0;i<n;i++){
        if(X[i]==x && Y[i]>max && Y[i]<y){
            max = Y[i];
            index = i;
        }
    }
    if(max!=(-300001)){
        ref+=1;
        if(T[index]==1) toright(x,max);
        else toleft(x,max);
    }
    return 0;
}
int toup(int x, int y){
    int lim=30001,index,i;
    for(i=0;i<n;i++){
        if(X[i]==x && Y[i]<lim && Y[i]>y){
            lim = Y[i];
            index = i;
        }
    }
    if(lim!=30001){
        ref+=1;
        if(T[index]==1) toleft(x,lim);
        else toright(x,lim);
    }
    return 0;
}
int toleft(int x,int y){
    int max=(-300001),index,i;
    for(i=0;i<n;i++){
        if(Y[i]==y && X[i]>max && X[i]<x){
            max = X[i];
            index = i;
        }
    }
    if(max!=(-300001)){
        ref+=1;
        if(T[index]==1) toup(max,y);
        else todown(max,y);
    }
    return 0;
}

int main()
{
    int i;
    scanf("%d",&n);
    for(i=0; i<n; i++)scanf("%d%d%d",&X[i],&Y[i],&T[i]);
    toright(0,0);
    printf("%d\n",ref);
    return 0;
}
