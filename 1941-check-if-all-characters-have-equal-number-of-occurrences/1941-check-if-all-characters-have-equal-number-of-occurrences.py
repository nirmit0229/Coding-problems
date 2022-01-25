class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = {}
        for n in s:
            if n not in a:
                a[n]=s.count(n)
        counts = a.values()
        return len(set(counts))==1