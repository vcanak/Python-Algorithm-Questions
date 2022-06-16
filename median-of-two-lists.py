def findMedianSortedArrays(nums1, nums2):
        m, n = len(nums1), len(nums2)
        mid_point = (m + n) // 2 + 1
        prev2 = prev1 = None
        i = j = 0

        for _ in range(mid_point):
            prev2 = prev1
            if j == n or (i != m and nums1[i] <= nums2[j]):
                prev1 = nums1[i]
                i += 1
            else:
                prev1 = nums2[j]
                j += 1
        
        if (m + n) % 2:
            return prev1
        else:
            return (prev1 + prev2) / 2

print(findMedianSortedArrays([1,2],[3,4]))