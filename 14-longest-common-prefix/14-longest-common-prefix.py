class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        strs.sort()
        begin = strs[0]
        next = strs[-1]
        i = 0
        
        while i<len(begin) and i<len(next) and begin[i]==next[i]:
            i+=1
        return begin[:i]