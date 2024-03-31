# 배낭 채우기 알고리즘(동적 계획법)
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:  # i번째 물건이 배낭 용량을 추가
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w-wt[i-1]]  # 넣었을 때의 가치 
                valWithout = A[i-1][w]  # 넣지 않았을 때의 가치
                A[i][w] = max(valWith, valWithout)
    return A[n][W]


# 2번을 해보세요!
n = int(input())
val = [int(n) for n in input().split()]
wt = [int(n) for n in input().split()]
W = int(input())


# 출력합니다!
print("최대 가치:", knapSack_dp(W, wt, val, n)) 