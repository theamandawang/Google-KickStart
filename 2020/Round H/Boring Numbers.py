###TLE Error; this code is still not efficient enough
def isBoring(num):
    num = str(num)
    #string conversion makes accessing digits easier!
    for x in range(len(num)):
        if(int(num[x])%2 != (x+1)%2):
            return False
    return True
cases = int(input())
arr = []
for i in range(cases):
    arr.append(input())
    arr[i] = arr[i].split(' ')
    

for x in range(len(arr)):
    L = int(arr[x][0])
    R = int(arr[x][1])
    count = 0
    for z in range(L, R+1):
        if((isBoring(z))):
            count += 1
    print('Case #' + str(x+1) + ': ' + str(count))
            
            
            
