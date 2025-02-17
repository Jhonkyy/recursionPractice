def palindrome(s):
    if len(s) == 1 or len(s) == 2:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

palindrome("oso")