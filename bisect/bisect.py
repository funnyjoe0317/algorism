def binary_search(target, data):
    start =0
    end = len(data) -1
    
    while start <= end:
        mid =(start+end)//2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid +1
        else:
            end = mid-1
    return None

from bisect import bisect
