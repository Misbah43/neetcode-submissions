class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            current_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    current_days += 1
                    current_load = w
                else:
                    current_load += w
            return current_days <= days

        low, high = max(weights), sum(weights)
        res = high

        while low <= high:
            mid = (low + high) // 2
            if can_ship(mid):
                res = mid
                high = mid - 1  # Try to find a smaller valid capacity
            else:
                low = mid + 1   # Capacity too small, need a larger one
                
        node = res
        return res
        