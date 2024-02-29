lst=list(map(int,input().split()))
lst.sort()
if lst[0]+1==lst[1] and lst[1]+1==lst[2]:
    print('0')
else:
    mx=0
    mx=max(mx,lst[2]-lst[1]-1)
    mx=max(mx,lst[1]-lst[0]-1)
    print(mx)