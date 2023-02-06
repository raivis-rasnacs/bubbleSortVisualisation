import os
from time import sleep

nums = [11, 2, 1, 0, 8, 7, 4, 6, 12, 5, 9, 10, 3]

height = max(nums)
nums_map = [["" for _ in range(len(nums))] for _ in range(height)]

def showMap(mapToShow):
    for row in nums_map:
        for col in row:
            print(col, end=" ")
        print()

for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):

        sleep(0.1)
        os.system("cls")
        showMap(nums_map.reverse())

        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        for i, row in enumerate(nums_map):
            for j, col in enumerate(row):
                if i <= nums[j]:
                    nums_map[i][j] = "|"
                else:
                    nums_map[i][j] = " "
                    

