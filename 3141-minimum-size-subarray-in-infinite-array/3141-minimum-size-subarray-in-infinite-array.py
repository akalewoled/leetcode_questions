class Solution:
  def minSizeSubarray(self, nums: List[int], target: int) -> int:
    s = sum(nums)
    num_cycles, target = target // s, target % s

    seen, curr, res = {0: -1}, 0, float('inf')
    for i in range(len(nums) * 2):
      curr += nums[i % len(nums)]
      seen[curr] = i
      if curr - target in seen:
        res = min(res, i - seen[curr - target])

    res += num_cycles * len(nums)
    return -1 if res == float('inf') else res