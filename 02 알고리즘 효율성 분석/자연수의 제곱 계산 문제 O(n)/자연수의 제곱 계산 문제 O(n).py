# 1번을 해보세요!
def compute_square_B(n):
    sum = 0
    # 복잡도가 O(n)이 되도록 반복문을 작성해보세요!
    for i in range(n):
        sum = sum + n
    return sum
    
# 2번을 해보세요!
n = None
n = int(input())

# 출력합니다!
print(compute_square_B(n))