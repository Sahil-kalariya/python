# 100. Four Even Integers Summing to n

def test(n):
    for a in range(n, 0, -1):
        if not a % 2 == 0:
            continue
        for b in range(n - a, 0, -1):
            if not b % 2 == 0:
                continue
            for c in range(n - b - a, 0, -1):
                if not c % 2 == 0:
                    continue
                for d in range(n - b - c - a, 0, -1):
                    if not d % 2 == 0:
                        continue
            
                    if a + b + c + d == n:
                        return [a, b, c, d]

n = 1001
print(test(n))
