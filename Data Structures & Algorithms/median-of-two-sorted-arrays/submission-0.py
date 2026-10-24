class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        
        low, high = 0, m
        while low <= high:
            i = (low + high) // 2  # Partition index for nums1
            j = total_left - i      # Partition index for nums2
            
            # Elements around the partition
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if partitions are correct
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                # If total length is even
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            
            elif nums1_left_max > nums2_right_min:
                high = i - 1
            else:
                low = i + 1
        