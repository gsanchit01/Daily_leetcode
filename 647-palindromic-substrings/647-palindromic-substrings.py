class Solution:
	def countSubstrings(self, s: str) -> int:
		l = res = len(s)

		def checker(i1, i2):
			nonlocal res
			while i1 > -1 and i2 < l:
				if s[i1] != s[i2]:
					return
				res += 1
				i1 -= 1
				i2 += 1

		for i in range(1, l - 1):
			prev, cur, nxt = s[i - 1], s[i], s[i + 1]

			if prev == cur:
				res += 1
				checker(i - 2, i + 1)

			if prev == nxt:
				res += 1
				checker(i - 2, i + 2)

		return res + 1 * (s[-1] == s[-2]) if l > 1 else res