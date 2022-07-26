'''
(url: https://zerojudge.tw/ShowProblem?problemid=f698)

內容
平常我們在寫運算式時習慣使用「中序表示法」(Infix Notation)，也就是把運算子放在兩個運算元中間，例如「3 + 4」。
1924 年一位波蘭的邏輯學家 Jan Łukasiewicz 發明了「前序表示法」(Prefix Notation)，它卻是把運算子放在運算元的前面，例如 「+ 3 4」。
儘管前序表示法並不符合人類的閱讀習慣，它的好處是不需要用到任何括號就可以清楚地指定運算的順序。比如說，在我們慣用的中序表示法裡：
1 + 2 × 3 = 7
因為會先算乘除再算加減。如果你要先算加減的話就得使用括號：
(1 + 2) × 3 = 9
但是如果使用前序表示法就不需要括號了：
+ 1 × 2 3 = 7
× + 1 2 3 = 9
前序表示法也稱作「波蘭表示法」(PN, Polish Notation)。
後來當電腦發明了以後，工程師們發現前序表示法在求值時耗用較多的記憶體，於是在 1954 年 Arthur Walter Burks 提出了「後序表示法」，
把運算子放在運算元的後面，一樣不需要括號就可以指定不同的運算順序：
1 2 3 × + = 7
1 2 + 3 × = 9
但是它只要使用「堆疊」就可以很簡單的完成求值動作。
後序表示法使用在 HP 於 1970 及 1980 年代所推出的所有電子計算器，甚至於 2020 年代的某些機型仍在使用。
也用在一些堆疊導向的程式語言，例如 Forth。
後序表示法也稱作「逆波蘭表示法」(RPN, Reverse Polish Notation) 或「波蘭後序表示法」(Polish Postfix Notation)。
現在，請你幫一個後序表示法運算式求值。

輸入說明
輸入只有一行，含有一個後序運算式。運算元為 32 位元有號整數，運算子包括 +, -, *, 及 /。所有的運算元及與運算子之間均以一個空白隔開。運算過程及結果也都是 32 位元有號整數。

輸出說明
輸出該運算式所求得的值。

範例輸入 #1
1 2 3 * +
範例輸出 #1
7
範例輸入 #2
1 2 + 3 *
範例輸出 #2
9
'''
s=[str(x) for x in input().split()]
stack=[]
for i in s:
    if len(i)>1 and i[0]=='-':
        stack.append(int(i))
    elif i.isdigit():
        stack.append(int(i))
    elif i=='+':
        a=int(stack.pop(-1))
        b=int(stack.pop(-1))
        stack.append(b+a)
    elif i=='-':
        a=int(stack.pop(-1))
        b=int(stack.pop(-1))
        stack.append(b-a)
    elif i=='*':
        a=int(stack.pop(-1))
        b=int(stack.pop(-1))
        stack.append(b*a)
    elif i=='/':
        a=int(stack.pop(-1))
        b=int(stack.pop(-1))
        stack.append(b//a)
print(stack[0])
