def solution(s):
    answer = ''
    count = 1 #자릿수(홀,짝)에 따라 대소문자 바꾸기 위해
    for ch in s:
        if ch == ' ': count = 1  # 공백은 다시 1로 자릿수 바꿔준다
        elif count%2 != 0:  # 짝수 자릿수
            ch = ch.upper()
            count += 1
        else:               # 홀수 자릿수
            ch = ch.lower()
            count += 1
        answer += ch
    return answer

##### Other's solution #####
#
# def toWeirdCase(s):
#     return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

## lambda x: "".join([a.lower() if i%2 else a.upper() for i, a in enumerate(x)])
# ==
# def func(x):
#   for i, a in enumerate(x):
#        if i % 2: a.lower()
#        else: a.upper()
# 후에 "".join(a) 차례차례 조인 하는 함수를 x라고 한다는 의미
# map(lambda x 함수, [파라미터(=" "를 기준으로 slice한 단어)])
# map를 통해 upper, lower한 단어를 다시 차례차례 " " 를 추가해 join한다.