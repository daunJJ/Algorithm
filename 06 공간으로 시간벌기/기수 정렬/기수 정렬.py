# 파이썬 queue모듈의 Queue 를 사용해요!
from queue import Queue

# 기수 정렬 
def radix_sort(A) :
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())  # buckets 개의 큐 사용

    n = len(A)
    factor = 1
    for d in range(DIGITS):  # 모든 자릿수에 대해 
        for i in range(n):  # 해당 자릿수의 수에 따라 큐에 삽입
            queues[(A[i]//factor)%10].put(A[i]) 
            # 해당 숫자를 1, 10, 100으로 나누었을 때의 몫을 10,100,1000으로 나누었을 때의 나머지 == 주어진 숫자의 일의 자리 수
        j = 0
        for b in range(BUCKETS):  # 버킷에서 꺼내어 원래의 리스트로
            while not queues[b].empty():  # 큐가 공백일 때까지
                A[j] = queues[b].get()  # 원소를 꺼내 리스트에 저장 
                j +=1
        factor *= 10  # 그 다음 자릿수를 위해 


# 2번을 해보세요!
data = [int(n) for n in input().split()]


# 출력합니다!
BUCKETS = 10		# 10진법으로 정렬
DIGITS  = 4		# 최대 4 자릿수
radix_sort(data)						# 기수 정렬
print("Radix:", data)					# 결과 출력