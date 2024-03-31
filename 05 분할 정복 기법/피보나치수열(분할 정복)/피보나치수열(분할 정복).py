# 분할 정복
# 시간 복잡도: O(n^2)
def fib(n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# 2번을 해보세요!
n = int(input())


# 출력합니다!
print(fib(n))