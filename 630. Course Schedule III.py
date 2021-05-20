import heapq

class Solution:
    def scheduleCourse(self, C) -> int:
        heap, total = [], 0
        print(sorted(C, key=lambda el: el[1]))
        for dur, end in sorted(C, key=lambda el: el[1]):
            if dur + total <= end:
                total += dur
                heapq.heappush(heap, -dur)
            elif heap and -heap[0] > dur:
                total += dur + heapq.heappop(heap)
                heapq.heappush(heap, -dur)
        return len(heap)


if __name__ == '__main__':
    print(Solution().scheduleCourse([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]))