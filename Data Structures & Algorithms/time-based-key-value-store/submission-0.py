from collections import defaultdict


class TimeMap:

  def __init__(self):
    # key -> list of [timestamp, value]
    self.store = defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.store[key].append((timestamp, value))

  def get(self, key: str, timestamp: int) -> str:
    res = ""
    values = self.store.get(key, [])

    left, right = 0, len(values) - 1

    while left <= right:
      mid = left + (right - left) // 2
      t, val = values[mid]

      if t <= timestamp:
        res = val  # Valid candidate, try finding a larger timestamp <= target
        left = mid + 1
      else:
        right = mid - 1

    return res
        
