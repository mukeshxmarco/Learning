class Solution:
    def possibleStringCount(self, word: str) -> int:
        last=word[0]
        f=True      
        ans=0
        idx=0

        for i in range(len(word)):
            if f and not last==word[i]:
                idx=i
                break
            elif f and last==word[i]:
                ans+=1

        words=0
        for i in range(idx,len(word)):
            if not word[i-1] == word[i]:
                words+=1
        
        other=len(word)-words-ans

        return ans+other
