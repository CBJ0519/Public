/*
(url: https://zerojudge.tw/ShowProblem?problemid=c290)

內容
問題描述

將一個十進位正整數的奇數位數的和稱為A ，偶數位數的和稱為B，則A與B的絕對差值 |A －B| 稱為這個正整數的秘密差。
例如： 263541 的奇數位和 A = 6+5+1 =12，偶數位的和 B = 2+3+4 = 9 ，所以 263541 的秘密差是 |12 －9|= 3 。
給定一個 十進位正整數 X，請找出 X的秘密差。

原題 : https://ppt.cc/fepBpx@.png

輸入說明
輸入為一行含有一個十進位表示法的正整數X，之後是一個換行字元。

輸出說明
請輸出 X的秘密差 Y(以十進位表示法輸出 )，以換行字元結尾 。

範例輸入 #1
263541
範例輸出 #1
3

範例輸入 #2
131
範例輸出 #2
1

提示 ：
（說明） 263541 的 A = 6+5+1= 12 , B = 2+3+4 =9 ，|A－B|=|12－9|= 3。
（說明） 131 的 A = 1+1= 2, B = 3，|A－B|= |2－3|= 1。
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
    int a=0,b=0;
    string x;
    cin>>x;
    for(int i=0;i<x.size();i++){
        if (i%2) a+=(int)x[i]-48;
        else b+=(int)x[i]-48;
    }
    cout<<abs(a-b);
}
