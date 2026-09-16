from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_deque = deque()
        result = []
        for i in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[i]:
                max_deque.pop()   
            max_deque.append(i)     
            
            if max_deque[0] <= i - k:
                max_deque.popleft()
            
            if i >= k - 1:
                result.append(nums[max_deque[0]])
        return result