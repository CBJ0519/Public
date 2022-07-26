'''
(url: https://zerojudge.tw/ShowProblem?problemid=a227)

內容
河內之塔(Towers of Hanoi)是法國人M.Claus(Lucas)於1883年從泰國帶至法國的，河內為越戰時北越的首都，即現在的胡志明市；
1883年法國數學家 Edouard Lucas曾提及這個故事，據說創世紀時Benares有一座波羅教塔，是由三支鑽石棒（Pag）所支撐，
開始時神在第一根棒上放置64個由上至下依由小至大排列的金盤（Disc），
並命令僧侶將所有的金盤從第一根石棒移至第三根石棒，且搬運過程中遵守大盤子在小盤子之下的原則，
若每日僅搬一個盤子，則當盤子全數搬運完畢之時，此塔將毀損，而也就是世界末日來臨之時。

例圖 : https://ppt.cc/fzAb5x@.jpg

輸入說明
每行有一個正整數N ， N <= 15

輸出說明
請輸出把 A 上 N 個環移動到 C 的方法
( 剛開始A層最下方的Ring編號為N 最上方的編號為1 )

範例輸入 #1
1
2
3
範例輸出 #1
Move ring 1 from A to C

Move ring 1 from A to B
Move ring 2 from A to C
Move ring 1 from B to C

Move ring 1 from A to C
Move ring 2 from A to B
Move ring 1 from C to B
Move ring 3 from A to C
Move ring 1 from B to A
Move ring 2 from B to C
Move ring 1 from A to C
'''
def hanoi(s,e,n,nu=1):
    if n==1: 
        print(f"Move ring {nu} from {chr(65+s)} to {chr(65+e)}")
        return
    hanoi(s,3-(s+e),n-1)
    hanoi(s,e,1,n)
    hanoi(3-(s+e),e,n-1,n-1)
try:
    while True:
        hanoi(0,2,int(input()))
        print()
except EOFError:
    pass
