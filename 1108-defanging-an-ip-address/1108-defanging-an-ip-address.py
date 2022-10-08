class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for i in address:
            if i.isdigit():
                res.append(i)
            else:
                res.append("[.]")
        return ''.join(res)