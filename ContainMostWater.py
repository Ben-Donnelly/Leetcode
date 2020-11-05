class Solution:
	def maxArea(self, height):
		f = 0
		l = len(height)-1

		maxarea = 0

		while f < l:
			beg = height[f]
			end = height[l]

			# check if current is bigger or the smaller of the two sides of container * the length of the container
			maxarea = max(maxarea, min(beg, end) * (l-f))

			# move left pointer up one if left side < right
			# otherwise move right pointer down one
			if beg < end:
				f += 1
			else:
				l -= 1
		return maxarea

t = Solution()
l = [1,8,6,2,5,4,8,3,7]
t.maxArea(l)