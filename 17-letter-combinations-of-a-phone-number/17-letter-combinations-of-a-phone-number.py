import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)==0): return []
        dic={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        lis=[]
        for i  in digits:
            lis.append(list(dic[i]))
        return ["".join(i) for i in itertools.product(*lis) ]