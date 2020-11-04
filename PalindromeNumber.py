class Solution:
	def isPalindromeString(self, x: int) -> bool:
		check = str(x)
		return check == check[::-1]

	def isPalindromeNum(self, x: int) -> bool:
		# String is faster
		div = 1
		while x // div >= 10:
			div *= 10

		while x != 0:

			first_num = x // div
			last_num = x % 10

			if first_num != last_num:
				return False

			x = x % div // 10

			div /= 100

		return True


test = Solution()
print(test.isPalindromeNum(-121))
