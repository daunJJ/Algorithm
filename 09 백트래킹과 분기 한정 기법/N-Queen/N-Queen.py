# N-Queen 문제의 유효성 검사 
def isSafe(board, x, y):
    N = len(board)

    for i in range(y):
        if board[i][x] == 1: return False  # 세로방향 검사 
    for i, j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):  
        if board[i][j] ==1: return False  # 왼쪽 대각선 방향 검사 
    for i, j in zip(range(y-1, -1, -1), range(x+1, N)):
        if board[i][j] ==1: return False  # 오른쪽 대각선 방향 검사 
    return True  # 모든 방향으로 OK 이면 safe

# N-Queen 
def solve_N_Queen(board, y):
    N = len(board)
    if y == N:  # 하나의 해 탐색 성공 
        printBoard(board)
        return
    for x in range(N):  # 현재 y(행)에서 모든 x 테스트 
        if isSafe(board,x,y):
            board[y][x] = 1  #넣고 
            solve_N_Queen(board, y+1)  # 다음행 처리
            board[y][x] = 0  # 복구 

# 출력 함수
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# 3번을 해보세요!
N = int(input())


# 출력합니다!
board = [[0 for i in range(N)] for j in range(N)]
solve_N_Queen(board, 0)