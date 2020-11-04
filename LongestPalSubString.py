class Solution:
	def lengthOfLongestSubstring(self, s):
		if s == s[::-1]:
			return s

		temp = ""
		# start of string to the end
		# move up one char (every i)
		# remove last char (every j)
		for i in range(len(s)):
			for j in range(len(s), 0, -1):
				current = s[i:j]
				# if the length of out current longest substring is > the length left for us to check
				if len(temp) >= len(current):
					break
				if current == current[::-1]:
					temp = current
		return temp

s = Solution()
print(s.lengthOfLongestSubstring("dabay"))