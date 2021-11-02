def reorder_data(nums):
    x,y,dx,dy = 0,0,0,1

    for i in nums:
        if i == 'G':
            x,y = x+dx,y+dx
        elif i == 'L':
            dx,dy = -dy,dx
        else:
            dx,dy = dy,-dx

    return (x,y) ==(0,0) or (dx,dy) != (0,1)


nums = "GGLLGG"

print(reorder_data(nums))
