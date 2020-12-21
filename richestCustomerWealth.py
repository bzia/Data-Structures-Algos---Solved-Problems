class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealth_max=0

        for customer in accounts:
            wealth=0

            for money in customer:
                wealth+=money

            if wealth_max<wealth:
                wealth_max=wealth

        return wealth_max 


# Time Complexity: O(n)
# Space Complexity: O(1) # only using extra space for the wealth variables

