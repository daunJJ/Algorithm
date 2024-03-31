# 퀵 정렬 
def quick_sort(A, left, right) :
    if left < right:  #항목이 2개 이상인 경우
        mid = partition(A, left, right)  # 피봇을 기준으로 좌우 분할
        quick_sort(A, left, mid-1)  # 왼쪽 부분 리스트 정렬 
        quick_sort(A, mid+1, right)  # 오른쪽 부분리스트 정렬 


# 리스트 분할 
def partition(A, left, right) :
    low = left + 1  # 왼쪽 부분 리스트의 인덱스(증가방향)
    high = right  # 오른쪽 부분 리스트의 인덱스(감소방향)
    pivot = A[left]  # 첫번째 항목을 피봇으로 설정 
    while (low <= high):  # low와 high가 역전되지 않는 한 반복
        while low <= right and A[low] <= pivot: low+=1  # 증가하다가 피봇보다 크면 멈춤
        while high >= left and A[high] > pivot : high -= 1  # 감소하다가 피봇보다 작으면 멈춤

        if low < high:  # 두 인덱스가 역전되지 않았으면 
            A[low], A[high] = A[high], A[low]  # 두 항목을 교환 

    # low와 high가 역전되고 나면 
    A[left], A[high] = A[high], A[left]  # high가 가리키는 항목과 피봇을 교환 
    return high  # 피봇이 자신의 위치에 가게 됨 -> 피봇 위치 반환

# 3번을 해보세요!
data = [int(n) for n in input().split()]


# 출력합니다!
print("Original  : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)