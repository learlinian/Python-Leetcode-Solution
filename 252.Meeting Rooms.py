def meeting_room(intervals):
    intervals = sorted(intervals)
    for index in range(1, len(intervals)):
        if intervals[index][0] < intervals[index - 1][1]:
            return False
    return True


if __name__ == '__main__':
    meetings = [[0, 30], [5, 10], [15, 20]]
    print(meeting_room(meetings))
