class Solution:
    def countBits(self, n: int) -> List[int]:
        def bin_repr(num):
            count = 0
            a = bin(num)
            for i in range(len(a)):
                if a[i] == "1":
                    count += 1
                    
            return count
        
        ans = []
        for i in range(n+1):
            binr = bin_repr(i)
            ans.append(binr)
            
        return ans
            
        