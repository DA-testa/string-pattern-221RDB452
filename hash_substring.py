# python3

def read_input_console():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def read_input_file():
    with open(input().rstrip(),'r') as f:
        pattern = f.readline().rstrip()
        text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    if not output:
        print("Pattern not found")
    else:
        print(' '.join(map(str,output)))

def get_occurrences(pattern, text):
    p = 31
    m = 10**9+9
    p_pow = pow(p, len(pattern), m)
    pattern_hash = sum(ord(c) * pow(p, i, m) for i, c in enumerate(pattern)) % m
    text_hash = sum(ord(c) * pow(p, i, m) for i, c in enumerate(text[:len(pattern)])) % m
    occur = []
    if pattern_hash == text_hash and pattern == text[:len(pattern)]:
        occur.append(0)
    for i in range(1, len(text)-len(pattern)+1):
        text_hash = (text_hash - ord(text[i-1]) * p_pow) % m
        text_hash = (text_hash * p + ord(text[i+len(pattern)-1])) % m
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occur.append(i)
    return occur

if __name__ == '__main__':
    chc = input().rstrip().lower()
    if chc =='t':
        pattern, text = read_input_console()
    elif chc=='f':
        pattern, text = read_input_file()
    else:
        print("Invalid choice")
        exit(1)
    print_occurrences(get_occurrences(pattern, text)))


