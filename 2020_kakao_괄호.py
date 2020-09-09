def balancing(s):

    cnt1 = 0
    cnt2 = 0
    pos = 0

    for i in range (0,len(s)) :
        if s[i] == '(' :
            cnt1 = cnt1 + 1
        elif s[i] == ')' :
            cnt2 = cnt2 + 1

        if cnt1 == cnt2 :
            pos = i
            break

    u = s[:pos+1]
    v = s[pos+1:]
    return u, v

def correct_checking(s):

    answer = True
    cnt = 0

    for i in range (0,len(s)) :
        if s[i] == '(' :
            cnt = cnt + 1
        elif s[i] == ')' :
            cnt = cnt - 1

        if cnt < 0 :
            answer = False
            return answer

    return answer

def correcting(p_u, p_v):

    c_u = ''
    c_v = ''
    pv_u = ''
    pv_v  = ''
    answer = ''
    # P_U가 올바른 문자열일 경우
    if correct_checking(p_u):

        # P_V가 올바른 문자열일 경우
        if correct_checking(p_v):
            c_u = p_u
            c_v = p_v
            answer = c_u + c_v

        #p_v가 올바르지 않은 문자열일 경우
        else:
            pv_u, pv_v = balancing(p_v)
            c_u = p_u
            c_v = correcting(pv_u,pv_v)
            answer = c_u + c_v

    #P_U가 올바르지 않은 문자열일 경우
    else:

        #P_V가 올바른 문자열일 경우
        if correct_checking(p_v):

            c_v = p_v
            c_u = '(' + c_v + ')'

            for i in range(1,len(p_u)-1) :
                if p_u[i] == '(' :
                    c_u = c_u + ')'
                else :
                    c_u = c_u + '('

            answer = c_u

        #P_V가 올바르지 않은 문자열일 경우
        else:
            pv_u, pv_v = balancing(p_v)
            c_v = correcting(pv_u,pv_v)

            c_u = '(' + c_v + ')'

            for i in range(1, len(p_u) - 1):
                if p_u[i] == '(':
                    c_u = c_u + ')'
                else:
                    c_u = c_u + '('
            answer = c_u

    return answer


def solution(p):
    answer = ''

    if p != '' :
        p_u, p_v = balancing(p)
        #print(p_u,p_v)
        answer = correcting(p_u,p_v)

    print(answer)
    return answer

solution(")(")
