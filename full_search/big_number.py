import re
import itertools

def solution(expression):
    # 가능한 모든 연산자 우선순위의 조합
    operators = ['+', '-', '*']
    operator_permutations = list(itertools.permutations(operators))

    # expression을 연산자와 숫자로 분리
    def split_expression(expression):
        return re.split(r'(\D)', expression)

    # 두 숫자를 연산자에 따라 계산하는 함수
    def calculate(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b

    max_value = 0
    tokens = split_expression(expression)

    # 각 우선순위 조합에 대해서 수식 평가
    for op_priority in operator_permutations:
        temp_tokens = tokens[:]
        for op in op_priority:
            stack = []
            while temp_tokens:
                token = temp_tokens.pop(0)
                if token == op:
                    prev = stack.pop()
                    next_value = temp_tokens.pop(0)
                    stack.append(calculate(op, int(prev), int(next_value)))
                else:
                    stack.append(token)
            temp_tokens = stack

        # 결과의 절댓값을 확인하여 최대값 갱신
        max_value = max(max_value, abs(int(temp_tokens[0])))

    return max_value

# 예시
expression = "100-200*300-500+20"
print(solution(expression))  # 출력: 60420
