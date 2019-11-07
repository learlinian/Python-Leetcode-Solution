class Solution(object):
    def find(self, board, word, index, i, j, reached_point):
        print(reached_point, index)
        # reach the end of the word
        if index == len(word):
            return True
        # move up
        if i - 1 >= 0 and [i - 1, j] not in reached_point and board[i - 1][j] == word[index]:
            # print('check point: {} {}'.format(i-1, j))
            reached_point.append([i - 1, j])
            if self.find(board, word, index + 1, i - 1, j, reached_point):
                return True
            del reached_point[-1]
        # move down
        if i + 1 < len(board) and [i + 1, j] not in reached_point and board[i + 1][j] == word[index]:
            # print('check point: {} {}'.format(i+1, j))
            reached_point.append([i + 1, j])
            if self.find(board, word, index + 1, i + 1, j, reached_point):
                return True
            del reached_point[-1]
        # move left
        if j - 1 >= 0 and [i, j - 1] not in reached_point and board[i][j - 1] == word[index]:
            # print('check point: {} {}'.format(i, j-1))
            reached_point.append([i, j - 1])
            if self.find(board, word, index + 1, i, j - 1, reached_point):
                return True
            del reached_point[-1]
        # move right
        if j + 1 < len(board[i]) and [i, j + 1] not in reached_point and board[i][j + 1] == word[index]:
            # print('check point: {} {}'.format(i, j+1))
            reached_point.append([i, j+1])
            if self.find(board, word, index + 1, i, j + 1, reached_point):
                return True
            del reached_point[-1]
        return False

    def exist(self, board, word):
        word_key = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[word_key]:
                    print('finding origin index: {} {}'.format(i, j))
                    if self.find(board, word, 1, i, j, [[i, j]]):
                        return True
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    # board = [["C","A","A"],
    #          ["A","A","A"],
    #          ["B","C","D"]]

    # board=[["a","a"]]
    word = "ABCB"
    print(Solution().exist(board, word))
