class Solution:#funny approach but the real soln is using binary search
    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        i,j,m1,m2=0,0,0,0

        for _ in range((n+m)//2 +1) :#  up to the mid value of the joind array
            m1=m2
            if i <m and j <n:
                if nums1[i]>nums2[j]:
                    m2=nums2[j]
                    j+=1
                else:
                    m2=nums1[i]
                    i+=1
            elif i< m:
                m2=nums1[i]
                i+=1
            else:
                m2=nums2[j]
                j+=1
        if (n+m)%2:
            return float(m2)
        else:
            return (float(m1)+float(m2))/2