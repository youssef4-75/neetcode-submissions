class Solution:
    def trap(self, height: List[int]) -> int:
        heights = [0] + height + [0]
        maximums = []
        start_declining = False 
        max_height_index = 0
        temp_maximums = []
        for i_, h in enumerate(heights[1:-1]):
            i = i_+1
            # print(heights[i-1], h, heights[i+1], h <= heights[i-1] or h <= heights[i+1])
            if h < heights[i-1] or h < heights[i+1]:
                continue 
            # print(h, i, heights[max_height_index], start_declining, h < heights[max_height_index])
            if h < heights[max_height_index]:
                while start_declining and temp_maximums and h > heights[temp_maximums[-1]]:
                    temp_maximums.pop()
                start_declining = True 
                temp_maximums.append(i)
            else: 
                max_height_index = i
                if start_declining:    
                    temp_maximums = []
                    start_declining = False
                maximums.append(i)
        # print(maximums)
        maximums.extend(temp_maximums)

        
        maximum_values = {}
        s = 0
        for j, i in enumerate(maximums[:-1]):
            maximum_values[i] = heights[i] if heights[i]<heights[maximums[j+1]] else heights[maximums[j+1]]
        if maximums: maximum_values[maximums[-1]] = 0
        # print(maximums, maximum_values)
        current_maximum = maximum_values.get(0, 0)
        for i, h in enumerate(heights):
            if i in maximum_values:
                current_maximum = maximum_values[i]
            s += max(0, current_maximum - h)
        return s
        
