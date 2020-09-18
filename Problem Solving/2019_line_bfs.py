from collections import deque

def solution_bfs() :

    answer = -1
    C, B = map(int, input().strip().split(' '))

    visit = [0 for _ in range(200001)]

    visit[B] = 1
    queue = deque([[C,B,0]])

    if C == B :
        answer = 0
        print(answer)
        return answer

    while queue : 
        
        now = queue.popleft()
        print(now)

        now_c = now[0]
        now_b = now[1]
        now_n = now[2]
    
        #종료조건
        if now_c == now_b:
            answer = now_n
            break

        nxt_b = 0
        nxt_n = now_n +1
        nxt_c = now_c + nxt_n


        # nxt_c 가 범위 안에 있는 경우만 넣음 queue 에
        if nxt_c <= 200000 :
            
            #1
            if now_b -1 >= 0  :
                nxt_b = now_b -1
                visit[nxt_b] = 1
                queue.append([nxt_c,nxt_b,nxt_n])

            #2
            if now_b +1 <= 200000  :
                nxt_b = now_b +1
                visit[nxt_b] = 1
                queue.append([nxt_c,nxt_b,nxt_n])

            
            #3
            if now_b *2 <= 200000 :
                nxt_b = now_b *2
                visit[nxt_b] = 1
                queue.append([nxt_c,nxt_b,nxt_n])
        
    print(answer)
    return answer 


solution_bfs()