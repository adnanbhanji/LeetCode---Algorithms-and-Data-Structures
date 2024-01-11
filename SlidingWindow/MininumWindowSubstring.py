class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        store = {}
        store2 = {}
        substr = ""
        counter = 0

        for i in range(len(t)):
            if t[i] not in store:
                store[t[i]] = 1
            else:
                store[t[i]] += 1

        for i in range(len(s)):
            if s[i] in store:    
                if s[i] not in store2:                
                    store2[s[i]] = 1
                else:
                    store2[s[i]] += 1
                
                if store2[s[i]] == store[s[i]]:
                    counter += 1
                
            while counter == len(store):
                temp_substr = s[left:i+1]
                if not substr or len(temp_substr) <= len(substr):
                    substr = temp_substr

                if s[left] in store:
                    store2[s[left]] -= 1
                    if store2[s[left]] < store[s[left]]:
                        counter -= 1

                left += 1

        return substr
