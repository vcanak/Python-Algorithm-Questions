"""
iven an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find minimum number of conference rooms required.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
"""
import heapq
#Greedy
def minMeetingRoomsGreedy(self, intervals) -> int:
        size = len(intervals)
        if size<=1: return size
        sorted_intervals = sorted(intervals)
        rooms=[[sorted_intervals[0][1]]]
        for i in range(1,size):
            booked = False
            for room in rooms:
                if sorted_intervals[i][0]>=room[-1]:
                    room.append(sorted_intervals[i][1])
                    booked = True
                    break
            if not booked:rooms.append([sorted_intervals[i][1]])
        return len(rooms)
    
def minMeetingRooms( intervals) -> int:
    size = len(intervals)
    if size<=1: return size
    heap = []
    for interval in sorted(intervals):
        if heap and interval[0]>=heap[0]:
            heapq.heappushpop(heap,interval[1])
        else:
            heapq.heappush(heap,interval[1])
        print(heap)
    return len(heap)



"version for can person  attend all meeatings"
def canAttendMeetings(intervals) -> bool:
        new_intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1,len(new_intervals)):
            if new_intervals[i-1][1] > new_intervals[i][0]:return False
        return True
    
print(minMeetingRooms( [(0,30),(5,10),(15,20)]))
print(canAttendMeetings( [(0,30),(5,10),(15,20)]))