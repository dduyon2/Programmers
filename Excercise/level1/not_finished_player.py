def solution(participant, completion):
    if len(set(participant)) != len(set(completion)):
        answer=list(set(participant)-set(completion))
        return answer[0]
    else:
        for i in completion:
            if participant.count(i)>1 and participant.count(i)-1 == completion.count(i):
                answer = i
        return answer