M = 13					# 테이블의 크기
table = [None]*M			# 테이블 만들기: None으로 초기화
def hashFn(key) :		# 해시 함수
    return key % M

# 선형조사법의 삽입 알고리즘
def lp_insert(key) :
    id = hashFn(key)
    count = M # 남은 위치의 개수
    while count >0 and (table[id] != None):  # 비어있는 자리 있지만, 해당 자리는 차있음
        id = (id + 1 + M) % M  # 다음 위치로 이동 
        count -= 1  # 검사할 남은 위치의 개수
    if count > 0:
        table[id] = key  # 해당 자리에 항목 저장 
    return


# 2번을 해보세요!
n = int(input())
for _ in range(n):
    lp_insert(int(input()))


# 출력합니다!
print(table)