class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        for word in words:
            if len(result) == 0:
                result.append(word)
                continue
            if len(result[-1]) + len(word) < maxWidth:
                result[-1] = result[-1] + " " + word
            else:
                if maxWidth - len(result[-1]) > 0:
                    diff_len = maxWidth - len(result[-1])
                    count = result[-1].count(' ')
                    if count > 0:
                        number_of_spaces = diff_len // count + 1
                        extra_spaces = diff_len % count
                        result[-1] = result[-1].replace(' ', ' ' * number_of_spaces)
                        result[-1] = result[-1].replace(' ' * number_of_spaces, ' ' * (number_of_spaces + 1), extra_spaces)
                    else:
                        result[-1] += ' ' * diff_len
                result.append(word)
        result[-1] += (maxWidth - len(result[-1])) * ' '
        return result


if __name__ == '__main__':
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    print(Solution().fullJustify(words, maxWidth))
