def palindrome_check(s: str) -> bool:
    head = 0
    tail = len(s)-1
    while head <= int(tail / 2):
        if s[head] != s[tail]:
            return False
        head += 1
        tail -= 1
    else:
        return True


if __name__ == '__main__':
    print(palindrome_check('racecar'))

