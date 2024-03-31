# 병합 정렬
def merge_sort(A, left, right) :  # left 와 right는 인덱스
    if left < right:  # 항목이 2개 이상인 경우
        mid = (left + right) // 2  # 리스트 균등 분할 
        merge_sort(A, left, mid)  # 부분 리스트 정렬
        merge_sort(A, mid+1, right)  #  부분 리스트 정렬 
        merge(A, left, mid, right)  # 병합 
    return None

# 병합 알고리즘 (정렬된 두 리스트의 병합 )
def merge(A, left, mid, right) :
    k =left  # 병합을 위한 임시 리스트의 인덱스
    i = left  # 왼쪽 리스트의 인덱스
    j = mid + 1  # 오른쪽 리스트의 인덱스
    while i<=mid and j<=right:
        if A[i] <= A[j]:  # 왼쪽 리스트의 값이 더 작으면 
            sorted[k] = A[i]  # 임시 리스트에 저장 
            i, k = i+1, k+1   # 왼쪽 리스트, 임시 리스트 한 칸씩 이동
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1
    
    if i > mid:  # 왼쪽 리스트에 있는 값 모두 복사
        sorted[k:k+right-j+1] = A[j: right+1]  # 남은 오른쪽 리스트 모두 복사
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]

    A[left:right+1] = sorted[left:right+1]  # 임시리스트를 A리스트에 다시 복사


# 3번을 해보세요!
data = [int(n) for n in input().split()]

# 출력합니다!
sorted = [0] * len(data)			# 길이가 len(data)인 임시 리스트를
print("Original  : ", data)			# 만들고 모든 항목을 0으로 초기화
merge_sort(data, 0, len(data)-1)	# 병합 정렬
print("MergeSort : ", data)