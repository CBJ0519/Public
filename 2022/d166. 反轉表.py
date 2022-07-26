'''
(url: https://zerojudge.tw/ShowProblem?problemid=d166)

內容
由1開始之連續數字a1.a2.a3...an相對有一反轉表：b1.b2...bm。
其bm代表意思為：數字m的位置前面有幾個比大個個數。
2 3 6 4 0 2 2 1 0
第1個2為1前面有2個比它大的數
第2個3為2前面有3個比它大的數
第3個6為3前面有6個比它大的數....以此類推
所以答案為
5 9 1 8 2 6 4 7 3
數字1前面有2個比它大的數 5 9
數字2前面有3個比它大的數 5 9 8

輸入說明
輸入的每一行含有一個由m個數所組成的數列(反轉表) 1<=m<=50，
單獨一個 -1 在一行代表測試資料的結束

輸出說明
請輸出從 1 到 m 所代表的數列

範例輸入 #1
2 3 6 4 0 2 2 1 0
-1
範例輸出 #1
5 9 1 8 2 6 4 7 3
'''
try:
  while True:
    s=[int(x) for x in input().split()]
    if s==[-1]: break
    ans=[0]*len(s)
    for i in range(len(s)): #0-8
      cnt=0
      for j in range(len(ans)): #0-8
        if ans[j]==0:
          cnt+=1
          if cnt==s[i]+1:
            ans[j]=i+1
    print(*ans,sep=" ")
except EOFError:
  pass
