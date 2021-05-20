class Solution(object):
    def fallingSquares(self, positions):
        results = [0]
        heights = []
        for L, size in positions:
            if L + size > len(heights):
                heights += [0] * (L + size - len(heights))

            h = max(heights[L: L+size])
            heights[L: L + size] = [h + size] * size
            results.append(max(results[-1], h + size))
            print(heights)
        del results[0]
        return results


if __name__ == '__main__':
    positions = [[1,1],[2,2]]
    print(Solution().fallingSquares(positions))