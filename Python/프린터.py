def solution(priorities, location):
    arrow = 0
    cnt = 1
    
    while True:
        if priorities[arrow] == max(priorities):
            priorities[arrow] = 0
            
            if arrow == location:
                return cnt
            
            cnt += 1
            
        arrow += 1
        arrow %= len(priorities)