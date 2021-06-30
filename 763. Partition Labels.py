class Solution(object):
    def partitionLabels(self, s):
        if len(s) == 0:
            return [0]

        result = []
        last_i = 0
        prev_i = 0

        while last_i < len(s) - 1:
            prev_to_check = {s[last_i]}
            to_check = {s[last_i]}
            for i in range(last_i + 1, len(s)):
                if s[i] in prev_to_check:
                    prev_to_check = to_check.copy()
                    last_i = i
                    continue
                to_check.add(s[i])
            result.append(last_i - prev_i + 1)
            last_i += 1
            prev_i = last_i

        if prev_i == last_i == len(s) - 1:
            result.append(1)

        return result


if __name__ == '__main__':
    print(Solution().partitionLabels("eccbbbbdec"))
