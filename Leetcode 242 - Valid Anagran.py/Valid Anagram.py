
class Solution(object):
    def isAnagram(self, s, t):
        tarray = []
        sarray = []
        for letter in s:
            sarray.append(letter)
        for letter in t:
            tarray.append(letter)
        sarray.sort()
        tarray.sort()
        if(sarray == tarray):
            return True
        else:
            return False