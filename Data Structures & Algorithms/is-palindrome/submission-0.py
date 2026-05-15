class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_sent = len(s)
        new_s = ""
        alf = "abcdefghijkmnlopqrstuvwxyz0123456789"
        for let in s:
            if let.lower() in alf:
                new_s += let.lower()
        for i in range(len(new_s)):
            if new_s[i] != new_s[len(new_s)-1-i]:
                return False
        return True
        