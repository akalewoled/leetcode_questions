class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)
        nums1=quicksort(nums)
        for i in range(len(nums)):
            nums[i]=nums1[i]

        