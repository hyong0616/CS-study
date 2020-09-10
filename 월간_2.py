def solution(n):
    answer = []

    for i in range (0,n) :
        tmp = [0 for _ in range(i+1)]
        answer.append(tmp)

    #반복되는 열 수

    n_range = n-1

    #넣어야하는 수
    cnt = 1
    cnt_range =0

    if n == 1 :
        answer[0] = 1
        return answer

    # i = 반복해야하는 횟수
    for i in range(n_range,-1,-3) :
        #아래로 내려가는 방향
        start_x = cnt_range *2
        start_y = cnt_range *1
        if i == 0 :
            answer[start_x][start_y] = cnt
        for k in range(0,i) :
            answer[start_x+k][start_y] = cnt
            cnt = cnt +1

        #옆으로 가는 방향
        start_x = start_x + i
        for k in range(0,i) :
            answer[start_x][start_y+k] = cnt
            cnt = cnt+1

        #대각선 방향
        start_y = start_y + i

        for k in range(0,i) :
            answer[start_x-k][start_y-k] = cnt
            cnt = cnt+1
        cnt_range = cnt_range +1

    res = []
    for i in answer:
        res += i

    answer = res

    return answer
