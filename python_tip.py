#python TIP

"""
1. divmod : 몫과 나머지 구하기
"""
def test1() :
    a, b = map(int, input().strip().split(' '))
    n_a, n_b = divmod(a,b)
    print(n_a,n_b)
    print(*divmod(a,b)) # *하면 unpacking 임
    #print(a//b, a%b)

"""
2-1. 진법 변환 int (x, base = 10)
2-2. enumerate 사용
"""

def test2_1() :
    num, base = map(int, input().strip().split(' '))
    snum = str(num)
    print(int (snum,base))

def test2_2() :
    num, base = map(int, input().strip().split(' '))
    num = str(num)
    answer = 0

    for idx, i in enumerate(num[::-1]):
        answer += int(i) * (base**idx)
    print(answer)


"""
3. 문자열 정렬
"""
def test3_1() : # 정렬함수 사용
    s, n = input().strip().split(' ')
    n = int(n) 
    print(s.ljust(n)) #좌측정렬
    print(s.center(n)) #가운데정렬
    print(s.rjust(n)) #우측정렬  

def test3_2() : #정렬함수 사용 안할 시
    s, n = input().strip().split(' ')
    n = int(n)
    tmp = n - len(s)
    print(s+' '*tmp)
    print(' '*(tmp//2)+ s+' '*(tmp//2))
    print(' '*tmp+s)
 

"""
4. 알파벳 출력 string 내장 상수 사용
"""
import string 

def test4_1() :
    num = int(input().strip())
    if num == 0:
        print(string.ascii_lowercase)
    else :
        print(string.ascii_uppercase)
    #string.ascii_letters 대소문자모두
    #string.digits 숫자모두

def test4_2() : #내풀이
    num = int(input().strip())
    code = 0
    if num == 0 : #소문자
        code = 97
    else :
        code = 65
        
    for i in range(0,26):
        print(chr(i+code),end='')

"""
5. 문자열 뒤집기 @@zip@@
"""

def test5_1(mylist):

    answer = list(map(list,zip(*mylist)))
    print(answer)
    return answer

def test5_2(mylist):
    
    answer = [[0]*len(mylist[0]) for _ in range(len(mylist))]

    for i,lst in enumerate(mylist) :
        for j,item in enumerate(lst) :
            answer[j][i] = item
    print(answer)
    return answer


"""
6-7. map 함수
"""
def test6(mylist):
    answer = []
    answer = list(map(int,mylist))
    return answer

def test7(mylist):
    answer = list(map(len, mylist))
    return answer

"""
8. join 함수 
"""

def test8(mylist) :
    answer = ''.join(mylist)
    print(answer)
    return answer


"""
9. 
"""
