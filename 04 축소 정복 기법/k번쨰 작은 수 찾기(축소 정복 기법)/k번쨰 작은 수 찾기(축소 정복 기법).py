# 1번을 해보세요!
def quick_select(A, left, right, k): 
    pos = partition(A, left, right)

    if(pos+1 == left+k):  # 피봇의 인덱스와 k번째로 작은 수가 동일 
        return A[pos]
    elif (pos+1 > left+k):  # 피봇의 인덱스가 k번보다 큼 (작은 것 중에 피봇의 인덱스를 다시 찾아야함)
        return quick_select(A, left, pos-1, k)
    else:
        return quick_select(A, pos+1, right, k-(pos+1-left))


# 2번을 해보세요!
def partition(A, left, right) :  # 분할의 기준이 되는 항목의 인덱스를 반환하는 함수
    low = left + 1
    high = right 
    pivot = A[left]  # 가장 왼쪽값 
    while (low <= high):
        while low <= right and A[low] <= pivot: low += 1  # 가장 왼쪽 값이 low 보다 크면, low를 그 다음으로 이동 -> 피벗보다 큰 항목을 찾으면 멈춤 
        while high >= left and A[high] > pivot: high -= 1  # 가장 왼쪽 값이 high보다 작으면, high를 그 전으로 이동 -> 피벗보다 작은 항목을 찾으면 멈춤

        # 애초에 아래 조건 만족하지 않고 low와 high의 위치가 바뀌면 아래 과정 생략됨
        if low < high:  # 현재 low: 가장 왼쪽 값보다 '큰' 값, high: 가장 왼쪽 값보다 '작은' 값 
            A[low], A[high] = A[high], A[low]  # 두 값을 교환
        # 이 과정을 반복하다가 멈추지 않고 low와 high의 위치가 역전되면 끝

    # high와 pivot(letf) 교환 
    A[left], A[high] = A[high], A[left]  
    return high  # 피봇이 새롭게 들어간 인덱스 


# 3번을 해보세요!
array = [int(x) for x in input().split()]
k = int(input())

# 출력합니다!
n = len(array)
print("입력 리스트 =", array) 
print("[축소정복] %d번째 작은 수: " %(k), quick_select(array, 0, n-1, k)) 