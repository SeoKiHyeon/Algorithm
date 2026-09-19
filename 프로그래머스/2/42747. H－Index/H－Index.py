def solution(citations):
    
    citations.sort(reverse=True)
    max_cit = max(citations)
    
    if max_cit == 0:
        return 0
    
    for i in range(max_cit, -1, -1):
        
        big = 0
        
        for j in citations:
            if j >= i:
                big += 1

        
        if big >= i:
            answer = i
            break
    

    return answer