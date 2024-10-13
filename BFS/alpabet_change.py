def is_not_same(wor1,wor2):
    count = 0
    for i in range(len(wor1)):
        if wor1[i] != wor2[i]:
            count +=1
        if count > 1:
            return False
    return count == 1

def bfs( target, words, visited, begin):
    que =[[begin, 0]]
    
    # cnt = 0
    while que:
        cur_word, cnt = que.pop(0)
        # for i in range(len(words)-1):
        if cur_word == target:
            return cnt
        
        for i in range(len(words)):
            if not visited[i] and is_not_same(cur_word, words[i]):
                que.append([words[i], cnt+1])
                visited[i] = True

            # for word in words:
                
            # for j in range(len(words[i])):
            #     if cur_word[j] != words[i][j] and visited[i] ==False and is_not_same(cur_word, words[i]):
            #         word_list = list(cur_word)
            #         word_list[j] = words[i][j]
            #         new_word = ''.join(word_list)
            #         que.append([new_word, cnt+1])
            #         visited[i] =True
                    # cur = new_word
                    
    return 0
                    
            

def solution(begin, target, words):
    answer = 0
    visited = [] # 이거를 어떻게?
    if target not in words:
        return 0
    for i in range(len(words)):
        visited.append(False)
    print(visited)
    
    start = 0
    bfs( target, words, visited, begin)
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	

print(solution(begin, target, words))