def solution(n, m):
    for i in range(m):
        star = '*' * n
        print(star)

solution(5, 3)

# for문을 사용안하고 할 수 있는 방법
# a, b = map(int, input().strip().split(' '))       //input으로 입력값 받는 방법
# answer = ('*'*a +'\n')*b
