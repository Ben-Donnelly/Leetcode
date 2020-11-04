class Solution:
	def lengthOfLongestSubstring(self, s):
		if s == s[::-1]:
			return s

		temp = ""

		for i in range(len(s)):
			for j in range(len(s), 0, -1):
				current = s[i:j]
				if len(temp) >= len(current):
					break
				if current == current[::-1]:
					temp = current
		return temp
		# m = ''
		# for i in range(len(s)):
		# 	for j in range(len(s)):
		# 		y = s[j:i]
		# 		if len(m) >= j + i:
		# 			break
		# 		elif s[j:i] == s[j:i][::-1]:
		# 			m = s[j:i]
		# 			break

		# return m

s = Solution()
print(s.lengthOfLongestSubstring("dabay"))