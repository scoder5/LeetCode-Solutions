class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = list(map(lambda x: str(bin(x)[2:]).zfill(8),data))
        
        i = 0
        while i < len(data):
            count_ones = 0
            for j in data[i]:
                if j == '1':
                    count_ones += 1
                else:
                    break
            
            if count_ones == 1 or count_ones > 4:
                return False
            else:
                for _ in range(count_ones-1):
                    i += 1
                    if i >= len(data) or not data[i].startswith('10'):
                        return False
            
            i += 1
            
        return True