class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        biggest = 0
        for  i in range(len(candies)):
            if candies[i] > biggest:
                biggest = candies[i]


        for  i in range(len(candies)):
            if candies[i] + extraCandies >= biggest:
                candies[i] = True
            else:
                candies[i] = False


        return candies

# Time Complexity: O(n)
# Space Complexity: O(1) # only using extra space for the 'biggest' variable

