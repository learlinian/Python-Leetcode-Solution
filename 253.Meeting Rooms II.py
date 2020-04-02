import heapq


class Solution1:
    def meeting_room(self, intervals):
        intervals.sort()
        rooms = 0
        meeting = []
        for interval in intervals:
            if not meeting:
                meeting.append(interval[1])
                rooms += 1
            else:
                if interval[0] >= meeting[0]:
                    heapq.heappushpop(meeting, interval[1])  # pop the first heap element
                else:
                    heapq.heappush(meeting, interval[1])
                    rooms += 1
        return rooms


class Solution2:
    def meeting_room(self, intervals):
        meeting_num = len(intervals)
        rooms = 0

        start = [0] * meeting_num
        end = [0] * meeting_num
        for index in range(meeting_num):
            start[index] = intervals[index][0]
            end[index] = intervals[index][1]

        start.sort()
        end.sort()
        end_i = 0
        for index in range(meeting_num):
            if start[index] < end[end_i]:
                rooms += 1
            else:
                end_i += 1
        return rooms


if __name__ == '__main__':
    meetings = [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]
    s = Solution2()
    print(s.meeting_room(meetings))
