# 메모이제이션은 하향식으로 거꾸로 
def edit_distance_mem(S, T, m, n, mem): 
    if m == 0: return n  # S가 0 -> T의 문자열을 모두 S에 삽입
    if n == 0: return m  # T가 0 -> S의 문자열을 모두 T에 삽입 

    if mem[m-1][n-1] == None:  # 아직 해결되지 않은 문제이면 
        if S[m-1]==T[n-1]:  # S와 T의 마지막 문자가 같으면 
            mem[m-1][n-1] = edit_distance_mem(S,T,m-1,n-1,mem)

        else:
            mem[m-1][n-1] = 1 + \
             min(edit_distance_mem(S, T, m, n-1, mem),  # S에삽입
                 edit_distance_mem(S,T,m-1,n, mem),  # S를 삭제
                 edit_distance_mem(S,T,m-1,n-1, mem))  # S를 대체

    return mem[m-1][n-1]


# 2번을 해보세요!
S = input()
T = input()


# 출력합니다!
m = len(S)
n = len(T)
print("문자열:", S, T)
mem = [[None for _ in range(n)] for _ in range(m)] 
dist = edit_distance_mem(S, T, m, n, mem)
print("편집거리(메모이제이션)=", edit_distance_mem(S, T, m, n, mem))