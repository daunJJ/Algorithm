# 카운팅 정렬 
def counting_sort(A):
    output = [0] * len(A)  # 결과 저장용 리스트
    count = [0] * MAX_VAL  # 각 숫자의 빈도 저장 

    for i in A:
        count[i] += 1  # 리스트 안의 각 숫자에 대응되는 빈도수 세기

    for i in range(1, MAX_VAL):
        count[i]+= count[i-1]  # 누적 빈도 배열로 변환
        # count[i]가 가지는 값의 바로 전 인덱스까지 i가 저장될 수 있음

    for i in range(len(A)):  # 모든 입력항목 A[i]에 대해
        output[count[A[i]]-1] = A[i]  # 해당 위치( count[A[i]]-1 )에 저장 
        count[A[i]] -= 1  # 해당 값의 누적 빈도수를 -1

    for i in range(len(A)):  # 정렬 결과를 원래 배열에 복사 
        A[i] =output[i]



# 2번을 해보세요!
data = [int(n) for n in input().split()]


# 출력합니다!
MAX_VAL = 10
print("Original  : ", data)
counting_sort(data)             # 카운팅 정렬
print("Counting  : ", data)