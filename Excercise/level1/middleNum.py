def solution(s):
    length = len(s)
    if length%2==0:  #짝수의 경우
        answer = s[(length//2)-1:(length//2)+1]
    else: answer = s[length//2]  #홀수의 경우
    return answer

'''
Other's  Solution >>

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]

'''