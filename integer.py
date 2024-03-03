##START
#Define a function that has an array of values
#Returns the sum of the digits 
#if the there is not sum of two digits which are similar return -1
#Calculate the sum of the digits with similar sum of their individual digits
#Check for the maximum sum from the sums gotten
#Return the maximum sum
##END

##BDD An algorithm that returns the maximum sum of numbers within a given array with similar sum of the individual digits


def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1
    num_dict = {}
    for num in A:
        # Split the number into its digits
        digits = [int(d) for d in str(num)]  
        # Calculate the sum of digits
        sum_digits = sum(digits)  
        if sum_digits in num_dict:
            max_sum = max(max_sum, num + num_dict[sum_digits])
        num_dict[sum_digits] = max(num, num_dict.get(sum_digits, -1))
    return max_sum

# Test cases
print(solution([51, 71, 17, 42]))  
print(solution([42, 33, 60]))      
print(solution([51, 32, 43]))

