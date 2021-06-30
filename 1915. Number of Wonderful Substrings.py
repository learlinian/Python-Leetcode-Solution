class Solution(object):
    def wonderfulSubstrings(self, word):
        result = 0
        word_dict = {}
        for i in range(1024):
            word_dict[i] = 0
        word_dict[0] = 1
        w = 0

        for c in word:
            w ^= 1 << ord(c) - ord('a')
            for i in range(10):
                result += word_dict[w ^ 1 << i]
            result += word_dict[w]
            word_dict[w] += 1
        return result


if __name__ == '__main__':
    word = "aabb"
    print(Solution().wonderfulSubstrings(word))
