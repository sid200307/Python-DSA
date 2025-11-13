#LeetCode Problem No.912 Sort an Array:-
class Solution:
    
    def sortArray(self, nums):
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        
        return self.merge(left, right)

    def merge(self, left, right):
        i = j = 0
        res = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])
        return res
nums[5,1,1,2,0,0]
S1=Solution()
S1.sortArray(nums)

