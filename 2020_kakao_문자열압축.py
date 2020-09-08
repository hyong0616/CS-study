def solution(s):
    s_len = len(s)
    answer = s_len

    max_range = int(s_len / 2)

    # i = 반복되는 문자 길이
    for i in range(1, max_range + 1):

        i_range = int(s_len / i)
        i_answer = s_len

        pos = 0
        cnt = 1
        check = 0
        while pos+i < s_len:

            # 현재 상태
            tmp_now = s[pos:pos+i]
            #다음 상태

            tmp_nxt = s[pos+i:pos+i+i]

            if tmp_now == tmp_nxt :
                cnt = cnt + 1
                if cnt == 2 :
                    i_answer = i_answer -i + 1
                elif cnt == 10 :
                    i_answer = i_answer -i + 1
                elif cnt == 100 :
                    i_answer = i_answer -i + 1
                elif cnt == 1000 :
                    i_answer = i_answer -i + 1

                else :
                    i_answer = i_answer -i
                #print(pos,cnt, tmp_now, tmp_nxt)
            else :
                cnt = 1

            pos = pos + i
            #print(pos)
        #i_answer = s_len - check

        if i_answer < answer:
            answer = i_answer
    print(answer)
    return answer

