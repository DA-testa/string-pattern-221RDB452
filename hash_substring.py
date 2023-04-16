# python3

def read_input():
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
        return (pattern, text)
    elif input_type == 'F':
        with open("tests/06", "r") as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
        return (pattern, text)
    else:
        print("error")
        return
def print_occurrences(output):
    print(' '.join(map(str,output)))
def get_occurrences(pattern,text):
    pl = len(pattern)
    ph =sum(ors(c) for c in pattern)
    th = sum(ord(text[i]) for i in range(pl))
    tl= len(text)
    occur = []
    if ph == th and text[:pl] == pattern:
        occur.append(0)
    for i in range(1, tl - pl +1):
        th = th - ord(text[i - 1])+ ord(text[i + pl - 1])
        if ph == th and text[i:i + pl] == pattern:
            occur.append(i)
    return occur

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


