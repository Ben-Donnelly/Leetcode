class Solution:
	def longestCommonPrefix(self, l) -> str:
		ret_val = ""

		# tuple of each of the first chars in each entry
		for i in zip(*l):
			if len(set(i)) != 1:
				break
			# if all the same just add first one
			ret_val += i[0]

		return ret_val
t = Solution()
t = t.longestCommonPrefix(["","",""])

print(t)
#
# extensionsToCheck = ['.pdf', '.doc', '.xls']
# if any(ext in url_string for ext in extensionsToCheck):
#     print(url_string)