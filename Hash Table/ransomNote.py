# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapping = {}
        i = 0
        
        for char in magazine:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1            
        
        for c in ransomNote:       
            if c not in mapping:
                return False        
            elif mapping[c] == 0:
                return False         
            else:
                mapping[c] -= 1

        return True