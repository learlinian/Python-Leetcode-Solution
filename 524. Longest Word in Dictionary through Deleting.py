class Solution(object):
    def findLongestWord(self, s, dictionary):
        dictionary.sort()
        result = ''
        for word in dictionary:
            if len(word) <= len(result):
                continue
            s_copy = s
            possible = True
            for c in word:
                try:
                    i = s_copy.index(c)
                    s_copy = s_copy[i+1:]
                except:
                    possible = False
                    break
            if possible:
                result = word
        return result


if __name__ == '__main__':
    s = "abpcplea"
    dictionary = ["abccclllpppeeaaaa"]
    print(Solution().findLongestWord(s, dictionary))
