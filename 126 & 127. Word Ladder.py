import math

class Solution(object):
    '''function to check whether only 1 character is difference'''
    def check(self, word1, word2):
        same_num = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                same_num += 1
        if abs(same_num-len(word1)) == 1:
            return True
        else:
            return False

    '''find word sequence that reaches our end word'''
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:  # check whether word is in wordList. If not, exists directly
            return []
        self.result = []
        self.minlen = math.inf
        self.startfinding(beginWord, endWord, wordList, [])
        return self.result, self.minlen

    '''iteration function'''
    def startfinding(self, beginWord, endWord, wordList, temp):
        temp.append(beginWord)
        # print('temp: {}'.format(temp))
        # print('wordList: {}'.format(wordList))
        # print()
        if beginWord == endWord:    # if begin word is our end word, break the iteration
            # print(len(temp))
            '''append the list if list's length are equal. Redefine if list's length is shorter than minimum list.'''
            if len(temp) == self.minlen:
                self.result.append(temp.copy())
            elif len(temp) < self.minlen:
                self.result = [temp.copy()]
                self.minlen = len(temp)

        else:
            if wordList:
                for item in wordList.copy():    # iteration
                    # print('loop wordList: {}'.format(wordList))
                    # print('word:{}'.format(item))
                    if self.check(beginWord, item):
                        index = wordList.index(item)
                        del wordList[index]
                        self.startfinding(item, endWord, wordList.copy(), temp)
                        # print('deleted with wordlist:{}'.format(wordList))
                        temp.pop()


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    [ladder, minlen] = Solution().findLadders(beginWord, endWord, wordList)
    print(ladder, minlen)
