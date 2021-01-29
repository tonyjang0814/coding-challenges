class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1,ptr2=0,0
        content = list()
        count,_sum = 0,0
        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1] <= nums2[ptr2]:
                content.append(nums1[ptr1])
                ptr1 += 1
            else:
                content.append(nums2[ptr2])
                ptr2 += 1
            count += 1
        
        while ptr1 < len(nums1):
            content.append(nums1[ptr1])
            ptr1 += 1
            count += 1
        while ptr2 < len(nums2):
            content.append(nums2[ptr2])
            ptr2 += 1
            count += 1
        if count == 1:
            return content[0]
        else:
            if count % 2 == 0: #if even length,
                mid = count//2 - 1
                return (content[mid] + content[mid+1])/2
            else:   # if odd length,
                mid = count // 2
                return content[mid]