# 배낭 채우기 알고리즘(분할 정복 기법)
def knapSack_dc(W, wt, val, n): 
    if n==0 or W==0:
        return 0
    if (wt[n-1]>W):  # 넣을 수 없음 
        return knapSack_dc(W,wt,val,n-1)  # 나머지 항목들로 처리
    else:
        valWithout = knapSack_dc(W,wt,val,n-1)  # 넣지 않았을 때
        valWith = val[n-1] + knapSack_dc(W-wt[n-1], wt, val, n-1) # 넣었을 때 
        return max(valWith, valWithout)


# 2번을 해보세요!
n = int(input())
val = [int(n) for n in input().split()]
wt = [int(n) for n in input().split()]
W = int(input())


# 출력합니다!
print("최대 가치:", knapSack_dc(W, wt, val, n)) 