class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[count] == target:
                return count 
            else:
                count = count + 1

        return -1