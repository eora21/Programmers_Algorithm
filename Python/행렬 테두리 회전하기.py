import copy

def solution(rows, columns, queries):
    
    def yx_rotate(y, x):
        if y == y1 and x != x2:
            x += 1
        elif x == x2 and y != y2:
            y += 1
        elif y == y2 and x != x1:
            x -= 1
        else:
            y -= 1
        return y - 1, x - 1
    
    nums = set()
    
    field = [[(row - 1) * (columns) + col for col in range(1, columns + 1)] for row in range(1, rows + 1)]
    
    for y1, x1, y2, x2 in queries:
        rotate_field = copy.deepcopy(field)
        ori_y, ori_x = y1 - 1, x1 - 1
        rot_y, rot_x = y1 - 1, x1
        
        min_num = rows * columns
        
        for _ in range((x2 - x1 + y2 - y1) * 2):
            rotate_field[rot_y][rot_x] = field[ori_y][ori_x]
            ori_y, ori_x = yx_rotate(ori_y + 1, ori_x + 1)
            rot_y, rot_x = yx_rotate(rot_y + 1, rot_x + 1)
            
            min_num = min(field[ori_y][ori_x], min_num)
        
        nums.add(min_num)
        field = rotate_field
    print(nums)
    return list(nums)

print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))