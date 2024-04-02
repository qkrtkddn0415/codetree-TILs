from collections import deque
N,M=map(int,input().split())#격자 크기, 사람 수
arr=[list(map(int,input().split())) for _ in range(N)]
cvs_list=[]
for i in range(M):
    x,y=map(int,input().split())
    cvs_list.append((x-1,y-1))
visited=[[False]*N for _ in range(N)]
EMPTY=(-1,-1)
people=[EMPTY]*M
step=[[0]*N for _ in range(N)]

# 코드트리 빵 : 정확히 1분에 1명씩 1칸을, 각자가 원하는 편의점으로 최단거리로 이동
# 순차적으로 처리하고, 모든 사람이 이동한 후에 해당 위치는 움직일 수 없는 칸으로 바꿔줘야 함.
# 방향에 우선순위 있음. 최단거리로만 이동해야 함.
# [1] 격자 내, 모든 사람, 가고싶은 편의점에 가장 가까워지는 방향으로 1칸 이동, 상좌우하
# [2] 편의점 도착시, 멈춤. 모든 사람이 다 돌면 해당 칸을 정지로
# [3] t>M 인 경우, continue 처리
# [4] 아닌 경우, 가고싶은 편의점과 가장 가까운 베이스캠프로 이동시켜줌.
# [5] 모든 사람이 편의점에 도착하면 종료(어떤 사람이 편의점에 도착하지 못하는 경우는 없음)
def move():
    for i in range(M):
        if people[i]==EMPTY or people[i]==cvs_list[i]:
            continue
        px,py=people[i]
        bfs(cvs_list[i])
        min_dist=100000
        min_x,min_y=-1,-1
        for dx,dy in ((-1,0),(0,-1),(0,1),(1,0)):#상좌우하
            ni,nj=px+dx,py+dy
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] and min_dist>step[ni][nj]:
                min_dist=step[ni][nj]
                min_x,min_y=ni,nj
        people[i]=(min_x,min_y)
        if people[i]==cvs_list[i]:
            arr[min_x][min_y]=2
    if turn>M:
        return
    bfs(cvs_list[turn-1])
    min_dist=100000
    min_x,min_y=-1,-1
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1 and visited[i][j] and min_dist>step[i][j]:
                min_dist=step[i][j]
                min_x,min_y=i,j
    people[turn-1]=(min_x,min_y)
    arr[min_x][min_y]=2
def finished():
    for i in range(M):
        if cvs_list[i]!=people[i]:
            return False
    return True

def bfs(start_pos):
    for i in range(N):
        for j in range(N):
            visited[i][j]=0
            step[i][j]=0
    si,sj=start_pos
    q=deque()
    q.append((si,sj))
    visited[si][sj]=True

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(0,-1),(0,1),(1,0)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj]!=2:
                visited[ni][nj]=True
                step[ni][nj]=step[ci][cj]+1
                q.append((ni,nj))

turn=0
while True:
    turn+=1
    move()
    if finished():
        break
# [6] 편의점에 도착한 시간을 출력
print(turn)