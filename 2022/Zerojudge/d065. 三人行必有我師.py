'''
(url: https://zerojudge.tw/ShowProblem?problemid=d065)

內容
文文和兩個同學最近喜歡在 ZeroJudge 上解題。
有一天他們看到了孔子說的：「三人行必有我師焉。」就吵了起來，因為他們每個人都認為自己是三個人之中的「老師」。
後來他們決定要比比看誰在 ZeroJudge 上的 AC 題數最多。

輸入說明
輸入只有一行，含有三個由空白所隔開的非負整數。

輸出說明
輸出這三個整數中最大的那一個。

範例輸入 #1
35 26 48
範例輸出 #1
48

範例輸入 #2
37 59 59
範例輸出 #2
59

提示 :
嘗試不要使用到max()函數
'''
s=[int(x) for x in input().split()]
max=s[0]
for i in s:
  if i>max: max=i
print(max)
