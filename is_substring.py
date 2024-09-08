# Given two strings s and t, return true if s is a subsequence of t,
# or false otherwise.

def is_substring(s: str, t: str) -> bool:
    i = 0
    j = 0
    while j < len(t):

        if t[j] == s[i]:
            i += 1
        j += 1

    return i == len(s)


if __name__ == '__main__':
    print(is_substring('abc', 'aaaaaabbbdd'))
