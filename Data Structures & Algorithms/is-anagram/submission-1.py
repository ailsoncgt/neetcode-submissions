class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if not char in t:
                return False
            letter_position = t.find(char)
            if letter_position == -1:
                return False
            t = t[:letter_position] + t[letter_position+1:]

        return True