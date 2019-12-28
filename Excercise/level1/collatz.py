def solution(num):
    answer = 0      # return 할 횟수
    while num != 1:
        if num%2 == 0:   # 짝수이면 계속 나눔
            num = num//2
        else: num = num*3+1  # 홀수면 3곱하고 1더하기
        answer += 1
        if answer >= 500:  # 횟수가 500이상일 경우 -1반환, 중지
            return -1
    return answer
