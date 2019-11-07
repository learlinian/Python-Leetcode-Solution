class Solution(object):
    def convert(self, s, numRows):
        return_array = []
        row_index = 0
        direction = '+'
        for char in s:
            try:
                return_array[row_index].append(char)
            except:
                return_array.append([char])
            if row_index == 0:
                direction = '+'
            elif row_index == numRows - 1:
                direction = '-'
            if direction == '+':
                row_index += 1
            elif direction == '-':
                row_index -= 1

        result = []
        for array in return_array:
            result = result + array

        return ''.join(result)


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    numRows = 1
    print(Solution().convert(s, numRows))
