def solution(a, b):
    answer = 0
    if a<b:
        for x in range(a, b+1):
            answer += x
    else:
        for x in range(b, a+1):
            answer += x      
    return answer

solution(3, 5)
solution(3, 3)
solution(5, 3)