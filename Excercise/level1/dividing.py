def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    if len(answer) == 0: answer.append(-1)
    answer.sort()
    return answer


'''
Other's Solution

def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];  #for 문과  if 문을 한줄로 쓴 점이 배울 점!
    arr.sort();
    return arr if len(arr) != 0 else [-1];  # 코드에서 다른 변수를 사용하지않고 값을 직접 넣지 않고 리턴 값으로 구현한 것이 두번째 배울 점!
'''