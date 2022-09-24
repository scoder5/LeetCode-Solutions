class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []
        for i in title.split():
            if len(i) < 3:
                res.append(i.lower())
            else:
                res.append(i.title())
                
        return ' '.join(res)