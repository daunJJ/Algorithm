# 1번을 해보세요!
def insertion_sort(A) :
    n = len(A)
    for i in range(1,n):
        key = A[i]  # 각각의 값을 하나씪 key로 지정 
        j = i-1  # key 값의 바로 전 비교할 값
        while j >= 0 and A[j] > key:  # 비교할 값의 인덱스가 0 이상이고 비교할 값이 key값보다 크면 
            A[j+1] = A[j]  # key값 자리에 방금 비교한 값을 넣음 
            j = j - 1 # key 이전 인덱스로 이동하며 계속 우측으로 한칸씩 밀기 위함
        A[j+1] = key  # 최종적으로 key가 들어갈 자리에 key값을 끼워넣음
        printStep(A, i)

# 중간 과정을 출력하는 함수에요!
def printStep(arr, val) :
    print("  Step %2d = " % val, end='')
    print(arr)

# 2번을 해보세요!
data = [int(x) for x in input().split()]

# 출력합니다!
print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)