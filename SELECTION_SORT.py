def selection_sort(A):
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
               
        temp = A[i]
        A[i] = A[min]
        A[min] = temp
        
    return A
A = [2, 10, 9, 2, 6, 8]
print(selection_sort(A))