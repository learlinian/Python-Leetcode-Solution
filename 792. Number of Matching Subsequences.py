# slow solution. Time complexity O(m*n)
# class Solution(object):
#     def numMatchingSubseq(self, s, words):
#         result = 0
#         words_len = len(words)
#         i_list = [0] * words_len
#         for c in s:
#             for i in range(words_len):
#                 if i_list[i] == -1:
#                     continue
#                 if c == words[i][i_list[i]]:
#                     if i_list[i] == len(words[i]) - 1:
#                         i_list[i] = -1
#                         result += 1
#                     else:
#                         i_list[i] += 1
#         return result


class Solution(object):
    def numMatchingSubseq(self, s, words):
        words_list = []
        for _ in range(26):
            words_list.append([])
        result = 0

        for word in words:
            words_list[ord(word[0]) - ord("a")].append(word)
        for c in s:
            temp_list = []
            for word in words_list[ord(c) - ord("a")]:
                word = word[1:]
                if word == "":
                    result += 1
                    continue
                if word[0] == c:
                    temp_list.append(word)
                else:
                    words_list[ord(word[0]) - ord("a")].append(word)
            words_list[ord(c) - ord("a")] = temp_list.copy()

        return result


if __name__ == '__main__':
    s = "dsahjpjauf"
    words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    print(Solution().numMatchingSubseq(s, words))
