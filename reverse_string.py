# Write a function that reverses a string.
# The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverse_string(s: list[str]) -> list[str] :
    i = 0
    j = len(s) - 1
    while i < int(len(s) / 2):
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
        i += 1
        j -= 1
    return s


if __name__ == '__main__':
    print(reverse_string(['w','h','a','t']))

