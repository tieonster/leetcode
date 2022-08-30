# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


# Have a default dict to store result
# For each string, count the occurrences of each character and append the occurrences into the count list
# Then, append the count list to the result default dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Method 1 with m * n log n complexity
        sorted_words = {}
        res = []
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in sorted_words:
                sorted_words[sorted_word] = [word]
            else:
                sorted_words[sorted_word] += [word]
            
        for key, value in sorted_words.items():
            res.append(value)
            
        return res

#         # Method 2 using more efficient hashmap without sorting (Neetcode)
#         res = defaultdict(list)
        
#         for s in strs:
#             count = [0] * 26
#             for char in s:
#                 count[ord(char) - ord("a")] += 1
                
#             res[tuple(count)].append(s) 
            
#         return res.values()
            