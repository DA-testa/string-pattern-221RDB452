# python3

def read_input():
    pattern = ''
    text = ''
    chc = input().rstrip().lower()
    if chc == 't':
        pattern = input().rstrip()
        text =input().rstrip()
    elif chc == 'f':
        with open(input().rstrip(),'r') as F:
            pattern = F.readline().rstrip()
            text = F.readline().rstrip()
    return pattern,text
def print_occurrences(output):
    print(' '.join(map(str,output)))
def get_occurrences(pattern, text):
    p = 31
    m = 10**9+9
    occur = []
    pattern_hash= 0
    text_hash = 0
    p_pow=1
    for i in range(len(pattern)):
        pattern_hash =(pattern_hash*p+ord(pattern[i]))% m
        text_hash = (text_hash*p+ord(text[i])) % m
        p_pow =(p_pow*p) % m
    for i in range(len(text)-len(pattern)+1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occur.append(i)
        if i +len(pattern)<len(text):
            text_hash=(text_hash-ord(text[i])*p_pow) % m
            text_hash =(text_hash*p+ord(text[i+len(pattern)])) % m
    return occur

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))



