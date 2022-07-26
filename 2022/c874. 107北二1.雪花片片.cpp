/*
(url: https://zerojudge.tw/ShowProblem?problemid=c874)

Koch 曲線是瑞典數學家 Helge von Koch 於 1904 年提出來的。它是一種碎形，其形態似雪花，又稱 Koch 雪花曲線。
一開始給定一個等邊三角形，如例圖 N = 1 所示，它含有三個等長的線段。
接下來 N = 2 的 Koch 曲線可以由以下步驟生成：
將接觸外面的每個線段平分成三等份的較小線段。
以中間那一個較小線段為底，向外畫出一個等邊三角形。
此時 N = 2 共有 4 個等邊三角形（1 個大的、3 個小的），如例圖所示。
繼續以上的步驟，N = 3 時共有大大小小的16個等邊三角形。N = 4 時可依此類推。
現在要請你寫一個程式，輸入 N ，求出從 1 開始直到 N，所對應的等邊三角形的總數量。

例圖 : https://ppt.cc/frPFJx@.jpg

輸入說明
測試資料只有一行，只有一個數字 N，其值為 1 至 120 的整數。

輸出說明
輸出資料為一個正整數，表示從 1 開始直到 N ，所對應的等邊三角形的總數量。
下面輸入範例一的輸入 N = 2，其等邊三角形的總數量為 1 + 4 = 5。
而輸入範例二的輸入 N = 3，等邊三角形的總數量為 1 + 4 + 16 = 21。

範例輸入 #1
2
3
範例輸出 #1
5
21
*/
#include<bits/stdc++.h>
using namespace std;
int s[75];
void power(int n){
    int i,j,carry;
    for(i=0;i<n;i++){
        carry=0;
        for(j=0;j<75;j++){
            s[j]=s[j]*4+carry;
            carry=s[j]/10;
            s[j]=s[j]%10;
        }
    }
}
void divide(int n){
    int i,carry=0;
    for(i=74;i>=0;i--){
        s[i]+=carry*10;
        carry=s[i]%n;
        s[i]=s[i]/n;
    }
}
int main(){
    int n;
    while(cin>>n){
        int i;
        bool B=true;
        memset(s,0,sizeof(s));
        s[0]=1;
        power(n);
        s[0]-=1;
        divide(3);
        for(i=74;i>=0;i--){
            if(s[i]==0 && B)continue;
            B=false;
            cout<<s[i];
        }
        cout<<"\n";
    }
    return 0;
}
