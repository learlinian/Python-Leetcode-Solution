class Solution(object):
    def letterCombinations(self, digits):
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        combination = []
        for digit in digits:
            if digit in mapping:
                if not combination:     # append all the items in list if it is empty
                    for item in mapping[digit]:
                        combination.append(item)
                else:
                    mapping_num = len(mapping[digit])
                    num_len = len(combination)  # number of items in
                    combination *= mapping_num  # duplicate the number of previous choices
                    i = 0

                    for item in mapping[digit]:
                        for j in range(i*num_len, (i+1)*num_len):
                            combination[j] += item
                        i += 1
        combination.sort()
        return combination


if __name__ == '__main__':
    s = '234'
    print(Solution().letterCombinations(s))
