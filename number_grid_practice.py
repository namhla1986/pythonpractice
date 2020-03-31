# These are lists which are placed withtin square brackets to look like grids
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# this is called a nested for loop. It is a loop within a loop
# if we wanted to print them out in grids i could just say print(row)
for row in number_grid:
    for col in row:
        print(col)