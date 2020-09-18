def solution(numbers, hand) :

    answer = ''
    
    left_pos = [3,0]
    right_pos = [3,2]

    pad = [1,2,3,4,5,6,7,8,9,'*',0,'#']

    for number in numbers :

        idx = pad.index(number)
        num_pos = [idx//3, idx %3]

        #문자인 경우
        if  number == '*':
            left_pos = num_pos
            answer +='L'
        
        elif number == '#':
            right_pos = num_pos
            answer +='R'

        #숫자인 경우
        else :

            #무조건 left hand 사용해야하는 경우
            if number %3 ==1:
                left_pos = num_pos
                answer += 'L'

            #무조건 right hand 사용해야하는 경우
            elif number % 3 ==0 and number !=0 :
                right_pos = num_pos
                answer += 'R'

            #비교해야하는 경우
            else:
               
                left_dif = 0
                right_dif = 0

                left_dif = abs(left_pos[0]-num_pos[0]) + abs(left_pos[1]-num_pos[1])
                right_dif = abs(right_pos[0]-num_pos[0]) + abs(right_pos[1]-num_pos[1])

                if left_dif < right_dif:
                    left_pos = num_pos
                    answer+='L'
                elif left_dif > right_dif:
                    right_pos = num_pos
                    answer+='R'
                else :
                    if hand =='right':
                        right_pos = num_pos
                        answer+='R'
                    else:
                        left_pos = num_pos
                        answer+='L'
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")
