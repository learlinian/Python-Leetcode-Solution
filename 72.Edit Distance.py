class Solution(object):
    def minDistance(self, word1, word2):
        pre_info = []

        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        check_row = check_col = False

        for i in range(len(word2)):
            for j in range(len(word1)):
                if i == 0:
                    if not check_col and word1[j] == word2[i]:
                        try:
                            pre_info[i].append(pre_info[i][i-1])
                        except:
                            pre_info = [[0]]
                        check_col = True
                    else:
                        try:
                            pre_info[i].append(pre_info[i][i-1]+1)
                        except:
                            pre_info = [[1]]

                elif j == 0:
                    if not check_row and word1[j] == word2[i]:
                        pre_info.append([pre_info[i-1][0]])
                        check_row = True
                    else:
                        pre_info.append([pre_info[i-1][0]+1])
                else:
                    if word1[j] == word2[i]:
                        pre_info[i].append(pre_info[i-1][j-1])
                    else:
                        next_min = min(pre_info[i][j - 1], pre_info[i - 1][j], pre_info[i - 1][j - 1])
                        pre_info[i].append(next_min+1)
            # print(pre_info[i], len(pre_info[i]))
        return pre_info[-1][-1]


if __name__ == '__main__':
    word1 = 'intention'
    word2 = 'execution'
    print(Solution().minDistance(word1, word2))
