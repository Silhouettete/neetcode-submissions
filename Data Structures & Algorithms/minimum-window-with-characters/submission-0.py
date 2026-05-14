class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        countT = {}
        window = {}
        for i in t:
            countT[i] = 1 + countT.get(i,0)
        have = 0
        need = len(countT)
        res,res_length = [-1,-1],float('inf')
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1+window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if right - left + 1 < res_length:
                    res = [left,right]
                    res_length = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left+=1
        left,right = res
        return s[left:right+1] if res_length != float("inf") else ""

        