class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        idx: 0   1   2   3   4
        A:   1   4   7   15
        B:   2   7   8   13  14
        
        
        """
        if len(A) > len(B):
            A, B = B, A
        
        alen, blen = len(A), len(B)
        lo, hi = 0, alen
        while lo <= hi:
            asplit = (lo + hi) // 2
            bsplit = (alen + blen + 1) // 2 - asplit
            
            a_left_max = -float('inf') if asplit == 0 else A[asplit - 1] 
            a_right_min = float('inf') if asplit == alen else A[asplit]
            b_left_max = -float('inf') if bsplit == 0 else B[bsplit - 1]
            b_right_min = float('inf') if bsplit == blen else B[bsplit]

            if a_left_max <= b_right_min and b_left_max <= a_right_min:
                if (alen + blen) % 2 == 0:
                    return (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2
                else:
                    return max(a_left_max, b_left_max)
            elif a_left_max > b_right_min:
                hi = asplit - 1
            else:
                lo = asplit + 1
