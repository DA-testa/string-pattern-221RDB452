# python3

import sys
def read_input():
    pattern = input().strip()
    text = input().strip()
    return pattern, text
def get_occurrences(pattern, text):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences
def print_occurrences(occurrences):
    print(len(occurrences))
    for index in occurrences:
        print(index, end=' ')


if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)





