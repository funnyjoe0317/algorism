def solution(phone_book):
    hash_map = {}
    for number in phone_book:
        
        hash_map[number] =1 

    for phone_number in phone_book:
        juboo = ''
        for number in phone_number:
            juboo += number