class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]", "", "".join(s.lower().split()))
        if s == s[::-1]:
            return True
        else:
            return False