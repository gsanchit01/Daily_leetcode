class Solution:
	def countVowelStrings(self, n: int) -> int:
		vowels = deque([5,4,3,2,1])
		sm = temp = sum(vowels)
		for i in range(1, n):
			for _ in range(5):
				vowels.append(temp)
				temp -= vowels.popleft()
				sm += temp
			temp = sm
		return vowels[0]