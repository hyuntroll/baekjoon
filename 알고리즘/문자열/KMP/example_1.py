example_string = "ACBAACB"
example_string2 = "ACBAACBAABACBAACBC"

def fail_function(string: str) -> list[int]:
    lst = len(string)
    pi = [0] * lst
    j = 0
    for i in range(1, lst):
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1

        pi[i] = j
    return pi

def kmp_search(text: str, pattern: str, pi: list[int]):
    j = 0
    count = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            j = pi[j-1]
            count += 1
    return count

print(kmp_search(example_string2, example_string, fail_function(example_string)))