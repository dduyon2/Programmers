def solution(array, commands):
    answer = []
    for num in commands:
        slice = array[num[0]-1:num[1]]
        slice.sort()
        answer.append(slice[num[2] - 1])
    return answer