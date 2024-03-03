##START
#Define a function that calculates the total number of bricks
#Check if the total number of bricks can be evenly distributed among the boxes
#If not possible return -1
#Calculate the target number of bricks for each box
#Initialize the counter of moves





#BDD
# Function to calculate the number of moves required to ensure that each box has 10 bricks#
def solution(A):
    # Calculate the total number of bricks
    total_bricks = sum(A)
    
    # Check if the total number of bricks can be evenly distributed among boxes
    if total_bricks % len(A) != 0:
        return -1  # If not possible, return -1
    
    # Calculate the target number of bricks for each box
    target_bricks = total_bricks // len(A)
    
    # Initialize the counter for moves
    moves = 0
    
    # Iterate through each box of bricks
    for bricks in A:
        # If the number of bricks in a box is less than the target number
        if bricks < target_bricks:
            # Increment moves by the difference between target and current bricks
            moves += target_bricks - bricks
    
    # Return the total number of moves needed to equalize the boxes
    return moves

# Test cases
A = [11, 10, 8, 12, 8, 10, 11]
print(solution(A))  # Output: 7
A = [7, 14, 10]
print(solution(A))  # Output: -1
