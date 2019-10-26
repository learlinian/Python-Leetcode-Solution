class Solution(object):
    def isAlienSorted(self, words, order):
        records = []

        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] == words[i+1][j]:
                    continue
                records.append([words[i][j], words[i+1][j]])
                break

        for record in records:
            if order.index(record[0]) > order.index(record[1]):
                return False

        return True


if __name__ == '__main__':
    words = ["word","world","row"]
    order = 'worldabcefghijkmnpqstuvxyz'
    S = Solution()
    print(S.isAlienSorted(words, order))
