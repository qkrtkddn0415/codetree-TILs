N=int(input())
a_lst, b_lst= [0]*4, [0]*4
for _ in range(N):
    a, b = map(int,input().split())
    a_lst[a]+=1
    b_lst[b]+=1
mx=0
for i in range(1,4):
    mx=max(a_lst[i]-b_lst[i],mx)
    mx=max(b_lst[i]-a_lst[i],mx)
print(mx)