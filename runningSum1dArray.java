public class runningSum1dArray {
    
    public int[] runningSum(int[] nums) {
        
        int[] summed = new int[nums.length];
    
        summed[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            summed[i] = nums[i] + summed[i-1];
        }
    
        return summed;
       
    } 
}

// Time Complexity: O(N)
// Space Complexity: O(N)

