##Start
#Define a function that has an array of values
#Returns 

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1
    num_dict = {}
    for num in A:
        digits = [int(d) for d in str(num)]  # Split the number into its digits
        sum_digits = sum(digits)  # Calculate the sum of digits
        if sum_digits in num_dict:
            max_sum = max(max_sum, num + num_dict[sum_digits])
        num_dict[sum_digits] = max(num, num_dict.get(sum_digits, -1))
    return max_sum

# Test cases
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))      # Output: 102
print(solution([51, 32, 43]))

