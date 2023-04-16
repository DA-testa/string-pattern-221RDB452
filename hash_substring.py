# python3

def read_input():
    input_type == 'I':
        pattern = input().strip()
        text = input().strip()
        return (pattern, text)
    elif input_type == 'F':
        with open("tests/06", "r") as file:
            pattern = file.rreadline().strip()
            text = file.readline().strip()
        return (pattern, text)
    else:
        print("error")
        return
def print_occurrences(output):
    print(' '.join(map(str,output)))
def get_occurrences(pattern,text):
    p = 31
    m = 10**9+9
    occur = []
    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash+ord(pattern[i])*pow(p,i,m)) % m
    text_hash = 0
    for i in range(len(pattern)):
        text_hash = (text_hash+ord(text[i])*pow(p,i,m)) % m
    if pattern_hash == text_hash and pattern == text[:len(pattern)]:
        occur.append(0)
    p_pow = pow(p, len(pattern), m)
    for i in range(1,len(text)-len(pattern)+1):
        text_hash = (text_hash-ord(text[i-1])*p_pow) % m
        text_hash = (text_hash*p+ord(text[i+len(pattern)-1])) % m
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occur.append(i)
    return occur

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


