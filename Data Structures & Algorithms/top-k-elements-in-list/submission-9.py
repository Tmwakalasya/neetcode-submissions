class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        map = Counter(nums)
        for key, value in map.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
        