def solution(d, budget):
    bget= 0
    answer = 0
    d.sort()   # 가장 많이 분배할 수 있는 경우는 작은 예산부터 더했을 때의 총 개수이므로 오름차순정렬
    for i in d:
        if bget + i > budget: break   # 예산을 넘길 때는 예산가능그룹 count 늘리지않고 break
        bget += i
        answer += 1
    return answer