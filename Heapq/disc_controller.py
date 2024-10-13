import heapq

# def solution(jobs):
#     answer = 0
#     current_time = 0
#     total_time = 0
#     job_count = len(jobs)
#     task_heap = []
    
#     # 요청 시간을 기준으로 작업을 오름차순 정렬
#     jobs.sort(key=lambda x: x[0])
    
#     job_index = 0
#     jobs_completed = 0
    
#     # 작업이 모두 완료될 때까지 반복
#     while jobs_completed < job_count:
        
#         # 현재 시간보다 먼저 요청된 작업들을 모두 힙에 추가
#         while job_index < job_count and jobs[job_index][0] <= current_time:
#             heapq.heappush(task_heap, (jobs[job_index][1], jobs[job_index]))  # (작업 소요 시간, 작업)
#             job_index += 1
        
#         # 힙이 비어있다면 다음 작업을 요청 시간으로 현재 시간 갱신
#         if not task_heap:
#             current_time = jobs[job_index][0]
#         else:
#             # 작업 소요 시간이 가장 짧은 작업 처리
#             job_duration, task = heapq.heappop(task_heap)
#             request_time = task[0]
#             current_time += job_duration
#             total_time += (current_time - request_time)
#             jobs_completed += 1
    
#     # 평균 계산
#     answer = total_time // job_count
#     return answer

# jobs = 	[[0, 3], [1, 9], [2, 6]]
# solution(jobs)


import heapq


class Job(object):
    def __init__(self, begin=0, cost=0):
        self.begin = begin
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost


def solution(jobs):
    jobs.sort(key=lambda item: item[0])

    last_index = 1
    job_heap = [Job(begin=jobs[0][0], cost=jobs[0][1])]
    current_time = jobs[0][0]
    answer = 0
    while True:
        while last_index < len(jobs) and jobs[last_index][0] <= current_time:
            job = Job(begin=jobs[last_index][0], cost=jobs[last_index][1])
            heapq.heappush(job_heap, job)
            last_index += 1

        if len(job_heap) == 0:
            if last_index < len(jobs):
                job = Job(begin=jobs[last_index][0], cost=jobs[last_index][1])
                current_time = job.begin
                heapq.heappush(job_heap, job)
                last_index += 1
            else:
                break

        next_job = heapq.heappop(job_heap)

        current_time += next_job.cost

        answer += (current_time - next_job.begin)

    answer = int(answer/len(jobs))
    return answer


jobs = 	[[0, 3], [1, 9], [2, 6]]
solution(jobs)