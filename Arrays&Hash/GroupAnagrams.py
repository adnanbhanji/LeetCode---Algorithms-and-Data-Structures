class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store_anagrams = {}
        final_arr = []

        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in store_anagrams.keys():
                store_anagrams["".join(sorted(strs[i]))].append(strs[i])
            else:
                store_anagrams["".join(sorted(strs[i]))] = [strs[i]]
                final_arr.append(strs[i])
        

        return list(store_anagrams.values())

