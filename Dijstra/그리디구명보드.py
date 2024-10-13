def solution(people, limit):
    boat = 0
    i =0
    
    people.sort()
    
    j = len(people)-1
    while i<=j:
        
        if people[i]+people[j] <=limit:
            i += 1
        
        j-= 1
        boat +=1
    return boat

# people = 	[70, 80, 50] 
people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))