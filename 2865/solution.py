class Solution(object):

    def aux_sum_of_heights(self, peak_position, max_heights):

        """
        :type maxHeights: List[int]
        :rtype: List[int]
        """
        n = len(max_heights)

        """
        To handle the left side of the peak
        j: 0 <=  j <= peak_position, starting  from peak_position
        max_left_height the max left height from the peak 
        """
        j = peak_position - 1 if peak_position - 1 >= 0 else 0
        max_left_height = max_heights[j] if max_heights[j] <= max_heights[peak_position] else max_heights[peak_position]

        """
        To handle the left side of the peak
        k: peak_position <=  k <= len(maxHeights), starting  from peak_position
        max_right_height the max right height from the peak 
        """
        k = peak_position + 1 if peak_position + 1 <= n - 1 else n - 1
        max_right_height = max_heights[k] if max_heights[k] <= max_heights[peak_position] else max_heights[peak_position]

        towers = []
        for i in range(0, n):
            towers.append(0)

        towers[peak_position] = max_heights[peak_position]
        towers[j] = max_left_height
        towers[k] = max_right_height

        while 0 <= j <= peak_position <= k <= n - 1:

            j = j - 1
            k = k + 1

            if j < 0 and k > n - 1:
                break

            if j < 0:
                j = 0

            if k > n - 1:
                k = n - 1

            if max_heights[j] < max_left_height:
                max_left_height = max_heights[j]
            towers[j] = max_left_height

            if max_heights[k] < max_right_height:
                max_right_height = max_heights[k]
            towers[k] = max_right_height
        return towers

    def maximumSumOfHeights(self, maxHeights):

        max_sum = 0
        n = len(maxHeights)
        position = 0

        while position <= n - 1:
            temp_towers = self.aux_sum_of_heights(position, maxHeights)

            if sum(temp_towers) > max_sum:
                max_sum = sum(temp_towers)
                max_towers = temp_towers

            position = position + 1

        return max_sum




solution = Solution()
print(solution.maximumSumOfHeights([5]))

