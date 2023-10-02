def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    if s == s[::-1]: return True
    else: return False
