class Solution(object):
    def countAndSay(self, n):
        def calculate(nums):
            count = 0       # count the repetitive appeared item
            output = ''     # output
            pre = ''        # record the previous checked character
            for num in nums:
                if pre and num != pre:
                    output = output + str(count) + pre
                    count = 1
                elif not pre or num == pre:
                    count += 1
                pre = num
            output = output + str(count) + pre
            return output

        last = '1'
        for _ in range(n-1):
            last = calculate(last)

        return last


if __name__ == '__main__':
    print(Solution().countAndSay(5))    # answer: 111221
