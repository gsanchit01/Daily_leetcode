class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod= 10 **9 + 7
        result=0
        
        #count array 
        count=[0]*101
        for no in arr:
            count[no]+=1
        
        for i in range (0,101):
            for j in range (i,101):
                
                k=target-i-j
                
                if k <0 or k> 100 :
                    continue
                    
                elif i==j and j==k:
                    result += (count[i] * (count[i]-1) * (count[i]-2) )/6
                    
                elif i ==j and j != k:
                     result += (count[i] * (count[i]-1) ) /2 * count[k]
                        
                elif i < j and j<k :
                    result += count[i] *count[j] * count[k]
                    
        return int(result % mod)