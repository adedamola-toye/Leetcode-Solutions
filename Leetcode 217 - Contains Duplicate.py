""" My first approach """

class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == 0:
            return None
        occurence_dict = {}
        for i in range(len(nums)):
            occurence_dict.update({str(nums[i]): 1})
        if (len(occurence_dict) < len(nums)):
            return True
        else:
            return False