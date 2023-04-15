# python3

def read_input():
    pattern, text = input().split()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31
    m = 10**9 + 9
    occur = []
    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash + ord(pattern[i]) * pow(p, i, m)) % m
    text_hash = 0
    for i in range(len(pattern)):
        text_hash = (text_hash + ord(text[i]) * pow(p, i, m)) % m
    p_pow = pow(p, len(pattern), m)
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occur.append(i)
        if i < len(text) - len(pattern):
            text_hash = (text_hash - ord(text[i]) * p_pow) % m
            text_hash = (text_hash * p + ord(text[i+len(pattern)])) % m
    return occur

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))




