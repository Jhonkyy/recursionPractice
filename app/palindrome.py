def palindrome(s :str):
    if len(s) == 0 or len(s) == 1:
        return print(f"la palabra {s} es palindroma")
    if s[0] != s[-1]:
        return False


print(palindrome("oso"))