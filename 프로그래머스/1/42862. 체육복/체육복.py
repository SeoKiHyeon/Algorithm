def solution(n, lost, reserve):
    answer = 0
    
    clothes = [1] * n
    for i in lost:
        clothes[i-1] -= 1
    for j in reserve:
        clothes[j-1] += 1
    
    for i in range(n):
        if clothes[i] != 0:
            continue
        if i == 0:                          # 맨 앞: 오른쪽만 있음
            if clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] += 1
        elif i == n-1:                       # 맨 끝: 왼쪽만 있음
            if clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] += 1

        else:                                # 중간: 왼쪽 먼저, 안 되면 오른쪽
            if clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] += 1
            elif clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] += 1
        

            
    for i in range(n):
        if clothes[i] > 0:
            answer += 1
            

    return answer