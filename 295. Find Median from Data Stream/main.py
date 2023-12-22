class MedianFinder:

    def __init__(self):
      self.small, self.large = [], []

    def addNum(self, num: int) -> None:
      heapq.heappush(small, num * -1)

      if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
        val = -1 * heapq.heappop(self.small)

    def findMedian(self) -> float:
      if len(self.small) > len(self.large):
        return -1 * self.small[0]
