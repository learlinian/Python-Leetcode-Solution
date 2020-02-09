class Solution(object):
    def romanToInt(self, s):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 1
        result = 0
        special = False
        for i in range(len(s)):
            # print(result)
            if special:
                special = False
                continue
            if i == len(s) - 1:
                result += (count * values[s[i]])
            else:
                if values[s[i+1]] > values[s[i]]:
                    result += (values[s[i+1]] - values[s[i]])
                    count = 1
                    special = True
                elif values[s[i+1]] < values[s[i]]:
                    result += (count * values[s[i]])
                    count = 1
                else:
                    count += 1
        return result


if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
