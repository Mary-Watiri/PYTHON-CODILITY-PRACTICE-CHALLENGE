def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join([alphabet for _ in range(N // len(alphabet))]) + alphabet[:N % len(alphabet)]

# Test cases
print(solution(5))  # Output: 'abcde'
print(solution(10)) # Output: 'abcdefghij'
print(solution(27)) # Output: 'abcdefghijklmnopqrstuvwxyz'