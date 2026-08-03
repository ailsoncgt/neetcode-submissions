class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # O(1)
            return False

        # for char in s: # O(n)
        # # O(n + n + n) = O(3n) = O(c * n) = O(n)
        #     if not char in t: #O(n)
        #         return False
        #     letter_position = t.find(char) #O(n)
        #     if letter_position == -1: #O(1)
        #         return False
        #     t = t[:letter_position] + t[letter_position+1:] #O(n)
        # return True

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s == sorted_t

        s_hash = {}
        t_hash = {}
        for char in s:
            s_hash[char] = s_hash.get(char, 0) + 1
        
        for char in t:
            t_hash[char] = t_hash.get(char, 0) + 1
        
        return s_hash == t_hash








        