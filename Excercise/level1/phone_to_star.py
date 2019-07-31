def solution(phone_number):
    for i in range(0, len(phone_number)):
        phone_number[:i] + "*" + phone_number[i+1:]
        return phone_number

'''
def solution(s): 의 형태로 변형할 수 없다.

    return "*"*(len(s)-4) + s[-4:]          
    
## str은 immmutable 하기때문에 s[3]='r'

'''