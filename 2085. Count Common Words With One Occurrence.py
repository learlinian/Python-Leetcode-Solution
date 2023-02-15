class Solution(object):
    def get_counts(self, words):
        counts = {}
        for w in words:
            if w not in counts:
                counts[w] = 1
            else:
                counts[w] += 1
        return counts
    def countWords(self, words1, words2):
        result = 0
        counts1 = self.get_counts(words1)
        counts2 = self.get_counts(words2)

        keys = list(counts1.keys() if len(counts1) <= len(counts2) else counts2.keys())
        for k in keys:
            if k in counts1 and k in counts2 and counts1[k] == counts2[k] == 1:
                result += 1

        return result


if __name__ == '__main__':
    words1 = ["leetcode", "is", "amazing", "as", "is"]
    words2 = ["amazing", "leetcode", "is"]
    print(Solution().countWords(words1, words2))
