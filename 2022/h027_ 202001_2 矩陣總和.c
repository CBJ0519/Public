/*
(url: https://zerojudge.tw/ShowProblem?problemid=h027)

內容
矩陣是將一群元素整齊的排列成一個矩形，在矩陣中的橫排稱為列 (row)，直排稱為行 (column)，一個 n*m 的矩陣有 n 列 m 行，其中以 Xij 來表示矩陣 X 中的第 i 列第 j 行的元素。
在同樣大小的矩陣中，我們定義兩個矩陣的距離為兩矩陣中對應位置相同但值不相同的元素數量。
有一個 s*t 的小矩陣 A，和一個 n*m 的大矩陣 B，請計算 B 矩陣的子矩陣中，與 A 矩陣距離不超過 r 的子矩陣個數，並從這些距離 A 不超過 r 的子矩陣中，找到總和與 A 差異最小的值。

輸入說明
第一行有五個正整數 s，t，n，m 與 r。
接下來 s 行(line)每行包含 t 個數，第 i 行第 j 個數代表 Aij 的值。
接下來 n 行(line)每行包含 m 個數，第 i 行第 j 個數代表 Bij 的值。
同一行間數字以空格隔開。
 
輸出說明
輸出有兩行：
第一行輸出符合條件的子矩陣個數。
第二行輸出所有符合條件的子矩陣中，數字總和與相差最小的值，若找不到符合條件的子矩陣，則輸出。

範例輸入 #1
1 3 1 10 1
7 4 7
6 7 7 7 4 5 0 4 4 7
範例輸出 #1
3
2

範例輸入 #2
3 3 5 5 2
1 2 1
2 4 2
2 4 5
1 2 1 2 3
2 4 2 4 2
2 4 2 3 5
3 2 4 2 0
3 2 4 5 5
範例輸出 #2
3
1
*/
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
int main()
{
    int s,t,n,m,r,i,j,k,l,match=0,s_sum=0,mini=INT_MAX;
    scanf("%d%d%d%d%d",&s,&t,&n,&m,&r);
    int s_matrix[s][t];
    int b_matrix[n][m];
    for(i=0; i<s; i++){
        for(j=0; j<t; j++){
            scanf("%d",&s_matrix[i][j]);
            s_sum += s_matrix[i][j];
        }
    }
    for(i=0; i<n; i++){
        for(j=0; j<m; j++){
            scanf("%d",&b_matrix[i][j]);
        }
    }
    int row_start=0,row_end=s;
    for(; row_start<=n && row_end<=n; row_start++,row_end++){
        int col_start=0, col_end=t;
        for(; col_start<=m && col_end<=m; col_start++,col_end++){
            int b_sum=0,fail=0,brk=0;
            for(i=row_start,k=0; i<row_end && k<s; i++,k++){
                for(j=col_start,l=0; j<col_end && l<t; j++,l++){
                    if(b_matrix[i][j] != s_matrix[k][l]){
                        fail += 1;
                    }
                    if(fail>r){
                        brk=1;
                        break;
                    }
                    b_sum+=b_matrix[i][j];
                }
                if(brk==1){
                    break;
                }
            }
            if(brk==0){
                match+=1;
                if(abs(b_sum-s_sum)<mini){
                    mini = abs(b_sum-s_sum);
                }
            }
        }
    }
    if(mini==INT_MAX){
        mini=-1;
    }
    printf("%d\n%d\n",match,mini);
    return 0;
}
