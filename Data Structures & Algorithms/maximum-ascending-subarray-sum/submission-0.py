class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
      

        for index, value in enumerate(nums):
            if index == 0 or value > nums[index - 1]:
                # Continue the ascending subarray by adding current value
                current_sum += value
                # Update the maximum sum if current sum is larger
                max_sum = max(max_sum, current_sum)
            else:
                # Start a new ascending subarray with current value
                current_sum = value
      
        # Return the maximum ascending sum found
        return max_sum
        