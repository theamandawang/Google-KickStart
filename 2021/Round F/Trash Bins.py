###TLE Error
def bins(can):
    #we can take a "math" approach to this problem
    #all the inputs for 'can' will be 1000011100011000 or some similar pattern
    #we have two types of runs, runs of 0s and runs of 1s.
    #distance for a house with a bin in front = 0 (disregard this in calculations)
    #only consider runs of 0s
    #if the run is odd, (for instance: 1000001) the distance for the 
    #0 houses, (left to right) are 1, 2, 3, 2, 1. or, 2*SUM(1 to runLength//2)+runLength//2+1
    
    #if the run is even, (for instance: 10000001) the distance for the 0 houses (left to right) are 1, 2, 3, 3, 2, 1
    #or 2*SUM(1 to runLength//2)
    
    #"edge" cases, where the 0 run is at the head or tail
    #take 00001 or 10000
    #then the distances are 1, 2, 3, 4 (for both), or SUM(1 to runLength)
    
    #I used the summation formula from math SUM(1 to n) = n(n+1)/2
    
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
