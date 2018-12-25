from itertools import combinations_with_replacement as combs

def findMax(fmap):
    highest = -1
    
    for k, v in fmap.items():
        if v > highest:
            highest = v
            
    return highest

def checkSuperior(s, start, end, fmap):
    if (end - start + 1) // 2 <= findMax(fmap):
        return end - start + 1
    else:
        if fmap[s[end]] < fmap[s[start]]:
            fmap[s[end]] -= 1
            return checkSuperior(s, start, end - 1, fmap)
        else:
            fmap[s[start]] -= 1
            return checkSuperior(s, start + 1, end, fmap)

def solve(n, s):
    print(s)
    fmap = {}

    for c in s:
        if c in fmap:
            fmap[c] += 1
        else:
            fmap[c] = 1
        
    print(checkSuperior(s, 0, n - 1, fmap))

# for t in range(int(input())):
#     n, s = int(input()), input()
    
#     solve(n, s)

def ttos(t):
    s = ''

    for v in t:
        s += v

    return s

for i in range(5, 50):
    for p in combs('abcde', i):
        solve(i, ttos(p))
        
