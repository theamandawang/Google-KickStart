### Full points
cases = int(input())
arr = []
for i in range(cases):
    arr.append(input())
    arr[i] = arr[i].split(' ')
    #each row of arr is the respective case number's N, K, and S values

for x in range(len(arr)):
    N = int(arr[x][0])
    K = int(arr[x][1])
    S = int(arr[x][2])
    #basic algebra
    #must find minimum time
    #option 1: going backwards from K to S, solving S,
    #and then returning from S to K, and then back to N
    #so we traverse the distance (K-S) twice (going K->S, then S->K)
    #must also count going from 1 to K (or K), and K to N (N-K)
    #therefore we get K+2*(K-S) + N
    
    #option 2: restarting the game from level 1. 
    #N-0 (restarting the game)+ K (original time spent)
    #therefore, N+K
    time = min(2*(K-S) + N, N + K)
    print('Case #' + str(x+1) + ': ' + str(time))
