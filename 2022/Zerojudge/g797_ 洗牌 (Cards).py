'''
(url: https://zerojudge.tw/ShowProblem?problemid=g797)
題目說明: https://drive.google.com/file/d/12dZOptkaLW-wfk42TKZ9Q8zl2n76XgmE/view
'''
N,M = map(int,input().split())
init = [int(x) for x in input().split()]
while M>0:
    tmp = []
    for i in range(N//2):
        tmp.append(init[i])
        tmp.append(init[i+(N//2)])
    init = tmp
    M = M-1
for j in range(len(init)):
    if j==len(init)-1:
        print(init[j])
    else:
        print(init[j],"",end='')
