/*
(url: https://zerojudge.tw/ShowProblem?problemid=a249)

內容
有K個球從一完整二元樹（fully binary tree, FBT）的樹根（root）一個一個往下掉。
當這個球遇到非終端節點時，可能往左子樹跑，也可能往右子樹跑，如此直到這顆球到達終端節點（也就是樹葉）為止。
至於在非終端節點時球該往左或往右的決定乃是由2個值 true, false 來控制的。
如果這非終端節點的現在的值為 false，則球來的時候會往左子樹走，但是這個值會變為 true。
如果這非終端節點的現在的值為 true，則球來的時候會往右子樹走，但是這個值會變為 false。
請注意：一開始時所有非終端節點的值均為 false。
另外，在完整二元樹中所有的節點被依序編號，從上（深度 = 1）到下，由左到右。

請參考例圖 : https://ppt.cc/fPcU3x@.gif

舉例來說，例圖為深度為4的完整二元樹。
第一顆球往下掉會經過節點1、2、4最後落在節點8中。
第二顆球往下掉則會經過節點1、3、6最後落在節點12中。
第三顆球往下掉會經過節點1、2、5最後落在節點10中。
給你完整二元樹的深度D以及落下的第I個球，請你寫一個程式算出第I個球落在終端節點的編號。

輸入說明
輸入的第一列有一個整數，代表以下有幾組測試資料。
每組測試資料一列有2個整數D,I（2 <= D <= 20, 1 <= I <= 524288）。

輸出說明
對每組測試資料輸出一列，第I個球落在終端節點的編號。

範例輸入 #1
5
4 2
3 4
10 1
2 2
8 128
範例輸出 #1
12
7
512
3
255
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
    int T,D,I;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&D,&I);
        I--;
        int pos=1;
        for(int i=1;i<D;i++){
            if(I%2)pos=pos*2+1;
            else pos*=2;
            I>>=1;
        }
        printf("%d\n",pos);
    }
    return 0;
}