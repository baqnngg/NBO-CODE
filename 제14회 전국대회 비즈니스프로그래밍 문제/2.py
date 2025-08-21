def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

a = input()
d = []
#문자를 아스키 코드로 바꿔서 저장
st = ""
for i in a:
    b = ord(i)
    c = []
    while b != 0:
        c.insert(0, b % 8)
        b //= 8
    d.append(c)
for i in d:
    for j in i: st += str(j)

print(run_length_encode(st))