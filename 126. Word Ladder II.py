from collections import deque   # use deque library to make your life easier


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)  # set the variable to set so lookup time complexity would be O(1)
        output = []
        lowest_level = None
        visited = {beginWord: 1}    # dictionary to store the lowest level to reach each word

        q = deque()
        q.append(([beginWord], 1))    # append the first element, with level 1
        while q:
            word_list, level = q.popleft()   # deque the most inner element
            word = word_list[-1]    # get the last word in list as the beginWord
            if lowest_level is not None and level > lowest_level:   # break if it has surpassed
                break
            if word == endWord:
                if lowest_level is None:
                    lowest_level = level            # init the lowest level value
                output.append(word_list.copy())     # append to output
            else:
                for word_i in range(len(word)):     # try each slot in word
                    for c in [chr(i) for i in range(97, 123)]:   # try different character in each slot
                        w = word[:word_i] + c + word[word_i+1:]  # new word to be tested
                        if w in wordList:
                            # if the level is the same to the one with the lowest level
                            if w in visited and level + 1 == visited[w]:
                                q.append((word_list.copy() + [w], level + 1))
                            elif w not in visited:
                                visited[w] = level + 1
                                q.append((word_list.copy() + [w], level + 1))

        return output


if __name__ == '__main__':
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red",  "tad", "den", "rex", "pee", "tax"]
    vals = Solution().findLadders(beginWord, endWord, wordList)
    for val in vals:
        print(val)
