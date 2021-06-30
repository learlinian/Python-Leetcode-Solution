class Solution(object):
    def countVowelPermutation(self, n):
        if n == 1:
            return 5
        next_mapping = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        count = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for _ in range(n - 1):
            next_count = count.copy()
            for k, v in count.items():
                for next_v in next_mapping[k]:
                    next_count[next_v] = (next_count[next_v] + v) % (10 ** 9 + 7)
                next_count[k] -= v
            count = next_count.copy()

        return sum(count.values()) % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().countVowelPermutation(5))
