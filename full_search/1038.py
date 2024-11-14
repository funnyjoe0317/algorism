
# def solve(sequence, start):
#     if len(sequence) == M:  # 종료 조건: 길이가 M인 경우
#         print(" ".join(map(str, sequence)))  # 수열 출력
#         return
    
#     for i in range(start, -1, -1):
#     # for i in range(start, -1, N + 1):# start부터 N까지 반복
#         sequence.append(i)         # 선택한 숫자를 추가
#         solve(sequence, i -1)     # 재귀 호출, 다음 숫자는 i + 1부터 선택
#         sequence.pop()             # 백트래킹: 마지막 숫자 제거하여 이전 상태로 돌아감
        
from collections import deque

# import sys

# sys.setrecursionlimit(111111)

answer = 0
cnt = 0
arr = []
# n = int(sys.stdin.readline())
n=18

# Let's translate the given Kotlin function into Python and implement it

# List to store decreasing numbers
decreasing_numbers = []

# Function to add decreasing numbers recursively
def add_decreasing_number(number):
    decreasing_numbers.append(number)
    
    last_digit = number % 10
    if last_digit <= 0:
        return

    for i in range(last_digit - 1, -1, -1):
        new_number = number * 10 + i
        add_decreasing_number(new_number)

# Function to generate and retrieve the nth decreasing number
def find_nth_decreasing_number(n):
    global decreasing_numbers
    decreasing_numbers = []  # Reset list for fresh calculations
    
    # Populate decreasing numbers from 1 to 9 as initial seeds
    for i in range(1, 10):
        add_decreasing_number(i)
    
    decreasing_numbers.sort()  # Sort to ensure the correct sequence
    
    # Return the nth decreasing number or -1 if out of range
    return decreasing_numbers[n-1] if n <= len(decreasing_numbers) else -1

# Testing for n=18 to check if it outputs 42
# find_nth_decreasing_number(18)
# Let's print the entire sequence up to the 18th decreasing number to verify the sequence

# Reset and generate the sequence up to the 18th decreasing number
nth_number = 7
result = find_nth_decreasing_number(nth_number)

# # Print the decreasing numbers up to the nth position
# for i, num in enumerate(decreasing_numbers[:nth_number], start=1):
#     print(f"{i}: {num}")

# Confirm the 18th decreasing number
print(result)

    
    



