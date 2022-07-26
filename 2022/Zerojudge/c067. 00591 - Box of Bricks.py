'''
(url: https://zerojudge.tw/ShowProblem?problemid=c067)

內容
3歲的小明喜歡玩他的方塊積木，他總是把方塊疊在一起形成高度不一的方塊堆。
然後他說：這是一面牆。5歲的姊姊小美聽到了就跟小明說：真正的牆高度應該要一樣才行。
小明聽了覺得有道理於是決定要搬動一些方塊使所有方塊堆的高度一樣。如例圖 https://ppt.cc/ftCpRx@.gif
由於小明是個懶惰的小孩，他想要搬動最小數目的方塊以達成這個目的，你能幫助他嗎？

輸入說明
輸入包含好幾組資料，每組資料有2行，第一行有一個數字n，代表有幾堆方塊。
第二行有n個數字分別代表這n堆方塊的高度hi。你可以假設1<=n<=50  1<=hi<=100
方塊的總數一定可以整除堆數n，也就是說一定可以使所有的方塊堆同樣高度。
如果輸入的n=0，代表輸入結束。 

輸出說明
對每一組輸入資料，首先輸出一行這是第幾組測試資料，下一行為"The minimum number of moves is k." 
k在這裡就是需搬動方塊最小的數目以使所有的方塊堆同一高度。
每組測試資料後亦請空一行。請參考Sample Output. 

範例輸入 #1
6
5 2 4 1 7 5
3
1 1 1
0
範例輸出 #1
Set #1
The minimum number of moves is 5.

Set #2
The minimum number of moves is 0.
'''
times=0
while True:
    times+=1
    ans=0
    if input()=='0': break
    hi=[int(x) for x in input().split()]
    average=sum(hi)//len(hi)
    for i in hi:
        if i>average: ans+=i-average
    print('Set #'+str(times))
    print('The minimum number of moves is '+str(ans)+'.')
