def josephus(n, k):
    people = list(range(1, n + 1))
    result = []
    idx = 0

    while people:
        idx = (idx + k - 1) % len(people)  # 원형 순회
        result.append(people.pop(idx))     # 제거 후 리스트 압축

    return result
n,m = map(int,input().split())
rst = josephus(n,m)
print(f"<{','.join(map(str,rst))}>")
