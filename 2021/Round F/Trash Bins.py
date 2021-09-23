###TLE Error
def bins(can):
    dis = 0
    run = 0
    for c in range(len(can)):
        if(c == len(can) - 1 and can[c]=='0'):
            run+=1
            dis = dis + run*(run+1)/2
            run = 0
        elif(c == can.index('1') and c != 0):
            dis = dis + run*(run+1)/2
            run = 0
        elif(can[c] == '1'):
            if(run%2 ==0):
                dis = dis + run/2*(run/2+1)
            else:
                dis = dis + (run//2+1)*(run//2+2) - (run//2+1)
            run = 0
        else:
            run += 1
    return str(int(dis))

t = int(input())
can = []
for x in range(t):
    input()
    can.append(input())
    print('Case #' + str(x+1) + ': ' + bins(can[x]))
