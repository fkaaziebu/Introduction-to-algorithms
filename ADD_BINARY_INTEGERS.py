def add_binary_integers(A, B):
    # Converting the binary arrays into integers
    a, b = 0, 0
    for i in range(len(A)):
        a += A[len(A)-1-i]*(2**i)
        b += B[len(A)-1-i]*(2**i)
    c, sum, C = a + b, 2**len(A), []
    #Converting the sum of a and b back to binary array
    for i in range(len(A)+1):
        if sum <= c:
            C.append(1)
        else:
            C.append(0)
            sum += 2**(len(A)-i)
            # should be done only once
        sum += 2**(len(A)-1-i)
    
    return C

A = [1, 0, 1, 1]
B = [0, 0, 0, 0]
print(add_binary_integers(A, B))