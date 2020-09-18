"""
Practice
"""
import re

def practice0 () :
    regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'

    search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
    다스베이더 070-9999-9999 darth_vader@gmail.com
    princess leia 010 2454 3457 leia@gmail.com'''

    result = re.findall(regex, search_target)
    print(result) # list 형태로 안에 들어감
    #print("\n".join(result))

#practice0()

"""
\d : 숫자를 표현
\w : 문자 표현 (알파벳,한글,숫자) 모두 포함
\d+ : 숫자 하나혹은 그이상 연결된 것
? : 있거나 없거나
{2,3} : 2부터 3까지 반복한다
[a-z] : a~zRKwl
"""

regex = r'[1-9]\d*' #자연수 찾기
    
regex = r'\d+-?\d+-?\d+-?'

regex = r'\d+[ -]?\d+[ -]?\d+'

regex = r'\d{2,3}[ -]?\d{3,4}[ -]?\d{4}'