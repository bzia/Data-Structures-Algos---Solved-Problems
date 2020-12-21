class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        for i in range(1, len(nums), 2):
            nums.insert(i, nums[i+n-1])
            nums.pop(i+n)
            n = n - 1
        
        
        return nums
    
    
# Time Complexity: O(n)
# Space Complexity: O(1) (modify array in place)