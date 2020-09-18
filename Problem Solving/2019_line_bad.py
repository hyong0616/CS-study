def solution() :

    answer = -1
    C, B = map(int, input().strip().split(' '))

    visit = [0 for _ in range(200001)]

    #아예 처음부터 같은 경우 
    if C == B :
        answer = 0
        print(answer)
        return answer

    now_c = C
    now_b = B

    b_arr = [[now_b]]
    visit[now_b] = 1

    N = 1

    while now_c <=200000 : 
        #첫번째 시작부터 ~~~까지

        #C의 경우는 기존에서 N만큼 더 간거 
        now_c = now_c + N
        
        tmp_b= []

        #이전 단계에 있던 모든 B에 대해서 반복
        for item in b_arr[N-1] :
            now_b = item

            #B의 경우1
            if now_b -1 >= 0 and visit[now_b-1] ==0 :
                nxt_b = now_b -1
                visit[nxt_b] = 1
                tmp_b.append(nxt_b)

            #B의 경우2 
            if now_b +1 <= 200000 and visit[now_b+1] ==0 :
                nxt_b = now_b +1
                visit[nxt_b] = 1
                tmp_b.append(nxt_b)


            #B의 경우3
            if now_b *2 <=200000 and visit[now_b*2] ==0 :
                nxt_b = now_b *2
                visit[nxt_b] = 1
                tmp_b.append(nxt_b)

        b_arr.append(tmp_b)

        break_check = False

        #만난경우
        for item in b_arr[N] :
            if item == now_c :
                answer = N
                break_check = True
                break

        if break_check == True :
            break

        #브라운이 움직이지 못한 경우
        if not tmp_b :
            break

        

        N +=1

    print(answer)
    return answer



solution()