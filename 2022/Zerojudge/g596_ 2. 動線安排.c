/*
(url: https://zerojudge.tw/ShowProblem?problemid=g596)

內容
你是一個遊樂園展場的管理員，展場是一個 m*n 的矩形，可以使用木樁和線來排動線，你可以有兩種操作:
加入木樁 r c 0
加一木樁在(r,c), 並且向他的上下左右盡量找離最近的木樁連線, 題目保證 (r,c) 上一定沒有木樁, 若 (r,c) 有線經過則先將那些線拆掉後再來連線
移除木樁 r c 1
(r,c) 拔木樁, 並把他的線也拔掉, 保證 (r,c) 上一定有木樁
總共有 h 次操作，輸出過程中有線和有木樁佔據空間的面積最大是多少, 以及 h 次操作後有線和有木樁佔據空間的面積

輸入說明
第一行輸入三個正整數 m, n 和 h 代表展場範圍是 m*n, 並且有 h 筆操作。
接下來會有 h 行，每一行都有三個非負整數 r, c, t，代表在位置 (r,c) 執行操作 t

輸出說明
輸出兩個數字
第一個數字表示，操作過程中有線和有木樁佔據空間的面積最大值
第二個數字表示，操作結束後有線和有木樁佔據空間的面積

範例輸入 #1
3 5 6
0 0 0
0 2 0
2 2 0
2 0 0
2 4 0
2 2 1
範例輸出 #1
10
6

範例輸入 #2
5 5 7
2 2 0
2 4 0
4 4 0
4 0 0
0 3 0
4 3 0
4 3 1
範例輸出 #2
12
7
*/
#include <stdio.h>
int m,n;
char exh[100][100]={};
int lead(int x,int y){
    int cur_area=0;
    int i,j;
    char now;
    for(i=y-1;i>=0;i--){
        now = exh[x][i];
        if(now=='-')break;
        else if(now=='@'){
            for(j=i+1;j<y;j++){
                now = exh[x][j];
                if(now=='\0'){
                    exh[x][j]='-';
                    cur_area+=1;
                }
                else if(now=='|')exh[x][j]='#';
            }
            break;
        }
    }
    for(i=x-1;i>=0;i--){
        now = exh[i][y];
        if(now=='|')break;
        else if(now=='@'){
            for(j=i+1;j<x;j++){
                now = exh[j][y];
                if(now=='\0'){
                    exh[j][y] = '|';
                    cur_area+=1;
                }
                else if(now=='-')exh[j][y] = '#';
            }
            break;
        }
    }
    for(i=y+1;i<n;i++){
        now = exh[x][i];
        if(now=='-')break;
        else if(now=='@'){
            for(j=i-1;j>y;j--){
                now = exh[x][j];
                if(now=='\0'){
                    exh[x][j] = '-';
                    cur_area+=1;
                }
                else if(now=='|')exh[x][j] = '#';
            }
            break;
        }
    }
    for(i=x+1;i<m;i++){
        now = exh[i][y];
        if(now=='|')break;
        else if(now=='@'){
            for(j=i-1;j>x;j--){
                now = exh[j][y];
                if(now=='\0'){
                    exh[j][y] = '|';
                    cur_area+=1;
                }
                else if(now=='-')exh[j][y] = '#';
            }
            break;
        }
    }
    return cur_area;
}
int tear(int x,int y){
    int i,j,cur_area=0;
    char now;
    for(i=y-1;i>=0;i--){
        now = exh[x][i];
        if(now=='@'){
            for(j=i+1;j<y;j++){
                now = exh[x][j];
                if(now=='-'){
                    exh[x][j]='\0';
                    cur_area-=1;
                }
                else if(now=='#'){
                    exh[x][j]='|';
                }
            }
            break;
        }
    }
    for(i=y+1;i<n;i++){
        now = exh[x][i];
        if(now=='@'){
            for(j=i-1;j>y;j--){
                now = exh[x][j];
                if(now=='-'){
                    exh[x][j]='\0';
                    cur_area-=1;
                }
                else if(now=='#'){
                    exh[x][j]='|';
                }
            }
            break;
        }
    }
    for(i=x-1;i>=0;i--){
        now = exh[i][y];
        if(now=='@'){
            for(j=i+1;j<x;j++){
                now = exh[j][y];
                if(now=='|'){
                    exh[j][y]='\0';
                    cur_area-=1;
                }
                else if(now=='#'){
                    exh[j][y]='-';
                }
            }
            break;
        }
    }
    for(i=x+1;i<m;i++){
        now = exh[i][y];
        if(now=='@'){
            for(j=i-1;j>x;j--){
                now = exh[j][y];
                if(now=='|'){
                    exh[j][y]='\0';
                    cur_area-=1;
                }
                else if(now=='#'){
                    exh[j][y]='-';
                }
            }
            break;
        }
    }
    return cur_area;
}
int main()
{
    int h,max_area=0,cur_area=0;
    scanf("%d%d%d",&m,&n,&h);
    while(h--){
        int x,y,t;
        scanf("%d%d%d",&x,&y,&t);
        if(t==0){
            if(exh[x][y]=='-' || exh[x][y]=='|'){
                cur_area+=tear(x,y);
                cur_area+=lead(x,y);
            }
            else if(exh[x][y]=='\0'){
                cur_area+=1;
                cur_area+=lead(x,y);
            }
            exh[x][y]='@';
        }
        else if(t==1){
            exh[x][y]='\0';
            cur_area-=1;
            cur_area+=tear(x,y);
        }
        if(cur_area>max_area)max_area=cur_area;
    }
    printf("%d\n",max_area);
    printf("%d\n",cur_area);
    return 0;
}
