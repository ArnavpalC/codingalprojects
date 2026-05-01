def get_substrings(s):
    n = len(s)
    result = []
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(s[i:j])
    
    return result


s = "anki"
subs = get_substrings(s)

for sub in subs:
    print(sub)
