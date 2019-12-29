def solution(s, n):
    answer = ""
    for ch in s:
        if ord(ch) == 32: answer += chr(32)  # 공백
        elif (ord(ch)+n >90) and (ord(ch)<=90): answer += chr(64+((ord(ch)+n)-90))
        #  대문자이지만 n만큼 뒤로 미뤘을 때 알파벳을 벗어나는 경우
        elif (ord(ch)+n >122) and (ord(ch)<=122): answer += chr(96+((ord(ch)+n)-122))
        #  소문자이지만 n만큼 뒤로 미뤘을 때 알파벳을 벗어나는 경우
        else: answer += chr(ord(ch)+n)
        #  대문자 소문자 관계없이 n만큼 미뤄도 알파벳을 벗어나지 않는 경우
    return answer
