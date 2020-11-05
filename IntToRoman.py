class Solution:
	def intToRoman(self, num: int) -> str:
		res = ''
		l = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
				 ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
				 ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
				 ['', 'M', 'MM', 'MMM']]

		for i, v in enumerate(str(num)[::-1]):
			res = l[i][int(v)] + res

		return res

test = Solution()
print(test.intToRoman(9))