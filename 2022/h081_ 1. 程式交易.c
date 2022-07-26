/*
(url: https://zerojudge.tw/ShowProblem?problemid=h081)

內容
小明最近想要用程式做股票交易，給一個股票的歷史價格 a[1], a[2], ... , a[n] 他的投資策略如下
1. 同一個時間最多只會持有一張股票, 並會在時間點 1 花 a[1] 買進。
2. 若當下持有股票且該股票買進價格為 x，當遇到價格 y 大於等於 x+D 時即賣出，並轉得利潤 y-x。
3. 若當下沒有持有股票且上一次的賣出價格為 x，當遇到價格 y 小於等於 x-D 時則會買進股票。

輸出依照上述規則買賣後所得到的利潤和，若交易結束仍持有股票，則不考慮該股票買進的成本，直接無視該股票即可。

輸入說明
第一行輸入兩個正整數 n, D，接下來有 n 個正整數，代表每個時間點股票的價格。
數字範圍: 1 <= n <= 100, 1 <= D <= 100, 1 <= a[i] <= 100

輸出說明
輸出一個正整數，代表總利潤。

範例輸入 #1
3 10
50 20 45
範例輸出 #1
0

範例輸入 #2
6 10
30 20 45 38 10 20
範例輸出 #2
25
*/

#include<stdio.h>
int main(void){
    int have,now,profit=0,n,D,i,j,sell=0,price[101];
    scanf("%d%d",&n,&D);
    for(i=0;i<n;i++){
        scanf("%d",&price[i]);
    }
    have = price[0];
    now = 1;
    for(j=1;j<n;j++){
        if(now==1){
            if(price[j]>=(have+D)){
                profit+=(price[j]-have);
                sell = price[j];
                now = 0;
            }
        }else if(price[j]<=(sell-D)){
            have = price[j];
            now = 1;
        }
    }
    printf("%d\n",profit);
}
