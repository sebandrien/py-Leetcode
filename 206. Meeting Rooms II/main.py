class Solution:
  def minMeetingRooms(self, intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    start_p, end_p = 0, 0

    while start_p < len(intervals
      if start[s] < end[e]:
        start_p += 1
        count += 1
      else:
        end_p += 1
        count -= 1
      res = max(res, count)
    return res
