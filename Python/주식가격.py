def solution(prices):
    stack = []
    answer = []
    for i in range(len(prices) -1 , -1, -1):
        while stack and stack[-1][0] >= prices[i]:
            del(stack[-1])
        answer.append(stack[-1][1] - i if stack else len(prices) - 1 - i)
        stack.append((prices[i], i))

    answer.reverse()
    return answer