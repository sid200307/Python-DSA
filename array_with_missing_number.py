# You are given an integer array A of length N. In array A, two integers are repeated, meaning two integers appear twice in the array.

# You need to transform the array into a valid permutation of integers from 1 to N using the following operation:

# In each operation, you can choose any element of the array and increase its value by 1.

# Task:
# Find and return an integer representing the minimum number of operations required to convert the array into a valid permutation of size N.

# Input1: 5
# Input2: [1, 1, 3, 3, 4]
# Output: 2

def min_operations_to_permutation(N, A):
    A.sort()
    operations=0
    for i in range(N):
        target = i + 1      # permutation should be 1..N
        if A[i] < target:
            operations += target - A[i]
            A[i] = target
    return operations

# Example usage:
N=5
A=[1, 1, 3, 3, 4]
print(min_operations_to_permutation(N, A))  # Output: 2

print(-(-5))