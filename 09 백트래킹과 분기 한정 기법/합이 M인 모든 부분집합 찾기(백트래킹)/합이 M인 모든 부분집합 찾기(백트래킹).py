# 리스트로 주어지는 입력 S에서 합이 M인 모든 부분집합 찾기 함수
def all_sum_of_subsets(S, M):
    DFS_sum_of_subsets(S, M, 0, [], sum(S))  # 루트부터 탐색 

# 합이 M인 모든 부분집합 찾기 
def DFS_sum_of_subsets(S, M, level, sol, remaining):
    if sum(sol) == M:  # 부분해 == 답
        print(sol)
        return
    if sum(sol) > M or (remaining+sum(sol))< M:
        return

    for i in range(level, len(S)):# 중복을 허용하지 않으므로 이전 원소는 처리할 필요 X
        sol.append(S[i])
        DFS_sum_of_subsets(S, M, i+1, sol, remaining-S[i])
        sol.pop()


# 2번을 해보세요!
nums = [int(n) for n in input().split()]
M = int(input())


# 출력합니다!
solution = all_sum_of_subsets(nums, M)
print("입력 집합 :", nums, "M=", M )