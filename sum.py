##Start
#Define a function that has an array of values
#Returns 


def solution(N):
   if not (1 <= N <= 200000):
       return "Invalid input"
   alphabet = "abcdefghijklmnopqrstuvwxyz"

   unique_letters = (N + 1) // 2  # Adding 1 ensures an equal number of occurrences

   # Create the string with equal occurrences of unique letters

   result = ""

   for i in range(unique_letters):

    #    result += alphabet[i] * 2  # Each letter occurs twice

   # If N is odd, add one more letter to make occurrences equal

   if N % 2 == 1:

       result += alphabet[unique_letters]

   return result

print(solution(5))