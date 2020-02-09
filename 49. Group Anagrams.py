class Solution(object):
    def groupAnagrams(self, strs):
        results = {}
        for s in strs:
            s_characters = [i for i in s]
            s_characters.sort()
            sorted_s = ''.join(s_characters)

            if sorted_s in results.keys():
                results[sorted_s].append(s)
            else:
                results[sorted_s] = [s]
        result = list(results.values())
        return result


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))