from collections import deque   # use deque library to make your life easier


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)    # set the variable to set so lookup time complexity would be O(1)

        q = deque()
        q.append((beginWord, 1))    # append the first element, with level 1
        while q:
            word, level = q.popleft()   # deque the most inner element
            if word == endWord:         # return current level if match has been found
                return level
            for word_i in range(len(word)):     # try each slot in word
                for c in [chr(i) for i in range(97, 123)]:  # try different character in each slot
                    w = word[:word_i] + c + word[word_i+1:]
                    if w in wordList:
                        wordList.remove(w)      # remove this node from the wordlist
                        q.append((w, level+1))
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    num = Solution().ladderLength(beginWord, endWord, wordList)
    print(num)
