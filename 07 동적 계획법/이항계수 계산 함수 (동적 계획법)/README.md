### 이항계수 C(n, k) 계산 함수(동적 계획법) | p.283
동적 계획법을 이용해 이항계수 C(n, k)를 계산하는 함수를 완성해 봅시다.

---

1. 동적 계획법으로 이항계수 C(n, k)를 계산하는 함수 bino_coef_dp(n, k)를 완성해 보세요.

* (n+1)x(k+1)의 2차원 테이블 C를 만들어요. 초깃값은 -1로 설정해요.
* 기반 상황인 경우 답을 테이블에 바로 저장해요.
* 일반 상황인 경우 저장된 답을 이용해 답을 계산한 후 결과를 다시 테이블에 저장해요.

2. n과 k의 값을 입력받아보세요. 첫 번째 줄에는 n에 입력될 자연수가 주어져요. 두 번째 줄에는 k에 입력될 자연수가 주어져요.