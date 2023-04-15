# python3

import numpy as np

def read_input():
    pattern = input().strip()
    text = input().strip()
    return pattern, text

def hash_func(s, p, x, m):
    h = np.zeros(m+1)
    h[0] = 0
    for i in range(1, m+1):
        h[i] = (x*h[i-1] + ord(s[i-1])) % p
    return h

def get_occurrences(pattern, text):
    p = 10**9+7
    x = np.random.randint(1, p-1)
    m, n = len(pattern), len(text)
    result = []
    p_hash = hash_func(pattern, p, x, m)[-1]
    h = hash_func(text, p, x, n)
    for i in range(n-m+1):
        if h[i+m]-x*h[i] == p_hash:
            if text[i:i+m] == pattern:
                result.append(i)
    return result

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print(" ".join(map(str, occurrences)))

