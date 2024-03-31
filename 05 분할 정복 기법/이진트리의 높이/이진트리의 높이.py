# 이진트리를 위한 노드 클래스
class TNode:
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크

# 이진트리의 높이
def calc_height(root) :
    if root is None:
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft, hRight) +1   # 더 높은 쪽에서 순환을 더 많이 하므로 더 커짐

# 트리 만들기
n = int(input())
binary_tree = [TNode(0,0,0) for _ in range(n)]
# [0]: 부모 노드, [1]: 왼쪽 자식 노드, [2]: 오른쪽 자식 노드, 없으면 -1

for i in range(n):
    data, left, right = [int(m) for m in input().split()][:3]

    binary_tree[i].data = data
    binary_tree[i].left = binary_tree[left-1] if left > 0 else None
    binary_tree[i].right = binary_tree[right - 1] if right > 0 else None

# 출력합니다!
root = binary_tree[0]
print("트리의 높이 =", calc_height(root))