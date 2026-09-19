def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        numlist = array[i-1:j]
        numlist.sort()
        num = numlist[k-1]
        answer.append(num)
    
    
    return answer