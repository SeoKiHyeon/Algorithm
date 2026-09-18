def solution(people, limit):
    
    people.sort()
    left, right = 0, len(people) - 1
    boat = 0
    
    while left <= right:
        if left != right and people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boat += 1
    
    answer = boat
    
    
    return answer