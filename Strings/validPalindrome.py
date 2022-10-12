# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # my own method
#         s = s.lower()
#         s = ''.join(ch for ch in s if ch.isalnum())
        
#         if s == "":
#             return True
        
#         for (charfront, charback) in zip(s, s[::-1]):
#             if charfront != charback:
#                 return False
#                 break
        
#         return True

# O(1) complexity
        l, r = 0, len(s)-1
    
        def alphaNum(char):
                return (ord("A") <= ord(char) <= ord("Z") or 
                       ord("a") <= ord(char) <= ord("z") or 
                       ord("0") <= ord(char) <= ord("9"))

        while l < r:
            # Skip alphanumeric characters (left pointer)
            while l < r and not alphaNum(s[l]):
                l += 1
            # Skip alphanumeric characters (right pointer)
            while r > l and not alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
                break
            l += 1
            r -= 1
        
        return True
                
                
        
                
                
        