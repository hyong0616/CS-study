def solution(words, queries):
    answer = []

    for query in queries:
        value = 0
        query_len = len(query)

        #전체가 ? 인경우
        if query[0] == '?' and query[-1] == '?':

            for word in words:
                if len(word) == len(query):
                   value = value +1

            answer.append(value)


        #접두사가 '?' 인경 우
        elif query[0] == '?':
            pos = 0

            #?가 아닌 부분까지 pos 움직임
            for i in range (0,len(query)):
                if query[i] != '?':
                    pos = i
                    break

            for word in words:
                if len(word) == len(query) and word[pos:] == query[pos:]:
                    value = value +1

            answer.append(value)

        #접미사가 ?인경우
        elif query[-1] == '?':
            pos = len(query)-1

            # ?인 부분까지 pos 움직임
            for i in range(0,len(query)):
                if query[i] == '?':
                    pos = i
                    break

            for word in words:
                if len(word) == len(query) and word[:pos] == query[:pos]:
                    value = value + 1

            answer.append(value)

    print(answer)
    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])