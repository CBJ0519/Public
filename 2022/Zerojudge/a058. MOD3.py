'''
(url: https://zerojudge.tw/ShowProblem?problemid=a058)

內容
相信判斷一個數除以三的餘數是多少，對你來說應該沒有問題。那，如果一次請你判斷很多個數呢？
給你n個數字，請你輸出3k、3k+1、3k+2的數各有幾個

輸入說明
第一行有一個正整數n，代表接下來有幾個數字，
接著有n個介於1到50000之間的數字，請你做判斷

輸出說明
輸出三個數字(以空白隔開)，
分別為n個數字中，三的倍數、三的倍數+1、三的倍數+2的數量

範例輸入 #1
5
1
2
3
4
5
範例輸出 #1
1 2 2
'''
n=int(input())
a=[];x=y=z=0
for i in range(n): a.append(int(input()))
for j in a:
    if j%3==0: x+=1
    elif j%3==1: y+=1
    else: z+=1
print(x,y,z)
