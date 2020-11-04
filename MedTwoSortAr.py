class Solution:
	def findMedianSortedArrays(self, nums, nums2):
		merged = sorted(nums + nums2)
		l_length = len(merged)

		target = l_length // 2
		if l_length % 2 == 0:
			return (merged[(target - 1)] + merged[target]) / 2

		return merged[target]

test = Solution()
test.findMedianSortedArrays([1,2], [3, 5])
