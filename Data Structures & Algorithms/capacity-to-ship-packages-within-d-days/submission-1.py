class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        result = 0
        while left <= right:
            capacity = (left + right) // 2
            days_needed = 1
            current_load = 0
            for weight in weights:
                if current_load + weight  <= capacity:
                    current_load += weight
                else:
                    days_needed += 1
                    current_load = weight

            if days_needed <= days:
                result = capacity
                right = capacity - 1
            else:
                left = capacity + 1
        return result 

        