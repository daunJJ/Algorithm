# 1번을 해보세요!
def selection_sort(A):
    # 여기에 코드를 작성해보세요!
    n = len(A)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if (A[j] < A[min]):
                min = j
        A[i], A[min] = A[min], A[i]
        printStep(A, i+1)
    return None

def printStep(arr, val):
    print("  Step %2d = " %val, end='')
    print(arr)

# 2번을 해보세요!
A = [int(n) for n in input().split()]

# 출력합니다!
print("Original  :", A)
selection_sort(A)
print("Selection :", A)