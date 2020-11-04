class Solution:
	def reverse(self, x: int) -> int:
		ret = str(x)

		val = int(f"-{ret[:0:-1]}") if x < 0 else int(ret[::-1])

		return val if -2 ** 31 <= val <= 2 ** 31 - 1 else 0

print(Solution().reverse(-123))