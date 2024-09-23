class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        n1=len(nums1)
        n2=len(nums2)
        nums3=[]
        while i<n1 and j<n2:
            if nums1[i]< nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        while i<n1:
            nums3.append(nums1[i])
            i+=1
        while j<n2:
            nums3.append(nums2[j])
            j+=1
        if len(nums3)%2==1:
            return nums3[len(nums3)//2]
        else:
            return (nums3[len(nums3)//2]+nums3[len(nums3)//2-1])/2