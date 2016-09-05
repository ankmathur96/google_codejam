def count_inversions(s):
    current = s[0]
    inversions = 0
    for i in range(1,len(s)):
        if current != s[i]:
            inversions += 1
            current = s[i]
    if s[-1] == '-':
        inversions += 1
    return inversions

def greedy_inversions(s):
    print(s, len(s), '+' * len(s))
    if s == '+' * len(s):
        return 0
    else:
        n_flips = count_inversions(s)
        print(n_flips)
        return n_flips


