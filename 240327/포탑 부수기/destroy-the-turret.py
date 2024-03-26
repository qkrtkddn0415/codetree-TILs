# import ---------------------------------  #
from collections import deque
# input ----------------------------------  #
N, M, K=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(N)]
# variables ------------------------------  #
turn=0
dxs,dys=[0,1,0,-1],[1,0,-1,0]
dxs2,dys2=[0,0,0,-1,-1,-1,1,1,1],[0,1,-1,0,1,-1,0,1,-1]
# ← ↓ → ↑ 
is_attacked=[[False]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]
last_attack=[[0]*M for _ in range(N)]
EMPTY=(-1,-1)
come=[[EMPTY]*M for _ in range(N)]
# functions ------------------------------  #
class Turret:
    def __init__(self, x, y, r, p):
        self.x=x
        self.y=y
        self.r=r
        self.p=p
    def __iter__(self):
        yield from [self.x,self.y,self.r,self.p]
def select_attacker():
    turret_list.sort(key=lambda x:(x.p,-x.r,-(x.x+x.y),-x.y))
    weak_turret=turret_list[0]
    x,y,_,_=weak_turret.__iter__()
    arr[x][y]+=N+M
    weak_turret.p=arr[x][y]
    last_attack[x][y]=turn
    weak_turret.r=last_attack[x][y]
    is_attacked[x][y]=True
    turret_list[0]=weak_turret

def laser_attack():
    weak_turret=turret_list[0]
    strong_turret=turret_list[-1]
    sx,sy,_,power=weak_turret.__iter__()
    ex,ey,_,_=strong_turret.__iter__()

    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    flag=False
    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            flag=True
            break
        for dx,dy in zip(dxs,dys):
            nx,ny=(x+dx+N)%N,(y+dy+M)%M
            if not visited[nx][ny] and arr[nx][ny]!=0:
                q.append((nx,ny))
                come[nx][ny]=(x,y)
                visited[nx][ny]=True
    if flag:
        arr[ex][ey]=max(0,arr[ex][ey]-power)
        is_attacked[ex][ey]=True

        tx,ty=come[ex][ey]
        while tx!=sx or ty!=sy:
            arr[tx][ty]=max(0,arr[tx][ty]-power//2)
            is_attacked[tx][ty]=True
            tx,ty=come[tx][ty]
    return flag

def bomb_attack():
    weak_turret=turret_list[0]
    strong_turret=turret_list[-1]
    sx,sy,_,power=weak_turret.__iter__()
    ex,ey,_,_=strong_turret.__iter__()
    for dx,dy in zip(dxs2,dys2):
        nx,ny=(ex+dx+N)%N, (ey+dy+M)%M
        if sx==nx and sy==ny:
            continue
        if nx==ex and ny==ey:
            arr[nx][ny]=max(0,arr[nx][ny]-power)
            is_attacked[nx][ny]=True
        else:
            arr[nx][ny]=max(0,arr[nx][ny]-power//2)
            is_attacked[nx][ny]=True
        
def repair():
    for i in range(N):
        for j in range(M):
            if not is_attacked[i][j] and arr[i][j]!=0:
                arr[i][j]+=1
                
def init():
    for i in range(N):
        for j in range(M):
            is_attacked[i][j]=False
            visited[i][j]=False
            come[i][j]=EMPTY
            if arr[i][j]:
                new_turret=Turret(i,j,last_attack[i][j],arr[i][j])
                turret_list.append(new_turret)
# output ---------------------------------  #
for _ in range(K):
    #[0] 턴 증가]
    turn+=1
    turret_list=[]
    init()
    if len(turret_list)<2:
        break
    #[1]공격자 선정
    select_attacker()
    #[2]공격자 공격
        #[2-1] 레이저 공격
    is_succ=laser_attack()
    if not is_succ:
        #[2-2] 안 되면 포탄 공격
        bomb_attack()
    #[3] 공격에 참여하지 않은 포탑 수리
    repair()

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, arr[i][j])
print(ans)