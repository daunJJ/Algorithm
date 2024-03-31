# 1번을 해보세요!
def knapSack_fractional_greedy(obj, W): # [(이름, 무게, 가치)], 용량
    obj.sort(key=lambda o: o[2]/o[1], reverse=True)  # 단위 무게당 가치를 내림차순 정렬

    totalValue=0
    for o in obj:  # 하나의 물건에 대하여
        if W <= 0: break
        if W -o[1] >= 0:  # 해당 물건을 전부 넣을 수 있으면 전부 넣기
            W -= o[1]
            totalValue += o[2]  
        else:  # 전부 넣을 수 없으면 
            fraction = W / o[1]  # 해당 물건에서 넣을 수 있는 정도 (분수)
            totalValue += o[2] * fraction  # 그만큼 넣어줌 
            W = int(W - (o[1]*fraction))  # 넣은만큼 줄어든 용량 
    return totalValue


# 2번을 해보세요!
n = int(input())
obj = [(lambda name, weight, value: (name, int(weight), int(value)))(*input().split()) for _ in range(n)]
W = int(input())


# 출력합니다!
print("W =", W, obj)
print(knapSack_fractional_greedy(obj,W)) 