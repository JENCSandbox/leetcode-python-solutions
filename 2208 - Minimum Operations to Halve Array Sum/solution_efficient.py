import heapq
class Solution(object):
    def halveArray(self, nums):
        priority_queue = [-n for n in nums]
        total = sum(nums)
        heapq.heapify(priority_queue)

        res, ans = 0,0
        while priority_queue:
            n = -heapq.heappop(priority_queue)
            if ans < total / 2:
                ans += n / 2
                res += 1
                heapq.heappush(priority_queue, -n/2)
            else:
                break
        return res
