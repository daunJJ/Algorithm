NO_OF_CHARS = 128

# 호스풀 알고리즘의 시프트 테이블 
def shift_table(pat):
    m = len(pat)  # 패턴의 길이 
    tbl = [m]*NO_OF_CHARS  # 시프트 테이블 
    
    for i in range(m-1):  # 패턴의 모든 문자에 대해
        tbl[ord(pat[i])] = m-1-i  # 그 알파벳이 패턴의 몇번째 문자인지 
        # 각 문자의 ASCKII 코드에 해당하는 인덱스 위치에 문자열의 몇번 째 문자인지를 저장 
        # 패턴이 중복된 문자가 있다면 맨 오른쪽 문자에 의한 거리가 들어간다

    return tbl

# 호스풀 알고리즘 
def search_horspool(T, P):   
    m = len(P)  # 패턴의 길이
    n = len(T)  # 텍스트 입력의 길이
    t = shift_table(P)  # shift 테이블 생성 
    i = m-1  # 패턴의 우측 끝 문자 위치 
    while(i <= n-1):  # 가능한 모든 위치에 대해
        k = 0  # 매칭된 개수 
        while k <= m-1 and P[m-1-k]==T[i-k]:  # 패턴을 뒤에서 앞으로 맞지 않을 때까지 검사
            k += 1
        if k == m:  # 매칭 성공
            return i-m+1  # 매칭 위치(왼쪽) 반환
        else:
            i += t[ord(T[i])]  # T[i] 테이블을 참조하여 건너뜀 
    return -1

# 3번을 해보세요!
text = input()
pattern = input()


# 출력합니다!
print("패턴의 위치 :", search_horspool(text, pattern))