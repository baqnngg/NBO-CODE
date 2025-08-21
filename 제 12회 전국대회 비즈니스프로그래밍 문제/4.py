import sys
import re

def normalize(s: str) -> str:
    # 영문자만 남기고 소문자화
    return "".join(ch.lower() for ch in s if ch.isalpha())


s = sys.stdin.readline().rstrip("\n")  # 한 줄 입력(원문 그대로 유지)
words = []
for m in re.finditer(r"\S+", s):
    start, end = m.span()  # [start, end)
    raw = s[start:end]
    norm = normalize(raw)
    words.append((start, end, raw, norm))

n = len(words)
i = 0
outputs = []

while i < n:
    best_j = -1  # i에서 시작하는 가장 긴 회문 구간의 끝 인덱스
    concat = ""  # 누적 정규화 문자열 (i..j)
    for j in range(i, n):
        # 단어 내부 일부 문자열은 금지 → 단어 전체만 사용
        # 정규화된 단어를 이어붙여 검사
        concat += words[j][3]  # norm
        # 한 글자(총 길이 1)는 회문에서 제외
        if len(concat) >= 2 and concat == concat[::-1]:
            best_j = j

    if best_j != -1:
        # 가장 긴 것만 출력(내부 회문은 스킵)
        start_idx = words[i][0]
        end_idx = words[best_j][1]
        outputs.append(s[start_idx:end_idx])
        i = best_j + 1
    else:
        i += 1

# 결과 출력
for line in outputs:
    print(line)
