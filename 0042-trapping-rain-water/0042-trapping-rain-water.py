class Solution:
    def trap(self, height: List[int]) -> int:
        # the art is 
        #using some fuction to claculate from l to r
        # and using another fuction to calculate from left to right
        # if left poiner is greter than equal to right give right a chance to excute up to it becom less thn the right
        #when right gereter than left exute the left 
        ans = 0
        l,r = 0 , len(height) -1
        l_max, r_max = 0,0
        while l < r:
		# case 1: lower_bound is from left.
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    ans += l_max - height[l]
                l += 1
			# case 2: the lower_bound is from right
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    ans += r_max - height[r]
                r -= 1
            print(l,r)
            print(l_max,r_max)
            print(ans)

        return ans