import math

with open('text_3_var_8.txt') as file:
    lines = file.readlines()
    
matrix = []

for line in lines:
    nums = line.strip().split(',')
    for i in range(len(nums)):
        if nums[i] == 'NA':
            prev_num = float(nums[i - 1])
            next_num = float(nums[i + 1])
            nums[i] = str((prev_num + next_num) / 2)
        
        filtered = []
    
    for item in nums:
        if item:
            num = float(item)
            if math.sqrt(num) > 58:
                filtered.append(num)

    matrix.append(filtered)

with open('output_3_var_8.txt', 'w') as result:
    for row in matrix:
        for num in row:
            result.write(str(int(num)) + ',')
        result.write('\n')
















# =============================================================================
# import math
# 
# with open('text_3_var_8.txt') as file:
#     lines = file.readline()
#     
# matrix = list()
# 
# for line in lines:
#     nums = line.strip().split(',')
#     for i in range(len(nums)):
#         if nums[i] == 'NA':
#             nums[i] = str((int(nums[i - 1] + nums[i + 1])) / 2)
#         
#         filtered = list()
#     
#     for item in nums:
#         num = float(item)
#         if math.sqrt(num) > 58:
#             filtered.append(num)
# 
#     matrix.append(filtered)
# 
# with open('output_3_var_8.txt') as result:
#     for row in matrix:
#         for num in row:
#             result.write(str(num) + ',')
#         result.write('\n')
# =============================================================================
        
