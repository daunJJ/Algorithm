### 호스풀 알고리즘 | p.242
문자열 매칭 알고리즘 중 호스풀 알고리즘을 구현한 함수 search_horspool(T, P)을 완성해 봅시다.

---

1. 호스풀 알고리즘의 시프트 테이블을 만드는 함수 shift_table(pat)을 완성해 보세요.

* pat은 패턴이에요.
* 크기가 NO_OF_CHARS인 리스트를 만들고, 모든 항목을 패턴의 길이로 채워요. 이것은 일단 모든 문자는 패턴에 없다고 생각하기 위함이에요.
* 패턴의 모든 문자에 대해 테이블의 해당 위치의 이동 거리를 계산해 넣어요. 만약 패턴에 중복된 문자가 있다면 맨 오른쪽 문자에 의한 거리가 최종적으로 들어가요. (반복문이 0부터 증가하는 방향으로 진행되기 때문이에요)

2. 호스풀 알고리즘을 구현한 함수 search_horspool(T, P)을 완성해 보세요.

* T는 텍스트, p는 패턴이에요.
* 패턴의 위치를 우측 끝 문자를 기준으로 뒤에서 앞으로 맞지 않을 때까지 검사해요.
* 패턴의 모든 문자가 일치하면 위치를 반환해요.
* 패턴의 어느 문자가 일치하지 않으면 테이블을 찾아 그만큼 건너뛰어요.
* search_horspool(T, P) 함수 내에서 shift_table(pat) 함수를 호출하여 shift 테이블을 생성해요.

3. 텍스트 text와 패턴 pattern을 입력받아 보세요. 첫 번째 줄에는 text에 저장될 문자열이 주어져요. 두 번째 줄에는 pattern에 저장될 문자열이 주어져요.