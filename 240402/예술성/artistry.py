from collections import deque
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
group=[[0]*N for _ in range(N)]
group_members=[0]*(N*N+1)
narr=[[0]*N for _ in range(N)]

def bfs(i,j,group_num):
    q=deque()
    q.append((i,j))
    group[i][j]=group_num
    visited[i][j]=True
    cnt=1
    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ci][cj]==arr[ni][nj]:
                group[ni][nj]=group_num
                visited[ni][nj]=True
                q.append((ni,nj))
                cnt+=1
    return cnt
def make_group():
    for i in range(N):
        for j in range(N):
            group[i][j]=0
            visited[i][j]=0
    for i in range(N*N+1):
        group_members[i]=0
    group_num=0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group_num+=1
                group_member=bfs(i,j,group_num)
                group_members[group_num]=group_member
def cal_point():
    val=0
    for i in range(N):
        for j in range(N):
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=i+di,j+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=arr[i][j]:
                    val+=(group_members[group[i][j]]+group_members[group[ni][nj]])*arr[i][j]*arr[ni][nj]
    return val//2

def rotate():
    global arr
    for i in range(N):
        for j in range(N):
            narr[i][j]=0
    for i in range(N):
        for j in range(N):
            narr[N-j-1][i]=arr[i][j]    #모든 구간을 일단 회전
    for si,sj in ((0,0),((N//2)+1,0),(0,(N//2)+1),((N//2)+1,(N//2)+1)):
        for i in range(N//2):
            for j in range(N//2):
                narr[si+j][sj+N//2-i-1]=arr[si+i][sj+j]
    for i in range(N):
        for j in range(N):
            arr[i][j]=narr[i][j]

turn=0
ans=0
while turn<4:
    turn+=1
    #[1] 그룹 찾기
    make_group()
    #[2] 점수 계산
    ans+=cal_point()


    #[3] 회전
    if turn==4:
        break
    rotate()
print(ans)