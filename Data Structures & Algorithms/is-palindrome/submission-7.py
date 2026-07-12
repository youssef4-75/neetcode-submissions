class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz1234567890':
                res += i.lower()
        
        return res == res[::-1]