def solution(n, arr1, arr2):
    answer = [""]*n   # for storing map
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:].zfill(n)  # after changing decimal to binary, match digit
        arr2[i] = bin(arr2[i])[2:].zfill(n)  # bin(10) = 0b1010, I need 1010 so use [2:]

    for i in range(n):
        for j in range(n):
            if (arr1[i][j]=="0")&(arr2[i][j]=='0'): answer[i] += ' '     # if arr1 and arr2 is 0, it can be blank
            else: answer[i] += '#'   # all of the other case would be wall (#)
    return answer

### THE OTHER'S ANSWER ###

# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):   # zip() function is creating an iterator that will aggregate elements from two or more iterables
#         a12 = str(bin(i|j)[2:])    # bin(i|j) : after changing dec to bin, do 'or' operation
#         a12=a12.rjust(n,'0')     # rjust() : Right justified and padded with zeros, if you don't write parameter '0', it will padded ' ' (blank)
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer