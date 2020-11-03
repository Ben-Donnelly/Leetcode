# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The
# answer is "abc",
# with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The
# answer is "b",
# with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The
# answer is "wke",
# with the length of 3.

# Example 4:
#
# Input: s = ""
# Output: 0
#
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
	def lengthOfLongestSubstring(self, s):
		lst = []
		count, temp = 0, 0
		for i in s:
			lst.append(i)
			if len(set(lst)) < len(lst):
				# If duplicate:
				# Slide window up
				# Note: if there are multiple substrings of same length this will return the latest one

				# Note this could also be achieved with just: if len(set(lst)) < len(lst): lst.pop(0)
				# however, this wil not return the substring in order and it could also mean the list
				# does in fact still have duplicates or it actually is not a substring at all.
				# However, for this scenario, it will work
				if temp > count:
					count = temp
					lst = lst[1:]
			temp += 1
		return len(lst)

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))