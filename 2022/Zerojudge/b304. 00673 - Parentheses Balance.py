'''
(url: https://zerojudge.tw/ShowProblem?problemid=b304)

內容
在本題中，題目會先給你一個包含小括號（）及中括號〔〕的字串。
當字串符合下列條件時我們稱他為正確的運算式：

該字串為一個空字串
如果Ａ和Ｂ都為正確的運算式，則ＡＢ也為正確的運算式，
如果Ａ為正確的運算式，則（Ａ）及〔Ａ〕都為正確的運算式。
現在，請你寫一支程式可以讀入這類字串並檢查它們是否為正確的運算式。
字串的最大長度為128個字元。

輸入說明
輸入的第一列為正整數n，代表接下來有n列待測資料。

輸出說明
檢查每列待測資料，如果正確輸出Yes，否則輸出No。

範例輸入 #1
3
([])
(([()])))
([()[]()])()
範例輸出 #1
Yes
No
Yes
'''
input()
try:
    while True:
        s=[str(x) for x in input()]
        stack=[]; ok=True
        for i in s:
            if i=='(': stack.append('(')
            elif i=='[': stack.append('[')
            elif i==')':
                try:
                    if stack[-1]=='(': stack.pop(-1)
                    else:
                        ok=False
                        break
                except:
                    ok=False
                    break
            elif i==']':
                try:
                    if stack[-1]=='[': stack.pop(-1)
                    else:
                        ok=False
                        break
                except:
                    ok=False
                    break
        if ok and len(stack)==0: print('Yes')
        else: print('No')
except EOFError:
    pass
