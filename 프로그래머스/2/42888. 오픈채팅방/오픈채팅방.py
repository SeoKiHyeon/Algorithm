def solution(record):
    
    uid_dict = dict()
    
    for r in record:
        part = r.split()
        if part[0] in ("Enter", "Change"):
            uid_dict[part[1]] = part[2]
            
    answer = []
    
    for r in record:
        part = r.split()
        if part[0] == "Enter":
            answer.append(f"{uid_dict[part[1]]}님이 들어왔습니다.")
        elif part[0] == "Leave":
            answer.append(f"{uid_dict[part[1]]}님이 나갔습니다.")
            
    
    
    
    return answer