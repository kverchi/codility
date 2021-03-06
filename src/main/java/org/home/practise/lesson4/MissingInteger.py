# Level - Medium
#
# Find the smallest positive integer that does not occur in a given sequence.
#
# Solution - https://app.codility.com/demo/results/trainingCMCGSU-849/

def solution(A):
    n = len(A)
    counter = [0] * n
    for i in range(n):
        if A[i] > 0 and A[i] <= n:
            counter[A[i] - 1] += 1
    for i in range(n):
        if counter[i] == 0:
            return i+1
    return n + 1