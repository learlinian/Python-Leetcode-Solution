class Solution(object):
    def longestPalindrome(self, s):
        queue = []              # the queue to store characters in string s
        longest_substring = ''  # string to store the longest string
        prev_index = 0          # index of the first element in queue

        """function to check whether an input array is palindromic"""
        def check_palindromic(array):
            arr = list(array)
            arr.reverse()
            if arr == array:
                return True
            return False

        for i in range(len(s)):
            queue.append(s[i])
            queue_len = len(queue)
            if check_palindromic(queue):    # if current queue array is palindromic
                if queue_len > len(longest_substring):
                    longest_substring = ''.join(queue)
            elif prev_index-1 >= 0 and s[i] == s[prev_index-1]:  # if added element makes the queue palindromic by
                queue.insert(0, s[prev_index-1])                 # the element before index prev_index, add it
                prev_index -= 1             # deduct prev_index by 1
                if queue_len + 1 > len(longest_substring):
                    longest_substring = ''.join(queue)
            else:
                while not check_palindromic(queue):     # delete the first element until the queue is palindromic
                    del queue[0]
                    prev_index += 1
            # print(queue, prev_index)
        return longest_substring


if __name__ == '__main__':
    arr = "cbbd"
    print(Solution().longestPalindrome(arr))
