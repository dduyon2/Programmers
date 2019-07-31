def solution(n):
    answer="수박"
    return answer*(n//2) if n % 2 == 0 else answer*(n//2)+answer[0]


'''
Other's Solution >>

def water_melon(n):
    s = "수박" * n
    return s[:n]

'''