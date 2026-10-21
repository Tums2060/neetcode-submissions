class Solution:
    def isAnagram(self, s, t):
        counts = {}


        for letter in s:
            counts[letter] = counts.get(letter, 0)+1

        for letter in t:
            counts[letter] = counts.get(letter, 0)-1

        return not any(counts.values())

    

        