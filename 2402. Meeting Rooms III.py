import collections
import heapq


class Solution(object):
    def mostBooked(self, n, meetings):
        meetings = sorted(meetings)

        rooms_end_time = []
        vacant_room_number = [i for i in range(n)]
        heapq.heapify(vacant_room_number)
        rooms_count = collections.defaultdict(int)

        def clean_up_rooms(meetings_start_time):
            while len(rooms_end_time) > 0 and int(rooms_end_time[0]) <= meetings_start_time:
                prev_meeting = heapq.heappop(rooms_end_time)
                end_time = int(prev_meeting)
                room_number = int(prev_meeting * 10 - end_time * 10)
                heapq.heappush(vacant_room_number, room_number)

        for i in range(len(meetings)):
            # no available room and all meetings got delayed
            if len(vacant_room_number) == 0 and int(rooms_end_time[0]) > meetings[i][0]:
                prev_meeting = rooms_end_time[0]
                end_time = int(prev_meeting)
                # wait until the 1st available room appears
                meetings[i][0], meetings[i][1] = end_time, end_time + meetings[i][1] - meetings[i][0]
            clean_up_rooms(meetings[i][0])

            room_number = heapq.heappop(vacant_room_number)
            heapq.heappush(rooms_end_time, meetings[i][1] + 0.1 * room_number)
            rooms_count[room_number] += 1

        max_count = 0
        answer = 0
        # print(rooms_count)
        for room_number, count in rooms_count.items():
            if count > max_count:
                max_count = count
                answer = room_number
        return answer


if __name__ == '__main__':
    n = 2
    meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]

    print(Solution().mostBooked(n, meetings))
