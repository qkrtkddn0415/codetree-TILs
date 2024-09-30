K,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(5)]
lst=list(map(int,input().split()))
ans=[]

def rotate(arr,si,sj):
    narr=[x[:] for x in arr]    #deepcopy보다 빠름
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j]=arr[si+3-j-1][sj+i]
    return narr

def count(arr,clr):     #해당 배열을 회전시켰을 때, 얻을 수 있는 점수의 최대 합을 계산
    v=[[0]*5 for _ in range(5)]
    cnt=0
    for i in range(5):
        for j in range(5):
            if v[i][j]==0:
                t=bfs(arr,v,i,j,clr)
                cnt+=t
    return cnt

def bfs(arr,v,i,j,clr):
    q=[]
    q.append((i,j))
    cnt=0
    sset=set()

    v[i][j]=1
    sset.add((i,j))
    cnt+=1
    while q:
        ci,cj=q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<5 and 0<=nj<5 and arr[ci][cj]==arr[ni][nj] and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=1
                sset.add((ni,nj))
                cnt+=1
    if cnt>=3:
        if clr==1:
            for i,j in sset:
                arr[i][j]=0
        return cnt
    else:
        return 0

for _ in range(K):#[0] K턴만큼 수행
    mx_cnt=0                #매 턴마다 mx_cnt갯수를 초기화, 해당 턴동안 유물을 얻을 수 없으면 break
    #[1] 탐사 진행.           해당 턴에서, 가장 많은 유물을 획득할 수 있는 곳을 찾음.
    for rot in range(1,4):          #회전한 각도가 가장 작고
        for sj in range(0,3):       #회전한 열이 가장 작고
            for si in range(0,3):   #회전한 행이 가잔 작은 배열을 고름
                narr=[x[:] for x in arr]    #deepcopy보다 빠름
                for _ in range(rot):     #해당 구간을 rot회만큼 회전시켜줘야 함
                    narr=rotate(narr,si,sj) #narr의 si, sj를 기준으로 rot회만큼 회전
                #[1-1]획득된 유물이 가장 많은 구간을 찾음
                t=count(narr,0)   #이 구간을 rot회만큼 회전시켰을 때의, 가장 많은 점수를 일단 확인함
                if mx_cnt<t:        #만약, 이전보다 더 많은 점수를 획득할 수 있는 구간이라면, 점수를 얻고 해당 배열을 저장함.
                    mx_cnt=t    
                    marr=narr
    if mx_cnt==0:                   #만약, 해당 턴에서 얻을 수 있는 유물 점수가 없는 경우, 종료함
        break
    #[2] 연쇄 획득. 해당 배열에서 점수를 획득하고, 이제 점수를 획득한 곳을 비워주고, 블록 배열에서 블록을 불러와서 다시 채워줌.
    arr=marr
    cnt=0
    while True:
        t=count(arr,1)  #해당 배열에서 값을 얻을 수 있는지 확인함. 만약, 값을 얻을 수 있다면, 해당 유물 칸에 빵꾸 내줌
        if t==0:
            break           #만약, 값을 얻을 수 없다면, 연쇄 획득 단계를 종료함
        cnt+=t              #얻을 수 있는 값을 넣어줌
        for j in range(5):  #열 번호가 작은 순으로, 행 번호가 큰 순으로 조각을 채움
            for i in range(4,-1,-1):
                if arr[i][j]==0:
                    arr[i][j]=lst.pop(0)
    ans.append(cnt)         #이번 턴에서 획득할 수 있는 점수의 총 합을 정답 배열에 넣어줌
#[3] 모든 탐사가 끝나면, 정답 배열에 담긴 값을 출력함.
print(*ans)