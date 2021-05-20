class Solution(object):
    def simplifiedFractions(self, n):
        result = []
        checked = {}
        for denominator in range(2, n + 1):
            for nominator in range(1, denominator):
                if float(nominator) / denominator not in checked.keys():
                    result.append("{}/{}".format(nominator, denominator))
                    checked[float(nominator) / denominator] = True
        return result


if __name__ == '__main__':
    print(Solution().simplifiedFractions(3))
