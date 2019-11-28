def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]      # count = [0]*3   => [0,0,0]
    answer = []      # return 할 리스트

    for i in range(len(answers)):  # 완전 탐색이라 하나씩 다 비교해보는 방법
        if answers[i] == student1[i%5]:   # student1의 리스트 길이는 5이기 때문에 순환주기인 5로 나눈 나머지를 리스트 요소 인덱스로 사용
            count[0] += 1
        if answers[i] == student2[i%8]:   # of course you can use 'len(student2)' instead of number
            count[1] += 1
        if answers[i] == student3[i%10]:  # But in this situation, student1,2,3 is not parameter so I used number
            count[2] += 1

    for i in range(3):    # max of count list is the highest score
        if count[i] == max(count):  # i starts 0, even if the score is the same,
            answer.append(i+1)  # it is automatically sorted in ascending order.
    return answer


  ### THE OTHER'S ANSWER ###

# def solution(answers):
#     p = [[1, 2, 3, 4, 5],
#          [2, 1, 2, 3, 2, 4, 2, 5],
#          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     s = [0] * len(p)
#
#     for q, a in enumerate(answers):    # enumerate returns both order and value ( parameter list )
#         for i, v in enumerate(p):   # student list
#             if a == v[q % len(v)]:  # q is parameter's order, q % len(v) is order number according to cycle
#                 s[i] += 1
#     return [i + 1 for i, v in enumerate(s) if v == max(s)]   # This answer doesn't have any list variable for return