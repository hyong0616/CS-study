def solution(a):
    answer = 0


    min_arr = [0 for _ in range(len(a))]

    for i in range (len(a)-1,-1,-1):
        if i == len(a)-1 :
            min_arr[i] = a[i]

        else :
            if a[i] < min_arr[i+1]:
                min_arr[i] = a[i]
            else :
                min_arr[i] = min_arr[i+1]

    min_left = a[0]
    min_right = min(a)
    min_idx = a.index(min(a))

    for i in range(0,len(a)) :

        if i == 0 or i == (len(a)-1):

            answer +=1
            continue

        if i == min_idx:
            answer +=1

        elif i < min_idx :

            if a[i-1] < min_left :
                min_left = a[i-1]

            if a[i] < min_left:
                answer +=1

        else :
            min_right = min_arr[i+1]
            if a[i] < min_right:
                answer +=1


    print(answer)
    return answer


solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])