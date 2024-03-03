##START
#Define a function that takes in all the letters of the alphabet
#Use list comprehension to create a list where each element is the entire alphabet string (alphabet).
#The loop for _ in range(N // len(alphabet)) repeats N // len(alphabet) times, ensuring that the alphabet is repeated as many times as necessary to fill the string up to N characters.
#''.join(...): This joins all the elements in the list created by the list comprehension into a single string. The empty string '' is used as the separator, meaning there is no separation between the alphabet repetitions.
#Slice the alphabet string up to the index N % len(alphabet) - 1, which represents the remaining characters needed to fill the string to length N ensuring that the final string has exactly N characters.
##END

##BDD A function that returns a word with the number of letters provided


def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #slice the alphabet string up to the index N % len(alphabet) - 1
    return ''.join([alphabet for _ in range(N // len(alphabet))]) + alphabet[:N % len(alphabet)]

# Test cases
print(solution(5))  # Output: 'abcde'
print(solution(10)) # Output: 'abcdefghij'
print(solution(27)) # Output: 'abcdefghijklmnopqrstuvwxyz'