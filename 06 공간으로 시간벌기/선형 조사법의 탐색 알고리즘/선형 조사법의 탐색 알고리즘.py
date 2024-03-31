M = 13					# 테이블의 크기
def hashFn(key) :		# 해시 함수
    return key % M

# 선형조사법의 탐색 알고리즘 
def lp_search(key) :
    id = hashFn(key)
    count = M 
    while count >0 :
        if table[id] == None:
            return None
        if table[id] == key:
            return table[id]
        id = (id + 1 + M) % M  # 해당 위치에 찾는 항목이 없으면 다음 위치 검사
        count -= 1
    return None


# 2번을 해보세요!
table = [None if m == "None" else int(m) for m in input().split()]
key = int(input())


# 출력합니다!
print(lp_search(key))