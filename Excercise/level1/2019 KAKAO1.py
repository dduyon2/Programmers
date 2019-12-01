from collections import Counter

def solution(N, stages):
    answer = []
    first = []
    stage = Counter(stages)
    all = len(stages)
    for i in range(N):
        if stage[i+1] == 0:        # 이부분을 추가 하기 전에는 runtime error가 났는데 모든 플레이어가 모든 스테이지를 클리어한 경우가 처리안된게 아닐까 싶다.
            first.append(0)
        else: first.append(stage[i+1]/all)
        all -= stage[i+1]

    sorted_list = sorted(first, reverse=True)
    for k in sorted_list:
        for i, v in enumerate(first):
            if v == k:
                answer.append(i+1)
                first[i]=2
                break
    return answer

##### THE OTHER'S SOLUTION #####
#
# def solution(N, stages):
#     result = {}    # DICTIONARY 를 사용해서 순위를 매기기에 훨씬 편리함을 확인할 수 있었던 문제.
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)   # 이 한줄로 내가 등수를 매기기 위해서 했던 For문이 퉁쳐지는거라 꼭 기억해야겠다.