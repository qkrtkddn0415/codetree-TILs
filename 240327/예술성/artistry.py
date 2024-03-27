from collections import deque

N=int(input())
arr=[list(map(int,input().split()))for _ in range(N)]
visited=[[0]*N for _ in range(N)]
M=(N)//2
narr=[[0]*N for _ in range(N)]
group=[0]*(N*N+1)

def bfs(i,j,group_num):
    cnt=1
    q=deque()
    q.append((i,j))
    visited[i][j]=group_num
    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj]==arr[ci][cj]:
                cnt+=1
                visited[ni][nj]=group_num
                q.append((ni,nj))
    return cnt
ans=0
for k in range(1,4):
    #[0] 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j]=0
            narr[i][j]=0
    for i in range(N*N+1):
        group[i]=0
    score=0
    #[1] 그룹 만들기
    group_num=0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group_num+=1
                cnt=bfs(i,j,group_num)
                group[group_num]=cnt                                                                                                                                                          
    #[2] 점수계산하기
    for i in range(N):
        for j in range(N):  
            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<N and 0<=nj<N and arr[i][j]!=arr[ni][nj]:
                    score+=(group[visited[i][j]]+group[visited[ni][nj]])*(arr[i][j])*(arr[ni][nj])
    ans+=score//2
        
    if k>3:
        break
    #[3] 회전하기
    for i in range(N):
        narr[M][i]=arr[i][M]
    for j in range(N):
        narr[j][M]=arr[M][M-j-1]
    for si,sj in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j]=arr[si+M-j-1][sj+i]
    arr=narr

print(ans)