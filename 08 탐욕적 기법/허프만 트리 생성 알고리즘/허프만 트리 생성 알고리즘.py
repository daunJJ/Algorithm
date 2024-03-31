from queue import PriorityQueue
import heapq


# 허프만 트리 생성 알고리즘 
def make_heap_tree(freq, label):  # 빈도 수 배열, 알파벳 배열 
    q = PriorityQueue()
    n = len(freq)
    h=[]
    for i in range(n):  # 모든 문자를 최소힙에 삽입 
        q.put((freq[i], label[i]))

    for i in range(1,n):  
        e1 = q.get()  # 빈도 수 가장 작은 알파벳 
        e2 = q.get()  # 그 다음으로 작은 알파벳 
        q.put((e1[0]+e2[0], e1[1]+e2[1]))  # 숫자를 더하고, 문자열도 더하기 
        print(e1, "+", e2)
        
    print(q.get())  # 최종 트리의 루트 


# 2번을 해보세요!
label = [n for n in input().split()]
freq  = [int(n) for n in input().split()]


# 출력합니다!
make_heap_tree(freq, label)