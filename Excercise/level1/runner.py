from operator import eq

def solution(participant, completion):
    answer = ''
    participant.sort()      # When I use sort() function, it might be found more useful
    completion.sort()
    flag = True
    for i in range(len(completion)):
        if not eq(completion[i], participant[i]):   # if the sorted lists don't match,
                answer = participant[i]   # then participant's element is answer
                flag = False
                break
    if flag:
        answer = participant[len(participant)-1]     # at last, if the sorted lists do match,
    return answer    # then participant's latest element is answer

#### THE OTHER'S SOLUTION ####

# import collections
#
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
    ##### collctions.Counter(participant) : Counter({'filipa': 1, 'josipa': 1, 'marina': 1, 'nikola': 1, 'vinko': 1})
#     return list(answer.keys())[0]