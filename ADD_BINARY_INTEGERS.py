def add_binary_integers(A, B):
    C = [0]*(len(A)+1)
    carry, j = 0, 0
    for i in range(len(A)):
        j = len(A) - 1 - i
        C[j] = (A[j] + B[j] + carry) % 2
        carry = (A[j] + B[j] + carry) // 2
    j -= 1
    C[j] = carry
    return C

A = [1, 0, 1, 1]
B = [0, 0, 0, 1]
print(add_binary_integers(A, B))