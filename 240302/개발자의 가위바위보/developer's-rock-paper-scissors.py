N=int(input())
arr=[]
for _ in range(N):
    a,b=map(int,input().split())
    arr.append((a,b))
win=mx=0
for a,b in arr:
    if a==1 and b==2:
        win+=1
    elif a==2 and b==3:
        win+=1
    elif a==3 and b==1:
        win+=1
mx=max(mx,win)
win=0
for a,b in arr:
    if a==3 and b==2:
        win+=1
    elif a==2 and b==1:
        win+=1
    elif a==1 and b==3:
        win+=1
mx=max(mx,win)
print(mx)