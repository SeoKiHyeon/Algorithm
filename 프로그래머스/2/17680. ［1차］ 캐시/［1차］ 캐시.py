from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    deqe = deque()
    time = 0
    
    for city in cities:
        if len(deqe) == 0:
            deqe.append(city.upper())
            time += 5
        else:
            if city.upper() in deqe:
                deqe.remove(city.upper())
                deqe.append(city.upper())
                time += 1
            else:
                if len(deqe) < cacheSize:
                    deqe.append(city.upper())
                    time += 5
                else:
                    deqe.popleft()
                    deqe.append(city.upper())
                    time += 5
            
    
    answer = time
    return answer