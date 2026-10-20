class Solution:

  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    res = right

    while left <= right:
      k = left + (right - left) // 2

      # Integer ceiling division: (p + k - 1) // k
      total_hours = sum((p + k - 1) // k for p in piles)

      if total_hours <= h:
        res = k
        right = k - 1
      else:
        left = k + 1

    return res