class Solution(object):
    def isAlienSorted(self, words, order):
        records = []

        # find sequence pairs
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] == words[i+1][j]:
                    continue
                records.append([words[i][j], words[i+1][j]])
                break
        # return False if nothing collected
        if not records:
            return False
        # check whether the sequence in order is correct
        for record in records:
            if order.index(record[0]) > order.index(record[1]):
                return False
        return True


if __name__ == '__main__':
    words = ["word","world","row"]
    order = 'worldabcefghijkmnpqstuvxyz'
    S = Solution()
    print(S.isAlienSorted(words, order))
