# python3

import numpy as np

def read_input():
    pattern = input().strip()
    text = input().strip()
    return pattern, text

def hash_substring(pattern, text):
    p_len = len(pattern)
    t_len = len(text)

    p_hash = hash(pattern)

    t_hashes = np.zeros(t_len - p_len + 1, dtype=np.int64)
    t_hashes[0] = hash(text[:p_len])
    for i in range(1, t_len - p_len + 1):
        t_hashes[i] = hash(text[i:i + p_len])

    matches = [str(i) for i in range(t_len - p_len + 1) if t_hashes[i] == p_hash]
    return ' '.join(matches)

if __name__ == '__main__':
    pattern, text = read_input()
    print(hash_substring(pattern, text))
