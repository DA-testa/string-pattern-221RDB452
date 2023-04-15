# python3

import numpy as np

def read_input():
    pattern = input().strip()
    text = input().strip()
    return pattern, text

def precompute_hashes(text, pattern_len, prime, multiplier):
    hashes = np.zeros(len(text) - pattern_len + 1, dtype=int)
    hashes[-1] = polynomial_hash(text[-pattern_len:], prime, multiplier)
    for i in range(len(text) - pattern_len - 1, -1, -1):
        hashes[i] = (multiplier * hashes[i + 1] + ord(text[i]) - ord(text[i + pattern_len]) * pow(multiplier, pattern_len)) % prime
    return hashes

def polynomial_hash(s, prime, multiplier):
    h = 0
    for c in reversed(s):
        h = (h * multiplier + ord(c)) % prime
    return h

def get_occurrences(pattern, text):
    prime = 10**9 + 7
    multiplier = np.random.randint(1, prime)
    pattern_hash = polynomial_hash(pattern, prime, multiplier)
    hashes = precompute_hashes(text, len(pattern), prime, multiplier)
    return [i for i in range(len(text) - len(pattern) + 1) if pattern_hash == hashes[i]]

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print(" ".join(str(i) for i in occurrences))


