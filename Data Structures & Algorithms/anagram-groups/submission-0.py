class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        index = 0
        for i in range(0, len(strs)):
            sort = str(sorted(strs[i]))
            if sort not in dict:
                dict[sort] = index
                index += 1
        arr = []
        for i in range(0, len(dict)):
            arr.append([])
        for i in range(0, len(strs)):
            sort = str(sorted(strs[i]))
            arr[dict[sort]].append(strs[i])
        return arr
