class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(n):
            swap=False
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]= nums[j+1],nums[j]
                    swap=True #to optimize
            if not swap:
                break
        return nums
        
